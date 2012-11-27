from ..messages import GitDataReference

class GitDataReferences:
  def __init__(self, github):
    self.github = github

  def get_reference(self, repo, ref, user=None):
    return self.github.get(
      'repos/%s/%s/git/refs/%s' % (self.username(user), repo, ref))

  def get_references(self, repo, subnamespace=None, user=None):
    url = 'repos/%s/%s/git/refs' % (repo, self.username(user))
    if subnamespace:
      if subnamespace[0] == '/':
        url += subnamespace
      else:
        url += subnamespace
    return self.github.get(url)

  def createReference(self, repo, ref, sha, user=None):
    msg = GitDataReference()
    msg.ref = ref
    msg.sha = sha
    return self.github.post(
      'repos/%s/%s/git/refs' % (self.username(user), repo), msg)

  def editReference(self, repo, sha, force=False, user=None):
    msg = GitDataReference()
    msg.force = force
    msg.sha = sha
    return self.github.patch(
      'repos/%s/%s/git/refs' % (self.username(user), repo), msg)
