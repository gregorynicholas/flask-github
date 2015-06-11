from __future__ import unicode_literals
from ..messages import Blob
from ..requests import BlobResponse

class GitDataBlobs:
  def __init__(self, client):
    self.client = client

  def get(self, repo, sha, user=None):
    return self.client.get(
      'repos/%s/%s/git/blobs/%s' % (
        self.client.user(user), repo, sha), msg_type=BlobResponse)

  def create(self, repo, content, encoding, user=None):
    msg = Blob(
      content=content,
      encoding=encoding)
    return self._create(repo=repo, user=user, msg=msg)

  def _create(self, repo, msg, user):
    return self.client.post(
      'repos/%s/%s/git/blobs' % (
        self.client.user(user), repo), data=msg, msg_type=BlobResponse)
