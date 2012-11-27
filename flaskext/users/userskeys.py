from ..messages import Key
from ..messages import KeyListRequest


class UsersKeys:
  def __init__(self, github):
    self.github = github

  def list_public_keys(self):
    return self.github.get('user/keys', KeyListRequest)

  def get_public_key(self, id):
    return self.github.get('user/keys/%s' % id, Key)

  def create_public_key(self, title, key):
    msg = Key(
      title=title,
      key=key)
    return self.github.post('user/keys', msg)

  def update_public_key(self, id, title, key):
    msg = Key(
      title=title,
      key=key)
    return self.github.patch('user/keys/%s' % id, msg)

  def delete_public_key(self, id):
    return self.github.delete('user/keys/%s' % id)

  def username(self, user):
    return self.github.username if user is None else user
