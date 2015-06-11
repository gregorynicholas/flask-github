from __future__ import unicode_literals
from ..requests import RepoResponse
from ..requests import RepoListResponse

class ReposForks:
  def __init__(self, client):
    self.client = client

  def list(self, repo, sort=None, user=None):
    query = None
    if sort:
      query = {'sort': sort}
    return self.client.get('repos/%s/%s/forks' % (
      self.client.user(user), repo), query=query, msg_type=RepoListResponse)

  def create(self, repo, org=None, user=None):
    query = None
    if org:
      query = {'org': org}
    return self.client.post('repos/%s/%s/forks' % (
      self.client.user(user), repo), query=query, msg_type=RepoResponse)
