from __future__ import unicode_literals
from ..messages import IssueLabel
from ..requests import IssueLabelResponse
from ..requests import IssueLabelListResponse

class IssuesLabels:
  def __init__(self, client):
    self.client = client

  def list_repo_labels(self, repo, user=None):
    return self.client.get('repos/%s/%s/labels' % (
      repo, self.client.user(user)), msg_type=IssueLabelListResponse)

  def get(self, repo, id, user=None):
    return self.client.get('repos/%s/%s/labels/%s' % (
      repo, self.client.user(user), id), msg_type=IssueLabelResponse)

  def create(self, repo, name, color, user=None):
    msg = IssueLabel(
      name=name,
      color=color)
    return self._create(repo=repo, msg=msg, user=user)

  def _create(self, repo, msg, user=None):
    return self.client.post('repos/%s/%s/labels' % (
      repo, self.client.user(user)), data=msg, msg_type=IssueLabelResponse)

  def edit(self, repo, id, name, color, user=None):
    msg = IssueLabel(
      name=name,
      color=color)
    return self.client.patch('repos/%s/%s/labels/%s' % (
      repo, self.client.user(user), id), data=msg)

  def delete(self, repo, id, user=None):
    return self.client.delete('repos/%s/%s/labels/%s' % (
      repo, self.client.user(user), id))

  #

  def list_issue_labels(self, repo, id, user=None):
    return self.client.get('repos/%s/%s/issues/%s/labels' % (
      repo, self.client.user(user), id), msg_type=IssueLabelListResponse)

  def add_issue_label(self, repo, id, labels, user=None):
    msg = labels
    return self.client.post('repos/%s/%s/issues/%s/labels' % (
      repo, self.client.user(user), id), data=msg)

  def delete_issue_label(self, repo, issue_id, label_id, user=None):
    return self.client.delete(url = 'repos/%s/%s/issues/%s/labels/%s' % (
      repo, self.client.user(user), issue_id, label_id))

  def replace_issue_labels(self, repo, id, labels, user=None):
    msg = labels
    return self.client.put('repos/%s/%s/issues/%s/labels' % (
      repo, self.client.user(user), id), data=msg)

  def remove_issue_labels(self, repo, id, user=None):
    return self.client.delete('repos/%s/%s/issues/%s/labels' % (
      repo, self.client.user(user), id))

  def list_issue_milestone_labels(self, repo, id, user=None):
    return self.client.get('repos/%s/%s/milestones/%s/labels' % (
      repo, self.client.user(user), id), msg_type=IssueLabelListResponse)
