from flask_protorpc.proto import messages as msgs
from messages import *

class RepoResponse(msgs.Message):
  response = msgs.MessageField('Repo', 1)

class RepoListResponse(msgs.Message):
  response = msgs.MessageField('Repo', 1, repeated=True)

class HookResponse(msgs.Message):
  response = msgs.MessageField('Hook', 1)

class HookListResponse(msgs.Message):
  response = msgs.MessageField('Hook', 1, repeated=True)

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

class RepoTagResponse(msgs.Message):
  response = msgs.MessageField('RepoTag', 1)

class RepoTagListResponse(msgs.Message):
  response = msgs.MessageField('RepoTag', 1, repeated=True)

class KeyResponse(msgs.Message):
  response = msgs.MessageField('Key', 1)

class KeyListResponse(msgs.Message):
  response = msgs.MessageField('Key', 1, repeated=True)

class UserResponse(msgs.Message):
  response = msgs.MessageField('User', 1)

class UserListResponse(msgs.Message):
  response = msgs.MessageField('User', 1, repeated=True)

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

class HookPushPayload(msgs.Message):
  payload = msgs.MessageField('HookCommit', 1)
