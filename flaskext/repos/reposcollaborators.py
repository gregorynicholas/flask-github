from ..messages import UserResponse
from ..messages import UsersResponse

class ReposCollaborators:
  def __init__(self, github):
    self.github = github

  def list(self, repo, user=None):
    return self.github.get(
      'repos/%s/%s/collaborators' % (self.username(user), repo), UsersResponse)

  def get(self, repo, collaborator, user=None):
    return self.github.get(
      'repos/%s/%s/collaborators/%s' % (
        self.username(user), repo, collaborator), UserResponse)

  def add(self, repo, collaborator, user=None):
    return self.github.put(
      'repos/%s/%s/collaborators/%s' % (
        self.username(user), repo, collaborator), UserResponse)

  def delete(self, repo, collaborator, user=None):
    return self.github.delete(
      'repos/%s/%s/collaborators/%s' % (
        self.username(user), repo, collaborator))

  def username(self, user):
    return self.github.username if user is None else user
