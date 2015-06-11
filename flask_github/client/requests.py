from __future__ import unicode_literals
from flask_protorpc.proto import messages as msgs
from messages import *

class RepoResponse(msgs.Message):
  response = msgs.MessageField('Repo', 1)

class RepoListResponse(msgs.Message):
  response = msgs.MessageField('Repo', 1, repeated=True)

class HookResponse(msgs.Message):
  response = msgs.MessageField('Hook', 1)

class HookTestResponse(msgs.Message):
  response = msgs.MessageField('Hook', 1)

class HookListResponse(msgs.Message):
  response = msgs.MessageField('Hook', 1, repeated=True)

class HookPushPayload(msgs.Message):
  payload = msgs.MessageField('HookCommit', 1)

class CommitResponse(msgs.Message):
  response = msgs.MessageField('Commit', 1)

class CommitListResponse(msgs.Message):
  response = msgs.MessageField('Commit', 1, repeated=True)

class CommentResponse(msgs.Message):
  response = msgs.MessageField('Comment', 1)

class CommentListResponse(msgs.Message):
  response = msgs.MessageField('Comment', 1, repeated=True)

class GitDataCommitResponse(msgs.Message):
  response = msgs.MessageField('Commit', 1)

class GitDataCommitListResponse(msgs.Message):
  response = msgs.MessageField('Commit', 1, repeated=True)

class TreeResponse(msgs.Message):
  response = msgs.MessageField('Tree', 1)

class TreeListResponse(msgs.Message):
  response = msgs.MessageField('Tree', 1, repeated=True)

class TeamResponse(msgs.Message):
  response = msgs.MessageField('Team', 1)

class TeamListResponse(msgs.Message):
  response = msgs.MessageField('Team', 1, repeated=True)

class TagResponse(msgs.Message):
  response = msgs.MessageField('Tag', 1)

class TagListResponse(msgs.Message):
  response = msgs.MessageField('Tag', 1, repeated=True)

class KeyResponse(msgs.Message):
  response = msgs.MessageField('Key', 1)

class KeyListResponse(msgs.Message):
  response = msgs.MessageField('Key', 1, repeated=True)

class UserResponse(msgs.Message):
  response = msgs.MessageField('User', 1)

class UserListResponse(msgs.Message):
  response = msgs.MessageField('User', 1, repeated=True)

class UserEmailResponse(msgs.Message):
  response = msgs.MessageField('UserEmail', 1)

class UserEmailListResponse(msgs.Message):
  response = msgs.MessageField('UserEmail', 1, repeated=True)

class BlobResponse(msgs.Message):
  response = msgs.MessageField('Blob', 1)

class BlobListResponse(msgs.Message):
  response = msgs.MessageField('Blob', 1, repeated=True)

class RefResponse(msgs.Message):
  response = msgs.MessageField('Ref', 1)

class RefListResponse(msgs.Message):
  response = msgs.MessageField('Ref', 1, repeated=True)

class PullReviewCommentResponse(msgs.Message):
  response = msgs.MessageField('PullReviewComment', 1)

class PullReviewCommentListResponse(msgs.Message):
  response = msgs.MessageField('PullReviewComment', 1, repeated=True)

class PullRequestResponse(msgs.Message):
  response = msgs.MessageField('PullRequest', 1)

class PullRequestListResponse(msgs.Message):
  response = msgs.MessageField('PullRequest', 1, repeated=True)

class OrgListResponse(msgs.Message):
  response = msgs.MessageField('Org', 1, repeated=True)

class RepoDownloadResponse(msgs.Message):
  response = msgs.MessageField('RepoDownload', 1)

class RepoDownloadListResponse(msgs.Message):
  response = msgs.MessageField('RepoDownload', 1, repeated=True)

class EventResponse(msgs.Message):
  response = msgs.MessageField('Event', 1)

class EventListResponse(msgs.Message):
  response = msgs.MessageField('Event', 1, repeated=True)

class GistResponse(msgs.Message):
  response = msgs.MessageField('Gist', 1)

class GistListResponse(msgs.Message):
  response = msgs.MessageField('Gist', 1, repeated=True)

class GistCommentResponse(msgs.Message):
  response = msgs.MessageField('GistComment', 1)

class GistCommentListResponse(msgs.Message):
  response = msgs.MessageField('GistComment', 1, repeated=True)

class IssueResponse(msgs.Message):
  response = msgs.MessageField('Issue', 1)

class IssueListResponse(msgs.Message):
  response = msgs.MessageField('Issue', 1, repeated=True)

class IssueEventResponse(msgs.Message):
  response = msgs.MessageField('IssueEvent', 1)

class IssueEventListResponse(msgs.Message):
  response = msgs.MessageField('IssueEvent', 1, repeated=True)

class IssueLabelResponse(msgs.Message):
  response = msgs.MessageField('IssueLabel', 1)

class IssueLabelListResponse(msgs.Message):
  response = msgs.MessageField('IssueLabel', 1, repeated=True)

class IssueMilestoneResponse(msgs.Message):
  response = msgs.MessageField('IssueMilestone', 1)

class IssueMilestoneListResponse(msgs.Message):
  response = msgs.MessageField('IssueMilestone', 1, repeated=True)

class IssueCommentResponse(msgs.Message):
  response = msgs.MessageField('IssueComment', 1)

class IssueCommentListResponse(msgs.Message):
  response = msgs.MessageField('IssueComment', 1, repeated=True)
