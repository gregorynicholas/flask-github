from ..requests import UserResponse
from ..requests import UserListResponse

class ReposCollaborators:
  def __init__(self, client):
    self.client = client

  def list(self, repo, user=None):
    return self.client.get(
      'repos/%s/%s/collaborators' % (
        self.client.username(user), repo), UserListResponse)

  def get(self, repo, collaborator, user=None):
    return self.client.get(
      'repos/%s/%s/collaborators/%s' % (
        self.client.username(user), repo, collaborator), UserResponse)

  def add(self, repo, collaborator, user=None):
    return self.client.put(
      'repos/%s/%s/collaborators/%s' % (
        self.client.username(user), repo, collaborator), UserResponse)

  def delete(self, repo, collaborator, user=None):
    return self.client.delete(
      'repos/%s/%s/collaborators/%s' % (
        self.client.username(user), repo, collaborator))
