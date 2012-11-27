
class IssuesEvents:
  def __init__(self, client):
    self.client = client

  def list_issue_events(self, repo, issue_id, user=None):
    return self.client.get('repos/%s/%s/issues/%s/events' % (
      self.client.username(user), repo, issue_id))

  def list_repo_issue_events(self, repo, user=None):
    return self.client.get('repos/%s/%s/issues/events' % (
      self.client.username(user), repo))

  def get_event(self, repo, id, user=None):
    return self.client.get('repos/%s/%s/issues/events/%s' % (
      self.client.username(user), repo, id))
