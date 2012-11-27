class Events:
  def __init__(self, github):
    # TODO: Research http://developer.github.com/v3/events/types/
    self.github = github

  def listPublicEvents(self):
    return self.github.get('events')

  def listRepoEvents(self, repo, user=None):
    return self.github.get(
      'repos/%s/%s/events' % (self.username(user), repo))

  def listRepoIssueEvents(self, repo, user=None):
    return self.github.get(
      'repos/%s/%s/issues/events' % (self.username(user), repo))

  def listRepoNetworkPublicEvents(self, repo, user=None):
    return self.github.get(
      'network/%s/%s/events' % (self.username(user), repo))

  def listOrgPublicEvents(self, org):
    return self.github.get('orgs/%s/events' % org)

  def listReceivedEvents(self, user=None):
    return self.github.get(
      'users/%s/received_events' % self.username(user))

  def listReceivedPublicEvents(self, user=None):
    return self.github.get(
      'users/%s/received_events/public' % self.username(user))

  def listOrgEvents(self, org):
    return self.github.get(
      'users/%s/events/orgs/%s' % (self.username(user), org))

  def username(self, user):
    return self.github.username if user is None else user
