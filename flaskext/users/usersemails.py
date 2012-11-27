from json import dumps

class UsersEmails:
  def __init__(self, github):
    self.github = github

  def list_emails(self):
    return self.github.get(
      'user/emails')

  def add_emails(self, emails):
    return self.github.post(
      'user/emails', dumps(emails))

  def delete_email(self, emails):
    return self.github.delete(
      'user/emails', dumps(emails))

  def username(self, user):
    return self.github.username if user is None else user
