from ..requests import UserResponse
from ..requests import UserListResponse

class OrgMembers:
  def __init__(self, client):
    self.client = client

  def list(self, org, public_only=False):
    url = 'orgs/%s/members' % org
    if public_only:
      url = 'orgs/%s/public_members' % org
    return self.client.get(url, msg_type=UserListResponse)

  def get(self, org, user=None, public_only=False):
    url = 'orgs/%s/members/%s' % (org, self.client.user(user))
    if public_only:
      url = 'orgs/%s/public_members/%s' % (
        org, self.client.user(user))
    return self.client.get(url, msg_type=UserResponse)

  def remove(self, org, user):
    return self.client.delete(
      'orgs/%s/members/%s' % (org, self.client.user(user)))

  def make_public(self, org, user):
    return self.client.put(
      'orgs/%s/public_members/%s' % (org, self.client.user(user)))

  def make_private(self, org, user):
    return self.client.delete(
      'orgs/%s/public_members/%s' % (org, self.client.user(user)))
