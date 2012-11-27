
class UsersFollowers:
  def __init__(self, github):
    self.github = github

  def listFollowers(self, user=None):
    url = 'users/%s/followers' % user if (
      user is not None and user != self.github.username) else 'user/followers'
    return self.github.get(url)

  def listFollowing(self, user=None):
    url = 'users/%s/following' % user if (
      user is not None and user != self.github.username) else 'user/following'
    return self.github.get(url)

  def checkIfFollowing(self, user):
    return self.github.get(
      'user/following/%s' % user)

  def followUser(self, user):
    return self.github.put(
      'user/following/%s' % user)

  def unfollowUser(self, user):
    return self.github.delete(
      'user/following/%s' % user)

  def username(self, user):
    return self.github.username if user is None else user
