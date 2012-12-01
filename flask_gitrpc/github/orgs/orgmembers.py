from ..requests import UserResponse
from ..requests import UserListResponse

class OrgMembers:
  def __init__(self, client):
    self.client = client

  def list_members(self, org):
    return self.client.get(
      'orgs/%s/members' % org, msg_type=UserListResponse)

  def get_member(self, org, user=None):
    return self.client.get(
      'orgs/%s/members/%s' % (
        org, self.client.user(user)), msg_type=UserResponse)

  def remove_member(self, org, user):
    return self.client.delete(
      'orgs/%s/members/%s' % (org, self.client.user(user)))

  def list_public_members(self, org):
    return self.client.get(
      'orgs/%s/public_members' % org, msg_type=UserListResponse)

  def get_if_user_is_public(self, org, user):
    return self.client.get(
      'orgs/%s/public_members/%s' % (
        org, self.client.user(user)), msg_type=UserResponse)

  def publicize_user(self, org, user):
    return self.client.put(
      'orgs/%s/public_members/%s' % (org, self.client.user(user)))

  def conceal_user(self, org, user):
    return self.client.delete(
      'orgs/%s/public_members/%s' % (org, self.client.user(user)))
