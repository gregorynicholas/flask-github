from orgmembers import OrgMembers
from orgteams import OrgTeams
from ..messages import Org

class Orgs:
  def __init__(self, github):
    self.github = github
    self.members = OrgMembers(self.github)
    self.teams = OrgTeams(self.github)

  def list_orgs(self, user=None):
    url = 'user/orgs'
    if user != self.github.username:
      url = 'users/%s/orgs' % self.username(user)
    return self.github.get(url)

  def get_org(self, org):
    return self.github.get('orgs/%s' % org)

  def edit_org(self, org, billing_email=None, company=None, email=None,
      location=None, name=None ):
    msg = Org()
    msg.billing_email = billing_email
    msg.company = company
    msg.email = email
    msg.location = location
    msg.name = name
    return self.github.patch('org/%s' % org, msg)

  def username(self, user):
    return self.github.username if user is None else user
