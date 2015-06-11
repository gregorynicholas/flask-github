from __future__ import unicode_literals
from orgteams import OrgTeams
from orgmembers import OrgMembers
from ..messages import Org
from ..requests import UserResponse
from ..requests import OrgListResponse

class Orgs:
  def __init__(self, client):
    self.client = client
    self.teams = OrgTeams(self.client)
    self.members = OrgMembers(self.client)

  def list(self, user=None):
    url = 'user/orgs'
    if user and user != self.client._username:
      url = 'users/%s/orgs' % self.client.user(user)
    return self.client.get(url, msg_type=OrgListResponse)

  def get(self, org):
    return self.client.get('orgs/%s' % org, msg_type=UserResponse)

  def edit(self, org, billing_email=None, company=None, email=None,
      location=None, name=None):
    msg = Org(
      billing_email=billing_email,
      company=company,
      email=email,
      location=location,
      name=name)
    return self._edit(org=org, msg=msg)

  def _edit(self, org, msg):
    return self.client.patch('org/%s' % org, data=msg)
