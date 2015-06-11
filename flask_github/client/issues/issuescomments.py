from __future__ import unicode_literals
from ..messages import IssueComment
from ..requests import IssueCommentResponse
from ..requests import IssueCommentListResponse

class IssuesComments:
  def __init__(self, client):
    self.client = client

  def list(self, repo, id, user=None):
    return self.client.get('repos/%s/%s/issues/%s/comments' % (
      self.client.user(user), repo, id), msg_type=IssueCommentListResponse)

  def get(self, repo, id, user=None):
    return self.client.get('repos/%s/%s/issues/comments/%s' % (
      self.client.user(user), repo, id), msg_type=IssueCommentResponse)

  def edit(self, repo, id, body, user=None):
    msg = IssueComment(
      body=body)
    return self.client.patch('repos/%s/%s/issues/comments/%s' % (
      self.client.user(user), repo, id), data=msg)

  def delete(self, repo, id, user=None):
    return self.client.delete('repos/%s/%s/issues/comments/%s' % (
      self.client.user(user), repo, id))
