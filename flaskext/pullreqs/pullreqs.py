from urllib import urlencode
from pullreqsreviewcomments import PullReviewComments
from ..messages import PullRequest
from ..messages import CommitMessage

class PullRequests:
  def __init__(self, github):
    self.github = github
    self.reviewcomments = PullReviewComments(self.github)

  def list_pull_requests(self, repo, state=None, user=None):
    url = 'repos/%s/%s/pulls' % (self.username(user), repo)
    if state:
      url += '?%s' % (urlencode({'state': state}))
    return self.github.get(url)

  def get_pull_request(self, repo, id, user=None):
    return self.github.get(
      'repos/%s/%s/pulls/%s' % (self.username(user), repo, id))

  def create_pull_request(self, repo, title, base, head, body=None, user=None):
    msg = PullRequest()
    msg.title = title
    msg.base = base
    msg.head = head
    msg.body = body
    return self.github.post(
      'repos/%s/%s/pulls' % (self.username(user), repo), msg)

  def create_pull_requestFromIssue(self, repo, issue, base, head, user=None):
    msg = PullRequest()
    msg.issue = issue
    msg.base = base
    msg.head = head
    return self.github.post(
      'repos/%s/%s/pulls' % (self.username(user), repo), msg)

  def list_pull_requestCommits(self, repo, id, user=None):
    return self.github.get(
      'repos/%s/%s/pulls/%s/commits' % (self.username(user), repo, id))

  def list_pull_requestFiles(self, repo, id, user=None):
    return self.github.get(
      'repos/%s/%s/pulls/%s/files' % (self.username(user), repo, id))

  def getIf_pull_requestMerged(self, repo, id, user=None):
    return self.github.get(
      'repos/%s/%s/pulls/%s/merge' % (self.username(user), repo, id))

  def merge_pull_request(self, repo, id, commit_message=None, user=None):
    if commit_message:
      msg = CommitMessage()
      msg.commit_message = commit_message
      return self.github.put(
        'repos/%s/%s/pulls/%s/merge' % (self.username(user), repo, id), msg)
    else:
      return self.github.put(
        'repos/%s/%s/pulls/%s/merge' % (self.username(user), repo, id))

  def username(self, user):
    return self.github.username if user is None else user
