from ..requests import UserListResponse
from ..requests import RepoListResponse

class ReposWatching:
  def __init__(self, client):
    self.client = client

  def list_watchers(self, repo, user=None, page=1):
    return self.client.get(
      'repos/%s/%s/subscribers' % (
        self.client.user(user), repo), msg_type=UserListResponse)

  def list_watched_repos(self, user=None, page=1):
    url = 'user/subscriptions'
    if user is not None and user != self.client._username:
      url = 'users/%s/subscriptions' % user
    return self.client.get(url, msg_type=RepoListResponse)

  def check_if_watching(self, repo, user=None):
    return self.client.get(
      'user/subscriptions/%s/%s' % (
        self.client.user(user), repo))

  def watch_repo(self, repo, user=None):
    return self.client.put(
      'user/subscriptions/%s/%s' % (
        self.client.user(user), repo))

  def stop_watching(self, repo, user=None):
    return self.client.delete(
      'user/subscriptions/%s/%s' % (
        self.client.user(user), repo))
