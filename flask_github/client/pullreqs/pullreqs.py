from __future__ import unicode_literals
from pullreqsreviewcomments import PullReviewComments
from ..messages import PullRequest
from ..messages import CommitMessage
from ..requests import PullRequestResponse
from ..requests import PullRequestListResponse

class PullRequests:
  def __init__(self, client):
    self.client = client
    self.reviewcomments = PullReviewComments(self.client)

  def list(self, repo, state=None, user=None):
    query = None
    if state:
      query = {'state': state}
    return self.client.get('repos/%s/%s/pulls' % (self.client.user(user),
      repo), query=query, msg_type=PullRequestListResponse)

  def get(self, repo, id, user=None):
    return self.client.get(
      'repos/%s/%s/pulls/%s' % (
        self.client.user(user), repo, id), msg_type=PullRequestResponse)

  def create(self, repo, title, base, head, body=None, user=None):
    msg = PullRequest(
      title=title,
      base=base,
      head=head,
      body=body)
    return self._create(repo=repo, msg=msg, user=user)

  def _create(self, repo, msg, user=None):
    return self.client.post(
      'repos/%s/%s/pulls' % (self.client.user(user), repo), data=msg,
      msg_type=PullRequestResponse)

  def create_from_issue(self, repo, issue, base, head, user=None):
    msg = PullRequest(
      issue=issue,
      base=base,
      head=head)
    return self.client.post(
      'repos/%s/%s/pulls' % (
        self.client.user(user), repo), data=msg, msg_type=PullRequestResponse)

  def list_commits(self, repo, id, user=None):
    return self.client.get(
      'repos/%s/%s/pulls/%s/commits' % (
        self.client.user(user), repo, id), msg_type=None)

  def list_files(self, repo, id, user=None):
    return self.client.get(
      'repos/%s/%s/pulls/%s/files' % (
        self.client.user(user), repo, id), msg_type=None)

  def get_if_merged(self, repo, id, user=None):
    return self.client.get(
      'repos/%s/%s/pulls/%s/merge' % (
        self.client.user(user), repo, id), msg_type=None)

  def merge(self, repo, id, commit_message=None, user=None):
    if commit_message:
      msg = CommitMessage(
        commit_message=commit_message)
      return self.client.put(
        'repos/%s/%s/pulls/%s/merge' % (
          self.client.user(user), repo, id), data=msg)
    else:
      return self.client.put(
        'repos/%s/%s/pulls/%s/merge' % (
          self.client.user(user), repo, id))
