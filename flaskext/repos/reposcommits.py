from ..messages import RepoCommit
from ..messages import RepoCommitResponse
from ..messages import RepoCommitsResponse

class ReposCommits:
  def __init__(self, github):
    self.github = github

  def list_commits(self, repo, sha=None, path=None, user=None):
    params = {'sha': sha, 'path': path}
    url = 'repos/%s/%s/commits' % (self.username(user), repo)
    if sha and path:
      # todo: urlencode params?
      url = 'repos/%s/%s/commits?%s' % (self.username(user), repo, params)
    return self.github.get(url, RepoCommitsResponse)

  def get_commit(self, repo, sha, user=None):
    return self.github.get(
      'repos/%s/%s/commits/%s' % (
        self.username(user), repo, sha), RepoCommitResponse)

  def list_repo_comments(self, repo, user=None):
    return self.github.get(
      'repos/%s/%s/comments' % (
        self.username(user), repo), RepoCommitsResponse)

  def list_comments(self, repo, sha, user=None):
    return self.github.get(
      'repos/%s/%s/comments/%s/comments' % (
        self.username(user), repo, sha), RepoCommitsResponse)

  def create_comment(self, repo, sha, body, line, path, position, user=None):
    msg = RepoCommit()
    msg.body = body
    msg.commit_id = sha
    msg.line = line
    msg.path = path
    msg.position = position
    return self.github.post(
      'repos/%s/%s/commits/%s/comments' % (
        self.username(user), repo, sha), msg)

  def get_single_comment(self, repo, id, user=None):
    return self.github.get(
      'repos/%s/%s/comment/%s' % (self.username(user), repo, id))

  def update_comment(self, repo, id, body, user=None):
    msg = RepoCommit()
    msg.body = body
    return self.github.post(
      'repos/%s/%s/comments/%s' % (
        self.username(user), repo, id), msg)

  def compare_commits(self, repo, base, head, user=None):
    return self.github.get(
      'repos/%s/%s/compare/%s...:%s' % (self.username(user), repo, base, head))

  def delete_comment(self, repo, id, user=None):
    return self.github.delete(
      'repos/%s/%s/comments/%s' % (self.username(user), repo, id))

  def username(self, user):
    return self.github.username if user is None else user
