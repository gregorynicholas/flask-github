from ..messages import Team

class OrgTeams:
  def __init__(self, github):
    self.github = github

  def list_teams(self, org):
    return self.github.get('orgs/%s/teams' % org)

  def get_team(self, id):
    return self.github.get('teams/%s' % id)

  def create_team(self, org, name, repo_names=None, permission=None):
    msg = Team()
    msg.name = name
    msg.repo_names = repo_names
    msg.permission = permission
    return self.github.post('orgs/%s/teams' % org, msg)

  def edit_team(self, id, name, permission=None):
    msg = Team()
    msg.name = name
    msg.permission = permission
    return self.github.patch('teams/%s' % id, msg)

  def delete_team(self, id):
    return self.github.delete(
      'teams/%s' % id)

  def list_team_members(self, id):
    return self.github.get(
      'teams/%s/members' % id)

  def get_team_member(self, id, user=None):
    return self.github.get(
      'teams/%s/members/%s' % (id, self.username(user)))

  def add_team_member(self, id, user):
    return self.github.put(
      'teams/%s/members/%s' % (id, self.username(user)))

  def delete_team_member(self, id, user):
    return self.github.delete(
      'teams/%s/members/%s' % (id, self.username(user)))

  def list_team_repos(self, id):
    return self.github.get(
      'teams/%s/repos' % id)

  def get_team_repo(self, id, user, repo):
    return self.github.get(
      'teams/%s/repos/%s/%s' % (id, self.username(user), repo))

  def add_team_repo(self, id, user, repo):
    return self.github.put(
      'teams/%s/repos/%s/%s' % (id, self.username(user), repo))

  def remove_team_repo(self, id, user, repo):
    return self.github.delete(
      'teams/%s/repos/%s/%s' % (id, self.username(user), repo))

  def username(self, user):
    return self.github.username if user is None else user
