from ..requests import EventListResponse

class Events:
  def __init__(self, client):
    # TODO: Research http://developer.github.com/v3/events/types/
    self.client = client

  def list_public_events(self):
    '''List public events.'''
    return self.client.get('events', msg_type=EventListResponse)

  def list_repo_events(self, repo, user=None):
    '''List repository events.'''
    return self.client.get(
      'repos/%s/%s/events' % (
        self.client.user(user), repo), msg_type=EventListResponse)

  def list_repo_issue_events(self, repo, user=None):
    '''List issue events for a repository.'''
    return self.client.get(
      'repos/%s/%s/issues/events' % (
        self.client.user(user), repo), msg_type=EventListResponse)

  def list_repo_network_public_events(self, repo, user=None):
    '''List public events for a network of repositories.'''
    return self.client.get(
      'network/%s/%s/events' % (
        self.client.user(user), repo), msg_type=EventListResponse)

  def list_user_events(self, user=None):
    '''List events performed by a user.

    If you are authenticated as the given user, you will see your private
    events. Otherwise, you’ll only see public events.'''
    return self.client.get(
      'users/%s/events' % (self.client.user(user)), msg_type=EventListResponse)

  def list_user_org_events(self, org):
    '''List a user's events for an organization.

    This is the user’s organization dashboard. You must be authenticated as the
    user to view this.'''
    return self.client.get(
      'users/%s/events/orgs/%s' % (org), msg_type=EventListResponse)

  def list_org_public_events(self, org):
    '''List public events for an organization.'''
    return self.client.get('orgs/%s/events' % org, msg_type=EventListResponse)

  def list_received_events(self, user=None):
    '''List events that a user has received.

    These are events that a user receives by watching repos and following
    users. If the user is authenticated as the given user, they will see private
    events. Otherwise, they'll only see public events.'''
    return self.client.get(
      'users/%s/received_events' % self.client.user(user), msg_type=EventListResponse)

  def list_received_public_events(self, user=None):
    '''List public events that a user has received.'''
    return self.client.get(
      'users/%s/received_events/public' % self.client.user(user), msg_type=EventListResponse)
