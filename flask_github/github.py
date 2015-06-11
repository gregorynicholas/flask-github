from __future__ import unicode_literals
import logging
from json import dumps
from urllib import urlencode
from urllib2 import Request, urlopen
from datetime import datetime, timedelta
from flask_protorpc.proto import message_from_json, message_to_json
from werkzeug import exceptions
from client.orgs import orgs
from client.repos import repos
from client.users import users
from client.events import events
from client.issues import issues
from client.gitdata import gitdata
from client.pullreqs import pullreqs


__all__ = ['Github']


class Github:
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
    # this avoids the request being sent as a GET when there is no data..
    if method == 'POST' and (data is None or len(data) < 1):
      data = '{}'
    result = '{}'
    status = 200
    request = Request(self._url(self.app.base_url + path, query),
      data=data, headers={
        'Content-Type': 'application/json',
        'Authorization': 'bearer ' + self.access_token})
    rate_limit = 0
    rate_limit_remaining = 0
    user_scopes = []
    accepted_scopes = []
    try:
      response = urlopen(request)
      result = response.read()
      response.close()
      status = response.code
      # parse info from github api response headers..
      rate_limit = int(response.headers.dict.get(
        'x-ratelimit-limit', 0))
      rate_limit_remaining = int(response.headers.dict.get(
        'x-ratelimit-remaining', 0))
      user_scopes = response.headers.dict.get(
        'x-oauth-scopes', '').split(',')
      accepted_scopes = response.headers.dict.get(
        'x-accepted-oauth-scopes', '').split(',')
      print 'rate_limit: %s' % (rate_limit)
      print 'rate_limit_remaining: %s' % (rate_limit_remaining)
      print 'user_scopes: %s' % (user_scopes)
      print 'accepted_scopes: %s' % (accepted_scopes)
    except:
      import traceback
      print 'HttpError: %s' % traceback.format_exc()

    # response = self.app.request(self._url(path, query),
    #   method=method, data=data, content_type='application/json',
    #   headers={
    #     'Accept': 'application/json',
    #     'Authorization': self.access_token},
    #   token=self.access_token)
    # result = dumps({'response': response.data})
    # todo: i need a root node.. i don't knot if i can serialize anonymous
    # root lists.. so i'm serializing, adding root node, then encoding back
    # to a json str.. sorry for the waste.
    # status = response.status

    if status == 401:
      raise exceptions.Unauthorized('''Error with Github api request:
        401, user is not authorized: %s.''' % result)
    elif status == 403:
      raise exceptions.MethodNotAllowed('''Error with Github api request:
        403, user is authenticated, but doesn't have permissions.''')
    elif status == 404:
      raise exceptions.NotFound('''Error with Github api request:
        404, data not found: %s''' % result)
    elif status > 299:
      raise exceptions.BadRequest(
        'Error with github api request: %s, %s' % (status, result))
    return '{"response": ' + result + '}'


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
