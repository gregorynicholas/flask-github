import urllib

class ReposForks:
  def __init__(self, github):
    self.github = github

  def list_forks(self, repo, sort=None, user=None):
    url = 'repos/%s/%s/forks' % (self.username(user), repo)
    if sort:
      url += '?%s' % urllib.urlencode({'sort': sort})
    return self.github.get(url)

  def create_fork(self, repo, org=None, user=None):
    url = 'repos/%s/%s/forks' % (self.username(user), repo)
    if org:
      url += '?%s' % urllib.urlencode({'org': org})
    return self.github.post(url)
