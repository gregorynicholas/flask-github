from json import dumps

class UsersEmails:
  def __init__(self, client):
    self.client = client

  def list(self):
    return self.client.get(
      'user/emails', msg_type=None)

  def add(self, emails):
    return self.client.post(
      'user/emails', data=dumps(emails), msg_type=None)

  def delete(self, emails):
    return self.client.delete(
      'user/emails', data=dumps(emails))
