from __future__ import unicode_literals
from ..messages import Gist
from ..requests import GistResponse
from ..requests import GistListResponse

class Gists:
  def __init__(self, client):
    self.client = client

  def list(self, user=None):
    url = 'users/%s/gists' % user if user else 'gists'
    return self.client.get(url, msg_type=GistListResponse)

  def list_public(self):
    return self.client.get('gists/public', msg_type=GistListResponse)

  def list_starred(self):
    return self.client.get('gists/starred', msg_type=GistListResponse)

  def get(self, id):
    return self.client.get('gists/%s' % id, msg_type=GistResponse)

  def create(self, public, files, description=None):
    msg = Gist(
      description=description,
      public=public,
      files=files)
    return self.client.post('gists', data=msg)

  def edit(self, id, files=None, description=None):
    msg = Gist(
      description=description,
      files=files)
    return self.client.patch('gists/%s' % id, data=msg)

  def star(self, id):
    return self.client.put('gists/%s/star' % id)

  def unstar(self, id):
    return self.client.delete('gists/%s/star' % id)

  def is_starred(self, id):
    return self.client.get('gists/%s/star' % id)

  def fork(self, id):
    return self.client.post('gists/%s/fork' % id)

  def delete(self, id):
    return self.client.delete('gists/%s' % id)
