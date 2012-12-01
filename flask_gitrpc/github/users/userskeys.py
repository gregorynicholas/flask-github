from ..messages import Key
from ..requests import KeyResponse
from ..requests import KeyListResponse

class UsersKeys:
  def __init__(self, client):
    self.client = client

  def list_public_keys(self):
    return self.client.get(
      'user/keys', msg_type=KeyListResponse)

  def get_public_key(self, id):
    return self.client.get(
      'user/keys/%s' % id, msg_type=KeyResponse)

  def create_public_key(self, title, key):
    msg = Key(
      title=title,
      key=key)
    return self.client.post(
      'user/keys', data=msg)

  def update_public_key(self, id, title, key):
    msg = Key(
      title=title,
      key=key)
    return self.client.patch(
      'user/keys/%s' % id, data=msg)

  def delete_public_key(self, id):
    return self.client.delete(
      'user/keys/%s' % id)
