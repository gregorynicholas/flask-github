from __future__ import unicode_literals
from ..messages import Ref
from ..requests import RefResponse
from ..requests import RefListResponse

class GitDataRefs:
  def __init__(self, client):
    self.client = client

  def list(self, repo, subnamespace=None, user=None):
    url = 'repos/%s/%s/git/refs' % (repo, self.client.user(user))
    if subnamespace:
      if subnamespace[0] == '/':
        url += subnamespace
      else:
        url += subnamespace
    return self.client.get(url, msg_type=RefListResponse)

  def get(self, repo, ref, user=None):
    return self.client.get(
      'repos/%s/%s/git/refs/%s' % (
        self.client.user(user), repo, ref), msg_type=RefResponse)

  def create(self, repo, ref, sha, user=None):
    msg = Ref(
      ref=ref,
      sha=sha)
    return self._create(repo=repo, msg=msg, user=user)

  def _create(self, repo, msg, user=None):
    return self.client.post(
      'repos/%s/%s/git/refs' % (
        self.client.user(user), repo), data=msg, msg_type=RefResponse)

  def edit(self, repo, sha, force=False, user=None):
    msg = Ref(
      force=force,
      sha=sha)
    return self._edit(repo=repo, msg=msg, user=user)

  def _edit(self, repo, msg, user=None):
    return self.client.patch(
      'repos/%s/%s/git/refs' % (
        self.client.user(user), repo), data=msg, msg_type=RefResponse)
