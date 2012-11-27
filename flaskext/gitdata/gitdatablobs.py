from ..messages import Blob
from ..messages import BlobResponse as Response

class GitDataBlobs:
  def __init__(self, github):
    self.github = github

  def get_blob(self, repo, sha, user=None):
    return self.github.get(
      'repos/%s/%s/git/blobs/%s' % (
        self.username(user), repo, sha), Response)

  def create_blob(self, repo, content, encoding, user=None):
    msg = Blob()
    msg.content = content
    msg.encoding = encoding
    return self.github.post(
      'repos/%s/%s/git/blobs' % (self.username(user), repo), msg, Response)

  def username(self, user):
    return self.github.username if user is None else user
