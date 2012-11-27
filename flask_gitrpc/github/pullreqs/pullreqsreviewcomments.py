from ..messages import PullReviewComment
from ..requests import PullReviewCommentResponse
from ..requests import PullReviewCommentListResponse

class PullReviewComments:
  def __init__(self, client):
    self.client = client

  def list_comments(self, repo, id, user=None):
    return self.client.get(
      'repos/%s/%s/pulls/%s/comments' % (
        self.client.username(user), repo, id), PullReviewCommentListResponse)

  def get_comment(self, repo, id, user=None):
    return self.client.get(
      'repos/%s/%s/pulls/comments/%s' % (
        self.client.username(user), repo, id), PullReviewCommentResponse)

  def create_comment(self, repo, id, body, commit_id, path, position,
      user=None):
    msg = PullReviewComment(
      body=body,
      commit_id=commit_id,
      path=path,
      position=position)
    return self.client.post(
      'repos/%s/%s/pulls/%s/comments' % (
        self.client.username(user), repo, id), msg)

  def create_comment_response(self, repo, id, body, in_reply_to, user=None):
    msg = PullReviewComment(
      body=body,
      in_reply_to=in_reply_to)
    return self.client.post(
      'repos/%s/%s/pulls/%s/comments' % (
        self.client.username(user), repo, id), msg)

  def edit_comment(self, repo, id, body, user=None):
    msg = PullReviewComment(
      body=body)
    return self.client.patch(
      'repos/%s/%s/pulls/comments/%s' % (
        self.client.username(user), repo, id), msg)

  def delete_comment(self, repo, id, user=None):
    return self.client.delete(
      'repos/%s/%s/pulls/comments/%s' % (
        self.client.username(user), repo, id))
