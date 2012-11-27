from ..messages import UsersResponse
from ..messages import ReposResponse

class ReposWatching:
  def __init__(self, github):
    self.github = github

  def list_watchers(self, repo, user=None, page=1):
    return self.github.get(
      'repos/%s/%s/subscribers' % (self.username(user), repo), UsersResponse)

  def list_watched_repos(self, user=None, page=1):
    url = 'user/subscriptions'
    if user is not None and user != self.github.username:
      url = 'users/%s/subscriptions' % user
    return self.github.get(url, ReposResponse)

  def check_if_watching(self, repo, user=None):
    return self.github.get(
      'user/subscriptions/%s/%s' % (self.username(user), repo))

  def watch_repo(self, repo, user=None):
    return self.github.put(
      'user/subscriptions/%s/%s' % (self.username(user), repo))

  def stop_watching(self, repo, user=None):
    return self.github.delete(
      'user/subscriptions/%s/%s' % (self.username(user), repo))

  def username(self, user):
    return self.github.username if user is None else user
