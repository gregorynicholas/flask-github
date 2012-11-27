import urllib
from ..requests import RepoListResponse

class ReposForks:
  def __init__(self, client):
    self.client = client

  def list_forks(self, repo, sort=None, user=None):
    url = 'repos/%s/%s/forks' % (
      self.client.username(user), repo)
    if sort:
      url += '?%s' % urllib.urlencode({'sort': sort})
    return self.client.get(url, RepoListResponse)

  def create_fork(self, repo, org=None, user=None):
    url = 'repos/%s/%s/forks' % (
      self.client.username(user), repo)
    if org:
      url += '?%s' % urllib.urlencode({'org': org})
    return self.client.post(url)
