from __future__ import unicode_literals
from ..messages import User
from ..messages import Commit
from ..requests import GitDataCommitResponse
from ..requests import GitDataCommitListResponse

class GitDataCommits:
  def __init__(self, client):
    self.client = client

  def get(self, repo, sha, user=None):
    return self.client.get(
      'repos/%s/%s/git/commits/%s' % (
        self.client.user(user), repo, sha), msg_type=GitDataCommitListResponse)

  def create(self, repo, message, tree, parents, author_name=None,
      author_email=None, author_date=None, committer_name=None,
      committer_email=None, commiter_date=None, user=None):
    msg = Commit(
      message=message,
      parents=parents,
      tree=tree,
      author=User(
        name=author_name,
        email=author_email,
        date=author_date),
      committer = User(
        name=committer_name,
        email=committer_email,
        date=commiter_date))
    return self._create(repo=repo, msg=msg, user=user)

  def _create(self, repo, msg, user=None):
    return self.client.post(
      'repos/%s/%s/git/commits' % (
        self.client.user(user), repo), data=msg, msg_type=GitDataCommitResponse)
