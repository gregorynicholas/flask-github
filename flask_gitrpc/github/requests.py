from flask_protorpc import messages as msgs
from messages import *

class RepoResponse(msgs.Message):
  response = msgs.MessageField('Repo', 1)

class RepoListResponse(msgs.Message):
  response = msgs.MessageField('Repo', 1, repeated=True)

class RepoHookResponse(msgs.Message):
  response = msgs.MessageField('RepoHook', 1)

class RepoHookListResponse(msgs.Message):
  response = msgs.MessageField('RepoHook', 1, repeated=True)

class RepoCommitResponse(msgs.Message):
  response = msgs.MessageField('RepoCommit', 1)

class RepoCommitListResponse(msgs.Message):
  response = msgs.MessageField('RepoCommit', 1, repeated=True)

class GitDataCommitResponse(msgs.Message):
  response = msgs.MessageField('GitCommit', 1)

class GitDataCommitListResponse(msgs.Message):
  response = msgs.MessageField('GitCommit', 1, repeated=True)

class TreeResponse(msgs.Message):
  response = msgs.MessageField('Tree', 1)

class TreeListResponse(msgs.Message):
  response = msgs.MessageField('Tree', 1, repeated=True)

class TeamResponse(msgs.Message):
  response = msgs.MessageField('Team', 1)

class TeamListResponse(msgs.Message):
  response = msgs.MessageField('Team', 1, repeated=True)

class TagReponse(msgs.Message):
  response = msgs.MessageField('Tag', 1)

class TagListReponse(msgs.Message):
  response = msgs.MessageField('Tag', 1, repeated=True)

class KeyResponse(msgs.Message):
  response = msgs.MessageField('Key', 1)

class KeyListResponse(msgs.Message):
  response = msgs.MessageField('Key', 1, repeated=True)

class UserReponse(msgs.Message):
  response = msgs.MessageField('User', 1)

class UserListReponse(msgs.Message):
  response = msgs.MessageField('User', 1, repeated=True)

class GitDataBlobResponse(msgs.Message):
  response = msgs.MessageField('Blob', 1)

class GitDataBlobListResponse(msgs.Message):
  response = msgs.MessageField('Blob', 1, repeated=True)

class GitDataReferenceResponse(msgs.Message):
  response = msgs.MessageField('GitDataReference', 1)

class GitDataReferenceListResponse(msgs.Message):
  response = msgs.MessageField('GitDataReference', 1, repeated=True)

class PullReviewCommentResponse(msgs.Message):
  response = msgs.MessageField('PullReviewComment')

class PullReviewCommentListResponse(msgs.Message):
  response = msgs.MessageField('PullReviewComment', 1, repeated=True)

class PullRequestResponse(msgs.Message):
  response = msgs.MessageField('PullRequest')

class PullRequestListResponse(msgs.Message):
  response = msgs.MessageField('PullRequest', 1, repeated=True)
