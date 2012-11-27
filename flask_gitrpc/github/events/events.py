
class Events:
  def __init__(self, client):
    # TODO: Research http://developer.github.com/v3/events/types/
    self.client = client

  def list_public_events(self):
    return self.client.get('events')

  def list_repo_events(self, repo, user=None):
    return self.client.get(
      'repos/%s/%s/events' % (
        self.client.username(user), repo))

  def list_repo_issue_events(self, repo, user=None):
    return self.client.get(
      'repos/%s/%s/issues/events' % (
        self.client.username(user), repo))

  def list_repo_network_public_events(self, repo, user=None):
    return self.client.get(
      'network/%s/%s/events' % (
        self.client.username(user), repo))

  def list_org_public_events(self, org):
    return self.client.get('orgs/%s/events' % org)

  def list_received_events(self, user=None):
    return self.client.get(
      'users/%s/received_events' % self.client.username(user))

  def list_received_public_events(self, user=None):
    return self.client.get(
      'users/%s/received_events/public' % self.client.username(user))

  def list_org_events(self, org):
    return self.client.get(
      'users/%s/events/orgs/%s' % (org))
