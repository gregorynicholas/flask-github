from ..messages import UsersResponse
from ..messages import ReposResponse

class ReposStarring:
  def __init__(self, github):
    self.github = github

  def list_stargazers(self, repo, user=None, page=1):
    return self.github.get(
      'repos/%s/%s/stargazers' % (self.username(user), repo), UsersResponse)

  def list_starred_repos(self, user=None, page=1):
    url = 'user/starred'
    if user is not None and user != self.github.username:
      url = 'users/%s/starred' % user
    return self.github.get(url, ReposResponse)

  def check_if_starring(self, repo, user=None):
    return self.github.get(
      'user/starred/%s/%s' % (self.username(user), repo))

  def star_repo(self, repo, user=None):
    return self.github.put(
      'user/starred/%s/%s' % (self.username(user), repo))

  def stop_starring(self, repo, user=None):
    return self.github.delete(
      'user/starred/%s/%s' % (self.username(user), repo))

  def username(self, user):
    return self.github.username if user is None else user
