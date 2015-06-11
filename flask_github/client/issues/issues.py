from __future__ import unicode_literals
from issuesevents import IssuesEvents
from issueslabels import IssuesLabels
from issuescomments import IssuesComments
from issuesmilestones import IssuesMilestones

from ..messages import Issue
from ..requests import IssueResponse
from ..requests import IssueListResponse

class Issues:
  def __init__(self, client):
    self.client = client
    self.comments = IssuesComments(self.client)
    self.events = IssuesEvents(self.client)
    self.labels = IssuesLabels(self.client)
    self.milestones = IssuesMilestones(self.client)

  def list_issues(self, filter='assigned', state='open', labels=None,
      sort='created', direction='desc', since=None):
    query = {
      'filter': filter,
      'state': state,
      'labels': labels,
      'sort': sort,
      'direction': direction,
      'since': since
    }
    return self.client.get('issues', query=query, msg_type=IssueListResponse)

  def list_repo_issues(self, repo, milestone=None, assignee=None,
    mentioned=None, state='open', labels=None, sort='created', direction='desc',
    since=None, user=None):
    query = {
      'state': state,
      'assignee': assignee,
      'mentioned': mentioned,
      'labels': labels,
      'sort': sort,
      'direction': direction,
      'since': since,
      'milestone': milestone
    }
    return self.client.get('repos/%s/%s/issues' % (
      self.client.user(user), repo), query=query, msg_type=IssueListResponse)

  def get(self, repo, number, user=None):
    return self.client.get(
      'repos/%s/%s/issues/%s' % (
        self.client.user(user), repo, number), msg_type=IssueResponse)

  def create(self, repo, title, body=None, assignee=None,
      milestone=None, labels=None, user=None):
    msg = Issue(
      title=title,
      body=body,
      assignee=assignee,
      milestone=milestone,
      labels=labels)
    return self._create(repo=repo, msg=msg, user=user)

  def _create(self, repo, msg, user=None):
    return self.client.post('repos/%s/%s/issues' % (
      self.client.user(user), repo), data=msg, msg_type=IssueResponse)

  def edit(self, repo, id, title=None, body=None, assignee=None,
      state=None, milestone=None, labels=None, user=None):
    msg = Issue(
      title=title,
      body=body,
      assignee=assignee,
      state=state,
      milestone=milestone,
      labels=labels)
    return self._edit(repo=repo, id=id, msg=msg, user=user)

  def _edit(self, repo, id, msg, user=None):
    return self.client.post(
      'repos/%s/%s/issues/%s' % (
        self.client.user(user), repo, id), data=msg)
