from __future__ import unicode_literals
from ..requests import UserEmailResponse
from ..requests import UserEmailListResponse

class UsersEmails:
  def __init__(self, client):
    self.client = client

  def list(self):
    return self.client.get(
      'user/emails', msg_type=UserEmailListResponse)

  def add(self, emails):
    return self.client.post(
      'user/emails', data=emails, msg_type=UserEmailResponse)

  def delete(self, emails):
    return self.client.delete(
      'user/emails', data=emails)
