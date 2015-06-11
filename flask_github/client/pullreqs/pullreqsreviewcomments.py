from __future__ import unicode_literals
from ..messages import PullReviewComment
from ..requests import PullReviewCommentResponse
from ..requests import PullReviewCommentListResponse

class PullReviewComments:
  def __init__(self, client):
    self.client = client

  def list(self, repo, id, user=None):
    return self.client.get(
      'repos/%s/%s/pulls/%s/comments' % (
        self.client.user(user), repo, id),
      msg_type=PullReviewCommentListResponse)

  def get(self, repo, id, user=None):
    return self.client.get(
      'repos/%s/%s/pulls/comments/%s' % (
        self.client.user(user), repo, id), msg_type=PullReviewCommentResponse)

  def create(self, repo, id, body, commit_id, path, position, user=None):
    msg = PullReviewComment(
      body=body,
      commit_id=commit_id,
      path=path,
      position=position)
    return self._create(repo=repo, id=id, msg=msg, user=user)

  def _create(self, repo, id, msg, user=None):
    return self.client.post(
      'repos/%s/%s/pulls/%s/comments' % (
        self.client.user(user), repo, id), data=msg,
      msg_type=PullReviewCommentResponse)

  def create_response(self, repo, id, body, in_reply_to, user=None):
    msg = PullReviewComment(
      body=body,
      in_reply_to=in_reply_to)
    return self._edit(repo=repo, id=id, msg=msg, user=user,
      msg_type=PullReviewCommentResponse)

  def edit(self, repo, id, body, user=None):
    msg = PullReviewComment(
      body=body)
    return self._edit(repo=repo, id=id, msg=msg, user=user)

  def _edit(self, repo, id, msg, user=None):
    return self.client.patch(
      'repos/%s/%s/pulls/comments/%s' % (
        self.client.user(user), repo, id), data=msg)

  def delete(self, repo, id, user=None):
    return self.client.delete(
      'repos/%s/%s/pulls/comments/%s' % (
        self.client.user(user), repo, id))
