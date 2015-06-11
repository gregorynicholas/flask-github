from __future__ import unicode_literals
from ..messages import Commit
from ..requests import CommitResponse
from ..requests import CommitListResponse
from ..requests import CommentResponse
from ..requests import CommentListResponse

class ReposCommits:
  def __init__(self, client):
    self.client = client

  def list(self, repo, sha=None, path=None, user=None):
    query = None
    if sha and path:
      query = {'sha': sha, 'path': path}
    return self.client.get('repos/%s/%s/commits' % (
      self.client.user(user), repo), query=query, msg_type=CommitListResponse)

  def get(self, repo, sha, user=None):
    return self.client.get(
      'repos/%s/%s/commits/%s' % (
        self.client.user(user), repo, sha), msg_type=CommitResponse)

  def compare(self, repo, base, head, user=None):
    return self.client.get(
      'repos/%s/%s/compare/%s...:%s' % (
        self.client.user(user), repo, base, head), msg_type=None)

  # comments..

  def list_comments(self, repo, sha=None, user=None):
    url = 'repos/%s/%s/comments' % (
      self.client.user(user), repo)
    if sha:
      url = 'repos/%s/%s/commits/%s/comments' % (
        self.client.user(user), repo, sha)
    return self.client.get(url, msg_type=CommentListResponse)

  def create_comment(self, repo, sha, body, line, path, position, user=None):
    msg = Commit(
      body=body,
      commit_id=sha,
      line=line,
      path=path,
      position=position)
    return self._create_comment(repo=repo, sha=sha, msg=msg, user=user)

  def _create_comment(self, repo, sha, msg, user=None):
    return self.client.post(
      'repos/%s/%s/commits/%s/comments' % (
        self.client.user(user), repo, sha), data=msg)

  def get_comment(self, repo, id, user=None):
    return self.client.get(
      'repos/%s/%s/comment/%s' % (
        self.client.user(user), repo, id), msg_type=CommentResponse)

  def update_comment(self, repo, id, body, user=None):
    msg = Commit(
      body=body)
    return self.client.post(
      'repos/%s/%s/comments/%s' % (
        self.client.user(user), repo, id), data=msg)

  def delete_comment(self, repo, id, user=None):
    return self.client.delete(
      'repos/%s/%s/comments/%s' % (
        self.client.user(user), repo, id))
