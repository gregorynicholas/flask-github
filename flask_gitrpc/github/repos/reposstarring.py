from ..requests import UserListResponse
from ..requests import RepoListResponse

class ReposStarring:
  def __init__(self, client):
    self.client = client

  def list_stargazers(self, repo, user=None, page=1):
    return self.client.get(
      'repos/%s/%s/stargazers' % (
        self.client.username(user), repo), UserListResponse)

  def list_starred_repos(self, user=None, page=1):
    url = 'user/starred'
    if user is not None and user != self.client._username:
      url = 'users/%s/starred' % user
    return self.client.get(url, RepoListResponse)

  def check_if_starring(self, repo, user=None):
    return self.client.get(
      'user/starred/%s/%s' % (
        self.client.username(user), repo))

  def star_repo(self, repo, user=None):
    return self.client.put(
      'user/starred/%s/%s' % (
        self.client.username(user), repo))

  def stop_starring(self, repo, user=None):
    return self.client.delete(
      'user/starred/%s/%s' % (
        self.client.username(user), repo))
