from __future__ import unicode_literals
from ..messages import IssueEvent
from ..requests import IssueEventResponse
from ..requests import IssueEventListResponse

class IssuesEvents:
  def __init__(self, client):
    self.client = client

  def list(self, repo, issue_id=None, user=None):
    'repos/%s/%s/issues/events' % (self.client.user(user), repo)
    if issue_id:
      url = 'repos/%s/%s/issues/%s/events' % (
        self.client.user(user), repo, issue_id)
    return self.client.get(url, msg_type=IssueEventListResponse)

  def get(self, repo, id, user=None):
    return self.client.get('repos/%s/%s/issues/events/%s' % (
      self.client.user(user), repo, id), msg_type=IssueEventResponse)
