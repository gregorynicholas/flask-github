from ..requests import UserResponse
from ..requests import UserListResponse

class ReposCollaborators:
  def __init__(self, client):
    self.client = client

  def list(self, repo, user=None):
    return self.client.get(
      'repos/%s/%s/collaborators' % (
        self.client.user(user), repo), msg_type=UserListResponse)

  def get(self, repo, collaborator, user=None):
    return self.client.get(
      'repos/%s/%s/collaborators/%s' % (
        self.client.user(user), repo, collaborator), msg_type=UserResponse)

  def add(self, repo, collaborator, user=None):
    return self.client.put(
      'repos/%s/%s/collaborators/%s' % (
        self.client.user(user), repo, collaborator), msg_type=UserResponse)

  def delete(self, repo, collaborator, user=None):
    return self.client.delete(
      'repos/%s/%s/collaborators/%s' % (
        self.client.user(user), repo, collaborator))
