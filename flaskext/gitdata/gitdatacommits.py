from ..messages import User
from ..messages import RepoCommit
from ..messages import GitDataCommitsResponse as Response

class GitDataCommits:
  def __init__(self, github):
    self.github = github

  def get_commit(self, repo, sha, user=None):
    return self.github.get(
      'repos/%s/%s/git/commits/%s' % (
        self.username(user), repo, sha), Response)

  def create_commit(self, repo, message, tree, parents, author_name=None,
    author_email=None, author_date=None, committer_name=None,
    committer_email=None, commiter_date=None, user=None):
    msg = RepoCommit()
    msg.author = User()
    msg.author.name = author_name
    msg.author.email = author_email
    msg.author.date = author_date
    msg.committer = User()
    msg.committer.name = committer_name
    msg.committer.email = committer_email
    msg.committer.date = commiter_date
    msg.message = message
    msg.parents = parents
    msg.tree = tree
    return self.github.post(
      'repos/%s/%s/git/commits' % (self.username(user), repo), msg, Response)

  def username(self, user):
    return self.github.username if user is None else user
