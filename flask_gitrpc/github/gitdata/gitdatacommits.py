from ..messages import User
from ..messages import RepoCommit
from ..requests import GitDataCommitResponse
from ..requests import GitDataCommitListResponse

class GitDataCommits:
  def __init__(self, client):
    self.client = client

  def get_commit(self, repo, sha, user=None):
    return self.client.get(
      'repos/%s/%s/git/commits/%s' % (
        self.client.username(user), repo, sha), GitDataCommitListResponse)

  def create_commit(self, repo, message, tree, parents, author_name=None,
    author_email=None, author_date=None, committer_name=None,
    committer_email=None, commiter_date=None, user=None):
    msg = RepoCommit(
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
    return self.client.post(
      'repos/%s/%s/git/commits' % (
        self.client.username(user), repo), msg, GitDataCommitResponse)
