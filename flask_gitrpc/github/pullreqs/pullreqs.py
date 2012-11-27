from urllib import urlencode
from pullreqsreviewcomments import PullReviewComments
from ..messages import PullRequest
from ..messages import CommitMessage
from ..requests import PullRequestResponse
from ..requests import PullRequestListResponse

class PullRequests:
  def __init__(self, client):
    self.client = client
    self.reviewcomments = PullReviewComments(self.client)

  def list_pull_requests(self, repo, state=None, user=None):
    url = 'repos/%s/%s/pulls' % (self.client.username(user), repo)
    if state:
      url += '?%s' % (urlencode({'state': state}))
    return self.client.get(url, PullRequestListResponse)

  def get_pull_request(self, repo, id, user=None):
    return self.client.get(
      'repos/%s/%s/pulls/%s' % (
        self.client.username(user), repo, id), PullRequestResponse)

  def create_pull_request(self, repo, title, base, head, body=None, user=None):
    msg = PullRequest(
      title=title,
      base=base,
      head=head,
      body=body)
    return self.client.post(
      'repos/%s/%s/pulls' % (
        self.client.username(user), repo), msg)

  def create_pull_request_from_issue(self, repo, issue, base, head, user=None):
    msg = PullRequest(
      issue=issue,
      base=base,
      head=head)
    return self.client.post(
      'repos/%s/%s/pulls' % (
        self.client.username(user), repo), msg)

  def list_pull_request_commits(self, repo, id, user=None):
    return self.client.get(
      'repos/%s/%s/pulls/%s/commits' % (
        self.client.username(user), repo, id))

  def list_pull_request_files(self, repo, id, user=None):
    return self.client.get(
      'repos/%s/%s/pulls/%s/files' % (
        self.client.username(user), repo, id))

  def get_if_pull_request_merged(self, repo, id, user=None):
    return self.client.get(
      'repos/%s/%s/pulls/%s/merge' % (
        self.client.username(user), repo, id))

  def merge_pull_request(self, repo, id, commit_message=None, user=None):
    if commit_message:
      msg = CommitMessage(
        commit_message=commit_message)
      return self.client.put(
        'repos/%s/%s/pulls/%s/merge' % (
          self.client.username(user), repo, id), msg)
    else:
      return self.client.put(
        'repos/%s/%s/pulls/%s/merge' % (
          self.client.username(user), repo, id))
