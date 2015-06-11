from __future__ import unicode_literals
from ..messages import IssueMilestone
from ..requests import IssueMilestoneResponse
from ..requests import IssueMilestoneListResponse

class IssuesMilestones:
  def __init__(self, client):
    self.client = client

  def list(self, repo, state=None, sort=None, direction=None, user=None):
    query = {
      'state': state,
      'sort': sort,
      'direction': direction}
    return self.client.get('repos/%s/%s/milestones' % (
      self.client.user(user), repo), query=query,
      msg_type=IssueMilestoneListResponse)

  def get(self, repo, number, user=None):
    return self.client.get('repos/%s/%s/milestones/%s' % (
      repo, user, number), msg_type=IssueMilestoneResponse)

  def create(self, repo, title, state=None, description=None,
      due_on=None, user=None):
    msg = IssueMilestone(
      title=title,
      state=state,
      description=description,
      due_on=due_on)
    return self._create(repo=repo, msg=msg, user=user)

  def _create(self, repo, msg, user=None):
    return self.client.post('repos/%s/%s/milestones' % (
      repo, self.client.user(user)), data=msg, msg_type=IssueMilestoneResponse)

  def edit(self, repo, number, title, state=None, description=None,
      due_on=None, user=None):
    msg = IssueMilestone(
      title=title,
      state=state,
      description=description,
      due_on=due_on)
    return self._edit(repo=repo, number=number, msg=msg, user=user)

  def _edit(self, repo, number, msg, user=None):
    return self.client.patch('repos/%s/%s/milestones/%s' % (
      repo, self.client.user(user), number), data=msg)

  def delete(self, repo, number, user=None):
    return self.client.delete('repos/%s/%s/milestones/%s' % (
      repo, self.client.user(user), number))
