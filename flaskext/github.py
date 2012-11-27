'''
  usage:
    from gitrpc import github
    client = github.Github('<username>', '<password>')
    repos = client.repos.list_repos()
    repo = repos[0]
    commits = client.repos.commits.list_commits('<repo_name>')
'''
import logging
import requests
from json import loads, dumps
from flask.ext.protorpc import message_from_json, message_to_json

from orgs import orgs
from repos import repos
from users import users
from events import events
from issues import issues
from gitdata import gitdata
from pullreqs import pullreqs


class AuthorizationError(ValueError):
  pass

class Github:
  apiurl = 'https://api.github.com'

  def __init__(self, username, password ):
    self.username = username
    self.password = password
    # api specific clients..
    self.issues = issues.Issues(self)
    self.orgs = orgs.Orgs(self)
    self.pullreqs = pullreqs.PullRequests(self)
    self.repos = repos.Repos(self)
    self.users = users.Users(self)
    self.events = events.Events(self)
    self.gitdata = gitdata.GitData(self)

  def execute(self, http_verb, path, data=None):
    verb = str.upper(http_verb)
    url = self._build_url(path)
    if verb == 'HEAD':
      return self.head(url)
    elif verb == 'GET':
      return self.get(url)
    elif verb == 'POST':
      return self.post(url, data)
    elif verb == 'PATCH':
      return self.patch(url, data)
    elif verb == 'PUT':
      return self.put(url, data)
    elif verb == 'DELETE':
      return self.delete(url)
    else:
      raise Exception(
        'Invalid httpVerb. Use: head, get, post, patch, put, delete')

  def head(self, url):
    return self._build_response(requests.head(
      self._build_url(url), auth=(self.username, self.password)))

  def get(self, url, message_type=None):
    return self._build_response(requests.get(
      self._build_url(url), auth=(self.username, self.password)),
    message_type=message_type)

  def post(self, url, data=None, message_type=None):
    return self._build_response(requests.post(self._build_url(url),
      data=self.msg_or_none(data), auth=(self.username, self.password)),
    message_type=message_type)

  def patch(self, url, data, message_type=None):
    return self._build_response(requests.patch(self._build_url(url),
      data=self.msg_or_none(data), auth=(self.username, self.password)),
    message_type=message_type)

  def put(self, url, data=None, message_type=None):
    return self._build_response(requests.put(self._build_url(url),
      data=self.msg_or_none(data), auth=(self.username, self.password)),
      message_type=message_type)

  def delete(self, url, data=None, message_type=None):
    return self._build_response(requests.post(self._build_url(url),
      data=self.msg_or_none(data), auth=(self.username, self.password)),
      message_type=message_type)

  def _build_url(self, path):
    url = Github.apiurl + (path if (path[0] is '/') else ('/%s' % path))
    print 'request url: %s' % url
    return url

  def _build_response(self, response, message_type=None):
    # check for unauthorized (401) response..
    if response.status_code == 401:
      raise AuthorizationError(response.text)
    elif response.status_code > 400:
      print 'ERROR: %d' % response.status_code
      print 'response: %s' % response.text
      print 'response: %s' % dir(response)
      print
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
      return {
        'headers': dumps(response.headers),
        'body': response.content }

  def msg_or_none(self, msg):
    if msg:
      return self.github.encode_message_to_json(msg)

  def encode_message_to_json(self, *args, **kwargs):
    return message_to_json(*args, **kwargs)

  def decode_json_to_message(self, *args, **kwargs):
    return message_from_json(*args, **kwargs)
