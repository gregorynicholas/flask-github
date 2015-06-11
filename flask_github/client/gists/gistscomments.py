from __future__ import unicode_literals
from ..messages import GistComment
from ..requests import GistCommentResponse
from ..requests import GistCommentListResponse

class GistsComments:
  def __init__(self, client):
    self.client = client

  def list(self, id):
    return self.client.get(
      'gists/%s/comments' % id, msg_type=GistCommentListResponse)

  def get(self, id):
    return self.client.get(
      'gists/comments/%s' % id, msg_type=GistCommentResponse)

  def create(self, id, body):
    msg = {
      'body': body
    }
    return self.client.post(
      'gists/%s/comments' % id, data=msg, msg_type=GistCommentResponse)

  def edit(self, id, body):
    msg = {
      'body': body
    }
    return self.client.patch(
      'gists/comments/%s' % id, data=msg, msg_type=GistCommentResponse)

  def delete(self, id):
    return self.client.delete(
      'gists/comments/%s' % id)
