from ..messages import GitDataReference
from ..requests import GitDataReferenceResponse
from ..requests import GitDataReferenceListResponse

class GitDataReferences:
  def __init__(self, client):
    self.client = client

  def get_reference(self, repo, ref, user=None):
    return self.client.get(
      'repos/%s/%s/git/refs/%s' % (
        self.client.user(user), repo, ref), msg_type=GitDataReferenceResponse)

  def get_references(self, repo, subnamespace=None, user=None):
    url = 'repos/%s/%s/git/refs' % (repo, self.client.user(user))
    if subnamespace:
      if subnamespace[0] == '/':
        url += subnamespace
      else:
        url += subnamespace
    return self.client.get(url, msg_type=GitDataReferenceListResponse)

  def create_reference(self, repo, ref, sha, user=None):
    msg = GitDataReference(
      ref=ref,
      sha=sha)
    return self.client.post(
      'repos/%s/%s/git/refs' % (
        self.client.user(user), repo), msg)

  def edit_reference(self, repo, sha, force=False, user=None):
    msg = GitDataReference(
      force=force,
      sha=sha)
    return self.client.patch(
      'repos/%s/%s/git/refs' % (
        self.client.user(user), repo), msg)
