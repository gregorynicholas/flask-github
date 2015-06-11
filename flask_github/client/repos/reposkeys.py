from __future__ import unicode_literals
from ..messages import Key
from ..requests import KeyResponse
from ..requests import KeyListResponse

class ReposKeys:
  def __init__(self, client):
    self.client = client

  def list(self, repo, user=None):
    return self.client.get(
      'repos/%s/%s/keys' % (
        self.client.user(user), repo), msg_type=KeyListResponse)

  def get(self, repo, id, user=None):
    return self.client.get(
      'repos/%s/%s/keys/%s' % (
        self.client.user(user), repo, id), msg_type=KeyResponse)

  def create(self, repo, title, key, user=None):
    msg = Key(
      title=title,
      key=key)
    return self._create(repo=repo, msg=msg, user=user)

  def _create(self, repo, msg, user=None):
    return self.client.post(
      'repos/%s/%s/keys' % (
        self.client.user(user), repo), data=msg, msg_type=KeyResponse)

  def edit(self, repo, id, title=None, key=None, user=None):
    msg = Key(
      title=title,
      key=key)
    return self.client.patch(
      'repos/%s/%s/keys/%s' % (
        self.client.user(user), repo, id), data=msg)

  def _edit(self, repo, msg, user=None):
    return self.client.patch(
      'repos/%s/%s/keys/%s' % (
        self.client.user(user), repo, msg.id), data=msg)

  def delete(self, repo, id, user=None):
    return self.client.delete(
      'repos/%s/%s/keys/%s' % (
        self.client.user(user), repo, id))
