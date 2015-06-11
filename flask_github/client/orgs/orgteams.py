from __future__ import unicode_literals
from ..messages import Team
from ..requests import TeamResponse
from ..requests import TeamListResponse
from ..requests import RepoResponse
from ..requests import RepoListResponse
from ..requests import UserResponse
from ..requests import UserListResponse

class OrgTeams:
  def __init__(self, client):
    self.client = client

  def list(self, org):
    return self.client.get('orgs/%s/teams' % org, msg_type=TeamListResponse)

  def get(self, id):
    return self.client.get('teams/%s' % id, msg_type=TeamResponse)

  def create(self, org, name, repo_names=None, permission=None):
    msg = Team(
      name=name,
      repo_names=repo_names,
      permission=permission)
    return self._create(org=org, msg=msg)

  def _create(self, org, msg):
    return self.client.post('orgs/%s/teams' % org, data=msg)

  def edit(self, id, name, permission=None):
    msg = Team(
      name=name,
      permission=permission)
    return self._edit(id=id, msg=msg)

  def _edit(self, id, msg):
    return self.client.patch('teams/%s' % id, data=msg)

  def delete(self, id):
    return self.client.delete(
      'teams/%s' % id)

  # members..

  def list_members(self, id):
    return self.client.get(
      'teams/%s/members' % id, msg_type=UserListResponse)

  def get_member(self, id, user=None):
    return self.client.get(
      'teams/%s/members/%s' % (
        id, self.client.user(user)), msg_type=UserResponse)

  def add_member(self, id, user):
    return self.client.put(
      'teams/%s/members/%s' % (id, self.client.user(user)))

  def delete_member(self, id, user):
    return self.client.delete(
      'teams/%s/members/%s' % (id, self.client.user(user)))

  # repos..

  def list_repos(self, id):
    return self.client.get(
      'teams/%s/repos' % id, msg_type=RepoListResponse)

  def get_repo(self, id, user, repo):
    return self.client.get(
      'teams/%s/repos/%s/%s' % (
        id, self.client.user(user), repo), msg_type=RepoResponse)

  def add_repo(self, id, user, repo):
    return self.client.put(
      'teams/%s/repos/%s/%s' % (id, self.client.user(user), repo))

  def remove_repo(self, id, user, repo):
    return self.client.delete(
      'teams/%s/repos/%s/%s' % (id, self.client.user(user), repo))
