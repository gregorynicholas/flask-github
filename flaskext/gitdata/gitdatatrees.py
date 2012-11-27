from ..messages import TreeRequest
from ..messages import TreeResponse as Response

class GitDataTrees:
  def __init__(self, github):
    self.github = github

  def get_tree(self, repo, sha, recursive=False, user=None):
    url = 'repos/%s/%s/git/trees/%s' % (self.username(user), repo, sha)
    if recursive:
      url += '?recursive=1'
    return self.github.get(url, Response)

  def create_tree(self, repo, tree, base_tree=None, user=None):
    msg = TreeRequest()
    msg.base_tree = base_tree
    msg.tree = tree
    return self.github.post(
      'repos/%s/%s/git/trees' % (self.username(user), repo), msg, Response)

  def username(self, user):
    return self.github.username if user is None else user
