import urllib
from issuesevents import IssuesEvents
from issueslabels import IssuesLabels
from issuescomments import IssuesComments
from issuesmilestones import IssuesMilestones

class Issues:
  def __init__(self, client):
    self.client = client
    self.comments = IssuesComments(self.client)
    self.events = IssuesEvents(self.client)
    self.labels = IssuesLabels(self.client)
    self.milestones = IssuesMilestones(self.client)

  def list_issues(self, filter='assigned', state='open', labels=None,
      sort='created', direction='desc', since=None):
    params = {
      'filter': filter,
      'state': state,
      'labels': labels,
      'sort': sort,
      'direction': direction,
      'since': since
    }
    return self.client.get('issues?%s' % urllib.urlencode(params))

  def list_repo_issues(self, repo, milestone=None, assignee=None,
    mentioned=None, state='open', labels=None, sort='created', direction='desc',
    since=None, user=None):
    params = {
      'state': state,
      'assignee': assignee,
      'mentioned': mentioned,
      'labels': labels,
      'sort': sort,
      'direction': direction,
      'since': since,
      'milestone': milestone
    }
    return self.client.get('repos/%s/%s/issues?%s' % (
      self.client.username(user), repo, urllib.urlencode(params)))

  def get_issue(self, repo, number, user=None):
    return self.client.get(
      'repos/%s/%s/issues/%s' % (
        self.client.username(user), repo, number))

  def create_issue(self, repo, title, body=None, assignee=None,
      milestone=None, labels=None, user=None):
    msg = {
      'title': title,
      'body': body,
      'assignee': assignee,
      'milestone': milestone,
      'labels': labels
    }
    return self.client.post('repos/%s/%s/issues' % (
      self.client.username(user), repo), msg)

  def edit_issue(self, repo, id, title=None, body=None, assignee=None,
      state=None, milestone=None, labels=None, user=None):
    msg = {
      'title': title,
      'body': body,
      'assignee': assignee,
      'state': state,
      'milestone': milestone,
      'labels': labels
    }
    return self.client.post(
      'repos/%s/%s/issues/%s' % (
        self.client.username(user), repo, id), msg)
