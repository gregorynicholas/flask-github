import config
import logging
from flask import g, request
from flask.ext.oauth import OAuth, OAuthException
from flask.ext.protorpc import remote_request
from functools import wraps
from werkzeug import exceptions
from app.github.v0 import models

__all__ = ['authorized_handler', 'authorize_with_token', 'call',
'create', 'delete', 'update']

def __oauth_tokengetter(token='user', auth=None):
  # todo: if a new token has been generated, this should use the globals value,
  # add a new entry to the user's access_tokens, and update the previously
  # token with `archived=True`.
  # tk = g.auth.get_access_token('github')
  # return (tk.token, "")
  return (g.github_oauth_access_token, "")

def authorize_with_token(func):
  @wraps(func)
  def decorated(auth, *args, **kw):
    if auth is None:
      raise ValueError('auth not passed to authorize_with_token.')
    # since we need the auth'd user before we can setup the api config,
    tk = auth.get_access_token('github')
    g.github_oauth_access_token = None
    if tk:
      g.github_oauth_access_token = auth.get_access_token('github')
    # we update the config here..
    g.api_config = config.APIConfig(auth.get_user())
    if not g.api_config.formatted:
      raise ValueError('api_config not formatted.')
    g.api_app = create_api_app(g.api_config)
    g.api_app.tokengetter_func = __oauth_tokengetter
    return func(*args, **kw)
  return decorated

def authorized_handler(f):
  @wraps(f)
  @authorize_with_token
  def decorated(auth, *args, **kw):
    try:
      # twitter is oauth1..
      if 'oauth_verifier' in request.args:
        data = g.api_app.handle_oauth1_response()
      # github is oauth2..
      elif 'code' in request.args:
          data = g.api_app.handle_oauth2_response()
      else:
        data = g.api_app.handle_unknown_response()
      g.api_app.free_request_token()
    except OAuthException:
      # todo: invalidate current user's token..
      auth.archive_access_token(g.api_config.name)
      from flask import redirect
      return redirect('/v0/github?uid=%s&session_token=%s' % (g.uid,
        g.session_token))
    return f(auth=auth, data=data, *args, **kw)
  return decorated

@remote_request(models.rpc.RemoteResponse)
def create(path=None, data=None):
  if data:
    data = message_to_json(data)
  return call(path=path, data=data, method='POST')

@remote_request(models.rpc.RemoteResponse)
def update(path=None, data=None):
  if data:
    data = message_to_json(data)
  return call(path=path, data=data, method='PUT')

@remote_request(models.rpc.RemoteResponse)
def delete(path=None, data=None):
  if data:
    data = message_to_json(data)
  return call(path=path, data=data, method='DELETE')

@remote_request(models.rpc.RemoteResponse)
def call(path=None, access_token=None, api_app=None, data=None, method='GET'):
  if not access_token:
    access_token = g.github_oauth_access_token
  if not access_token:
    raise ValueError('''github api access_token not passed to method, and \
does not exist in flask globals.''')
  if not api_app:
    if hasattr(g, 'api_app'):
      api_app = g.api_app
    else:
      raise ValueError('''github api_app not passed to method, and \
does not exist in flask globals.''')
  result = api_app.request('admin/{}'.format(path), method=method,
    data=data, content_type='application/json', headers={
    'Accept': 'application/json',
    'X-Shopify-Access-Token': access_token})
  if result.status == 401:
    raise exceptions.NotFound('''Error with github api request:
      401, user is not authorized.''')
  elif result.status == 403:
    raise exceptions.NotFound('''Error with github api request:
      403, user is authenticated, but doesn't have permissions.''')
  elif result.status == 404:
    raise exceptions.NotFound('''Error with github api request:
      404, data not found.''')
  elif result.status > 299:
    raise exceptions.NotFound(
      'Error with github api request: %s, %s' % (result.status, result.data))
  return result.data

def create_api_app(config):
  return OAuth().remote_app(config.name,
    base_url=config.base_url,
    request_token_url=config.request_token_url,
    access_token_url=config.access_token_url,
    access_token_method='POST',
    authorize_url=config.authorize_url,
    consumer_key=config.api_key,
    consumer_secret=config.api_secret,
    request_token_params={'scope': config.scope})
