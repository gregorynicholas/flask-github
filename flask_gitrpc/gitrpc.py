import logging
from json import loads, dumps
from urllib import urlencode
from datetime import datetime, timedelta
from flask_protorpc.proto import message_from_json, message_to_json
from werkzeug import exceptions
from github import messages
from github import requests
from github.orgs import orgs
from github.repos import repos
from github.users import users
from github.events import events
from github.issues import issues
from github.gitdata import gitdata
from github.pullreqs import pullreqs

__all__ = ['GitRpc', 'messages', 'requests']

class GitRpc:
  def __init__(self, app, config, access_token, username=None, password=None):
    if not app:
      raise ValueError('Github oauth app not passed to constructor.')
    if not access_token:
      raise ValueError('Github oauth access_token not passed to constructor.')
    self.app = app
    self.config = config
    self.access_token = access_token
    self._username = username
    self._password = password
    # api specific clients..
    self.orgs = orgs.Orgs(self)
    self.repos = repos.Repos(self)
    self.users = users.Users(self)
    self.events = events.Events(self)
    self.issues = issues.Issues(self)
    self.gitdata = gitdata.GitData(self)
    self.pullreqs = pullreqs.PullRequests(self)

  def set_auth_type(self):
    return 'OAUTH'

  def auth(self):
    return (self.username(), self.password())

  def request(self, http_verb, path, data=None):
    verb = http_verb.upper()
    methodmap = dict(
      GET=self.get,
      PUT=self.put,
      HEAD=self.head,
      POST=self.post,
      PATCH=self.patch,
      DELETE=self.delete)
    if verb in methodmap:
      return methodmap[verb](self._url(path))
    else:
      raise ValueError(
        'Invalid HTTP Method. Use: HEAD, GET, POST, PATCH, PUT, DELETE')

  def call(self, path=None, query=None, data=None, method='GET'):
    result = self.app.request(self._url(path, query),
      method=method,
      data=data,
      content_type='application/json',
      headers={'Accept': 'application/json'},
      token=self.access_token)
    if result.status == 401:
      raise exceptions.Unauthorized('''Error with Github api request:
        401, user is not authorized.''')
    elif result.status == 403:
      raise exceptions.MethodNotAllowed('''Error with Github api request:
        403, user is authenticated, but doesn't have permissions.''')
    elif result.status == 404:
      raise exceptions.NotFound('''Error with Github api request:
        404, data not found: %s''' % result.data)
    elif result.status > 299:
      raise exceptions.BadRequest(
        'Error with github api request: %s, %s' % (result.status, result.data))
    return result.data


  def head(self, path, query=None, msg_type=None):
    response = self.call(path, query=query, method='HEAD')
    return self._remote(response, msg_type)

  def get(self, path, query=None, msg_type=None):
    response = self.call(path, query=query, method='GET')
    return self._remote(response, msg_type)

  def post(self, path, query=None, data=None, msg_type=None):
    response = self.call(path, query=query, data=self.msg(data), method='POST')
    return self._remote(response, msg_type)

  def patch(self, path, query=None, data=None, msg_type=None):
    response = self.call(path, query=query, data=self.msg(data), method='PATCH')
    return self._remote(response, msg_type)

  def put(self, path, query=None, data=None, msg_type=None):
    response = self.call(path, query=query, data=self.msg(data), method='PUT')
    return self._remote(response, msg_type)

  def delete(self, path, query=None, data=None, msg_type=None):
    response = self.call(path, query=query, data=self.msg(data), method='DELETE')
    return self._remote(response, msg_type)

  def _url(self, path, query=None):
    params = {}
    if query and isinstance(query, dict):
      params.update(query)
    path += '?%s' % urlencode(params)
    print 'api request url path: %s' % path
    return path

  def _remote(self, response, msg_type=None):
    # print 'RESPONSE: %s' % response
    if msg_type is not None:
      # todo: i need a root node.. i don't knot if i can serialize anonymous
      # root lists.. so i'm serializing, adding root node, then encoding back
      # to a json str.. sorry for the waste.
      response = dumps({'response': response})
      try:
        return message_from_json(msg_type, response)
      except AttributeError, e:
        print 'AttributeError decoding json: %s\n\nRESPONSE: %s' % (e, response)
      return msg_type()
    else:
      return dict(
        headers=dumps({}), body=response)

  def msg(self, msg):
    if msg:
      return message_to_json(msg)

  def message_to_json(self, *args, **kwargs):
    return message_to_json(*args, **kwargs)

  def message_from_json(self, *args, **kwargs):
    return message_from_json(*args, **kwargs)

  def username(self, user):
    return self.user(user)

  def user(self, user):
    return self._username if user is None else user

  def password(self):
    return self._password

  def to_dt(self, value):
    '''Converts & returns a datetime object from an isoformat string.

      :param value: An isoformat string. ex: 2012-10-15T18:37:04-07:00
    '''
    dt, _, us = value.partition('.')
    dt = datetime.strptime(dt, '%Y-%m-%dT%H:%M:%S')
    return dt + timedelta(microseconds=int(us.rstrip('Z'), 10))

  def from_dt(self, value):
    '''Returns an isoformat string from a datetime object.

      :param value: Instance of a datetime.datetime object.
    '''
    return value.isoformat()
