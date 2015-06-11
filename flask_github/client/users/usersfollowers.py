from __future__ import unicode_literals
from ..requests import UserListResponse

class UsersFollowers:
  def __init__(self, client):
    self.client = client

  def list_followers(self, user=None):
    url = 'users/%s/followers' % user if (
      user is not None and user != self.client._username) else 'user/followers'
    return self.client.get(url, msg_type=UserListResponse)

  def list_following(self, user=None):
    url = 'users/%s/following' % user if (
      user is not None and user != self.client._username) else 'user/following'
    return self.client.get(url, msg_type=UserListResponse)

  def is_following(self, user):
    return self.client.get(
      'user/following/%s' % user)

  def follow(self, user):
    return self.client.put(
      'user/following/%s' % user)

  def unfollow(self, user):
    return self.client.delete(
      'user/following/%s' % user)
