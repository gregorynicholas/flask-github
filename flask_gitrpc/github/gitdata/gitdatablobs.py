from ..messages import Blob
from ..requests import GitDataBlobResponse

class GitDataBlobs:
  def __init__(self, client):
    self.client = client

  def get_blob(self, repo, sha, user=None):
    return self.client.get(
      'repos/%s/%s/git/blobs/%s' % (
        self.client.user(user), repo, sha), msg_type=GitDataBlobResponse)

  def create_blob(self, repo, content, encoding, user=None):
    msg = Blob(
      content=content,
      encoding=encoding)
    return self.client.post(
      'repos/%s/%s/git/blobs' % (
        self.client.user(user), repo), data=msg, msg_type=GitDataBlobResponse)
