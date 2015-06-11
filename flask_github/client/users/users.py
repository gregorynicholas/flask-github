from __future__ import unicode_literals
from userskeys import UsersKeys
from usersemails import UsersEmails
from usersfollowers import UsersFollowers
from ..messages import User
from ..requests import UserResponse

class Users:
  def __init__(self, client):
    self.client = client
    self.keys = UsersKeys(self.client)
    self.emails = UsersEmails(self.client)
    self.followers = UsersFollowers(self.client)

  def get(self, user=None):
    url = 'user'
    if (user is not None and user != self.client._username):
      url = 'users/%s' % user
    return self.client.get(url, msg_type=UserResponse)

  def update(self, name=None, email=None, blog=None, company=None,
      location=None, hireable=False, bio=None):
    msg = User(
      name=name,
      email=email,
      blog=blog,
      company=company,
      location=location,
      hireable=hireable,
      bio=bio)
    return self._update(msg=msg)

  def _update(self, msg):
    return self.client.patch('user', data=msg)
