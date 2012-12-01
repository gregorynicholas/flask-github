from ..messages import RepoCommit
from ..requests import RepoCommitResponse
from ..requests import RepoCommitListResponse

class ReposCommits:
  def __init__(self, client):
    self.client = client

  def list_commits(self, repo, sha=None, path=None, user=None):
    query = None
    if sha and path:
      query = {'sha': sha, 'path': path}
    return self.client.get('repos/%s/%s/commits' % (
      self.client.user(user), repo), query=query, msg_type=RepoCommitListResponse)

  def get_commit(self, repo, sha, user=None):
    return self.client.get(
      'repos/%s/%s/commits/%s' % (
        self.client.user(user), repo, sha), msg_type=RepoCommitResponse)

  def list_repo_comments(self, repo, user=None):
    return self.client.get(
      'repos/%s/%s/comments' % (
        self.client.user(user), repo), msg_type=RepoCommitListResponse)

  def list_comments(self, repo, sha, user=None):
    return self.client.get(
      'repos/%s/%s/comments/%s/comments' % (
        self.client.user(user), repo, sha), msg_type=RepoCommitListResponse)

  def create_comment(self, repo, sha, body, line, path, position, user=None):
    msg = RepoCommit(
      body=body,
      commit_id=sha,
      line=line,
      path=path,
      position=position)
    return self.client.post(
      'repos/%s/%s/commits/%s/comments' % (
        self.client.user(user), repo, sha), data=msg)

  def get_single_comment(self, repo, id, user=None):
    return self.client.get(
      'repos/%s/%s/comment/%s' % (
        self.client.user(user), repo, id), msg_type=None)

  def update_comment(self, repo, id, body, user=None):
    msg = RepoCommit(
      body=body)
    return self.client.post(
      'repos/%s/%s/comments/%s' % (
        self.client.user(user), repo, id), data=msg)

  def compare_commits(self, repo, base, head, user=None):
    return self.client.get(
      'repos/%s/%s/compare/%s...:%s' % (
        self.client.user(user), repo, base, head))

  def delete_comment(self, repo, id, user=None):
    return self.client.delete(
      'repos/%s/%s/comments/%s' % (
        self.client.user(user), repo, id))
