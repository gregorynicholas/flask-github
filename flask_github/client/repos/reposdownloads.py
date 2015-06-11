from __future__ import unicode_literals
import json
from ..requests import RepoDownloadResponse
from ..requests import RepoDownloadListResponse

class ReposDownloads:
  def __init__(self, client):
    self.client = client

  def list(self, repo, user=None):
    return self.client.get(
      'repos/%s/%s/downloads' % (
        self.client.username(user), repo), msg_type=RepoDownloadListResponse)

  def get(self, repo, id, user=None):
    return self.client.get(
      'repos/%s/%s/downloads/%s' % (
        self.client.username(user), repo, id), msg_type=RepoDownloadResponse)

  def create(self, repo, name, size, description=None,
      content_type=None, user=None):
    msg = {
      'name': name,
      'size': size,
      'description': description,
      'content_type': content_type
    }
    # TODO
    response = self.client.post(
      'repos/%s/%s/downloads/%s' % (
        self.client.username(user), repo, id), msg)
    data = json.loads(response)
    return data

  def delete(self, repo, id, user=None):
    return self.client.delete(
      'repos/%s/%s/downloads/%s' % (
        self.client.username(user), repo, id))
