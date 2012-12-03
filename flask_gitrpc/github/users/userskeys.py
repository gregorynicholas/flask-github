from ..messages import Key
from ..requests import KeyResponse
from ..requests import KeyListResponse

class UsersKeys:
  def __init__(self, client):
    self.client = client

  def list(self):
    return self.client.get(
      'user/keys', msg_type=KeyListResponse)

  def get(self, id):
    return self.client.get(
      'user/keys/%s' % id, msg_type=KeyResponse)

  def create(self, title, key):
    msg = Key(
      title=title,
      key=key)
    return self._create(msg=msg)

  def _create(self, msg):
    return self.client.post(
      'user/keys', data=msg, msg_type=KeyResponse)

  def edit(self, id, title, key):
    msg = Key(
      title=title,
      key=key)
    return self._edit(msg=msg)

  def _edit(self, msg):
    return self.client.patch(
      'user/keys/%s' % id, data=msg)

  def delete(self, id):
    return self.client.delete(
      'user/keys/%s' % id)
