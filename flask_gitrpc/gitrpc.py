import logging
# import requests
from json import loads, dumps
from flask_protorpc import message_from_json, message_to_json

from .github.orgs import orgs
from .github.repos import repos
from .github.users import users
from .github.events import events
from .github.issues import issues
from .github.gitdata import gitdata
from .github.pullreqs import pullreqs


class AuthorizationError(ValueError):
  pass


class Github:
  def __init__(self, config, username, password):
    self.config = config
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

  def head(self, url):
    return self._send(requests.head(
      self._url(url), auth=self.auth()))

  def get(self, url, message_type=None):
    return self._send(requests.get(
      self._url(url), auth=self.auth()), message_type=message_type)

  def post(self, url, data=None, message_type=None):
    return self._send(requests.post(self._url(url),
      data=self.msg(data), auth=self.auth()), message_type=message_type)

  def patch(self, url, data, message_type=None):
    return self._send(requests.patch(self._url(url),
      data=self.msg(data), auth=self.auth()), message_type=message_type)

  def put(self, url, data=None, message_type=None):
    return self._send(requests.put(self._url(url),
      data=self.msg(data), auth=self.auth()), message_type=message_type)

  def delete(self, url, data=None, message_type=None):
    return self._send(requests.post(self._url(url),
      data=self.msg(data), auth=self.auth()), message_type=message_type)

  def _url(self, path):
    url = self.config.base_url + (path if (path[0] is '/') else ('/%s' % path))
    print 'request url: %s' % url
    return url

  def _send(self, response, message_type=None):
    # check for unauthorized (401) response..
    if response.status_code == 401:
      raise AuthorizationError(response.text)
    elif response.status_code > 400:
      print 'ERROR: %d' % response.status_code
      print 'response: %s' % response.text
      print 'response: %s\n' % dir(response)
    if message_type is not None:
      # todo: i need a root node.. i don't knot if i can serialize anonymous
      # root lists.. so i'm serializing, adding root node, then encoding back
      # to a json str.. sorry for the waste.
      # print response.content
      _data = dumps({'response': loads(response.content)})
      try:
        return message_from_json(message_type, _data)
      except AttributeError, e:
        print 'AttributeError decoding json: %s: %s' % (e, _data)
      return message_type()
    else:
      return dict(
        headers=dumps(response.headers),
        body=response.content)

  def msg(self, msg):
    if msg:
      return self.client.message_to_json(msg)

  def message_to_json(self, *args, **kwargs):
    return message_to_json(*args, **kwargs)

  def message_from_json(self, *args, **kwargs):
    return message_from_json(*args, **kwargs)

  def username(self, user):
    return self._username if user is None else user

  def password(self):
    return self._password
