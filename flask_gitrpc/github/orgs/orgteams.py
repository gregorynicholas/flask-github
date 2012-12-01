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

  def list_teams(self, org):
    return self.client.get('orgs/%s/teams' % org, msg_type=TeamListResponse)

  def get_team(self, id):
    return self.client.get('teams/%s' % id, msg_type=TeamResponse)

  def create_team(self, org, name, repo_names=None, permission=None):
    msg = Team(
      name=name,
      repo_names=repo_names,
      permission=permission)
    return self.client.post('orgs/%s/teams' % org, data=msg)

  def edit_team(self, id, name, permission=None):
    msg = Team(
      name=name,
      permission=permission)
    return self.client.patch('teams/%s' % id, data=msg)

  def delete_team(self, id):
    return self.client.delete(
      'teams/%s' % id)

  def list_team_members(self, id):
    return self.client.get(
      'teams/%s/members' % id, msg_type=UserListResponse)

  def get_team_member(self, id, user=None):
    return self.client.get(
      'teams/%s/members/%s' % (
        id, self.client.user(user)), msg_type=UserResponse)

  def add_team_member(self, id, user):
    return self.client.put(
      'teams/%s/members/%s' % (id, self.client.user(user)))

  def delete_team_member(self, id, user):
    return self.client.delete(
      'teams/%s/members/%s' % (id, self.client.user(user)))

  def list_team_repos(self, id):
    return self.client.get(
      'teams/%s/repos' % id, msg_type=RepoListResponse)

  def get_team_repo(self, id, user, repo):
    return self.client.get(
      'teams/%s/repos/%s/%s' % (
        id, self.client.user(user), repo), msg_type=RepoResponse)

  def add_team_repo(self, id, user, repo):
    return self.client.put(
      'teams/%s/repos/%s/%s' % (id, self.client.user(user), repo))

  def remove_team_repo(self, id, user, repo):
    return self.client.delete(
      'teams/%s/repos/%s/%s' % (id, self.client.user(user), repo))
