from json import dumps

class UsersEmails:
  def __init__(self, client):
    self.client = client

  def list_emails(self):
    return self.client.get(
      'user/emails', message_type=None)

  def add_emails(self, emails):
    return self.client.post(
      'user/emails', data=dumps(emails))

  def delete_email(self, emails):
    return self.client.delete(
      'user/emails', data=dumps(emails))
