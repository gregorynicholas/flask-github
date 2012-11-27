from ..messages import PullReviewComment

class PullReviewComments:
  def __init__(self, github):
    self.github = github

  def list_comments(self, repo, id, user=None):
    return self.github.get(
      'repos/%s/%s/pulls/%s/comments' % (self.username(user), repo, id))

  def get_comment(self, repo, id, user=None):
    return self.github.get(
      'repos/%s/%s/pulls/comments/%s' % (self.username(user), repo, id))

  def create_comment(self, repo, id, body, commit_id, path, position,
      user=None):
    msg = PullReviewComment()
    msg.body = body
    msg.commit_id = commit_id
    msg.path = path
    msg.position = position
    return self.github.post(
      'repos/%s/%s/pulls/%s/comments' % (self.username(user), repo, id), msg)

  def create_commentResponse(self, repo, id, body, in_reply_to, user=None):
    msg = PullReviewComment()
    msg.body = body
    msg.in_reply_to = in_reply_to
    return self.github.post(
      'repos/%s/%s/pulls/%s/comments' % (self.username(user), repo, id), msg)

  def edit_comment(self, repo, id, body, user=None):
    msg = PullReviewComment()
    msg.body = body
    return self.github.patch(
      'repos/%s/%s/pulls/comments/%s' % (self.username(user), repo, id), msg)

  def delete_comment(self, repo, id, user=None):
    return self.github.delete(
      'repos/%s/%s/pulls/comments/%s' % (self.username(user), repo, id))

  def username(self, user):
    return self.github.username if user is None else user
