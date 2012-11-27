from userskeys import UsersKeys
from usersemails import UsersEmails
from usersfollowers import UsersFollowers

from ..messages import User


class Users:
  def __init__(self, github):
    self.github = github
    self.emails = UsersEmails(self.github)
    self.followers = UsersFollowers(self.github)
    self.keys = UsersKeys(self.github)

  def get_user(self, user=None):
    url = 'user'
    if (user is not None and user != self.github.username):
      url = 'users/%s' % user
    return self.github.get(url, User)

  def update_user(self, name=None, email=None, blog=None, company=None,
      location=None, hireable=False, bio=None):
    msg = User(
      name=name,
      email=email,
      blog=blog,
      company=company,
      location=location,
      hireable=hireable,
      bio=bio)
    return self.github.patch('user', msg)

  def username(self, user):
    return self.github.username if user is None else user
