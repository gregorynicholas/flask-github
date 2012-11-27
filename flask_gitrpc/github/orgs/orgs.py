from ..messages import Org
from orgteams import OrgTeams
from orgmembers import OrgMembers

class Orgs:
  def __init__(self, client):
    self.client = client
    self.members = OrgMembers(self.client)
    self.teams = OrgTeams(self.client)

  def list_orgs(self, user=None):
    url = 'user/orgs'
    if user != self.client._username:
      url = 'users/%s/orgs' % self.client.username(user)
    return self.client.get(url)

  def get_org(self, org):
    return self.client.get('orgs/%s' % org)

  def edit_org(self, org, billing_email=None, company=None, email=None,
      location=None, name=None):
    msg = Org(
      billing_email=billing_email,
      company=company,
      email=email,
      location=location,
      name=name)
    return self.client.patch('org/%s' % org, msg)
