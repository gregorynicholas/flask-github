from flask.ext.protorpc import messages

class Link(messages.Message):
  href = messages.StringField(1)
  git = messages.MessageField('Link', 2)
  self = messages.MessageField('Link', 3)
  html = messages.MessageField('Link', 4)


class User(messages.Message):
  name = messages.StringField(1)
  email = messages.StringField(2)
  id = messages.IntegerField(3, default=0)
  login = messages.StringField(4)
  url = messages.StringField(5)
  blog = messages.StringField(6)
  company = messages.StringField(7)
  location = messages.StringField(8)
  hireable = messages.BooleanField(9, default=False)
  bio = messages.StringField(10)
  avatar_url = messages.StringField(11)
  gravatar_id = messages.StringField(12)
  _links = messages.MessageField(Link, 13, repeated=True)
  # 2012-10-15T18:37:04-07:00
  date = messages.StringField(14)

class UserReponse(messages.Message):
  response = messages.MessageField('User', 1)

class UsersReponse(messages.Message):
  response = messages.MessageField('User', 1, repeated=True)


class RepoPermission(messages.Message):
  push = messages.BooleanField(1, default=False)
  pull = messages.BooleanField(2, default=False)
  admin = messages.BooleanField(3, default=False)

class Repo(messages.Message):
  # "2012-06-01T06:33:47Z"
  created_at = messages.StringField(1)
  has_downloads = messages.BooleanField(2, default=False)
  url = messages.StringField(3)
  description = messages.StringField(4)
  owner = messages.MessageField('User', 5)
  pushed_at = messages.StringField(6)
  svn_url = messages.StringField(7)
  forks = messages.IntegerField(8, default=0)
  has_issues = messages.BooleanField(9, default=False)
  updated_at = messages.StringField(10)
  git_url = messages.StringField(11)
  has_wiki = messages.BooleanField(12, default=False)
  forks_count = messages.IntegerField(13, default=0)
  _links = messages.MessageField(Link, 14, repeated=True)
  size = messages.IntegerField(15, default=0)
  watchers_count = messages.IntegerField(16, default=0)
  language = messages.StringField(17)
  html_url = messages.StringField(18)
  fork = messages.BooleanField(19, default=False)
  full_name = messages.StringField(20)
  permissions = messages.MessageField('RepoPermission', 21, repeated=True)
  open_issues = messages.IntegerField(22, default=0)
  watchers = messages.IntegerField(23, default=0)
  clone_url = messages.StringField(24)
  name = messages.StringField(25)
  homepage = messages.StringField(26)
  open_issues_count = messages.IntegerField(27, default=0)
  private = messages.BooleanField(28, default=False)
  id = messages.IntegerField(29, default=0)
  ssh_url = messages.StringField(30)
  mirror_url = messages.StringField(31)

class RepoResponse(messages.Message):
  response = messages.MessageField('Repo', 1)

class ReposResponse(messages.Message):
  response = messages.MessageField('Repo', 1, repeated=True)


class GitCommit(messages.Message):
  url = messages.StringField(1)
  sha = messages.StringField(2)
  committer = messages.MessageField('User', 3)
  author = messages.MessageField('User', 4)
  comment_count = messages.IntegerField(5, default=0)
  message = messages.StringField(6)
  # string reference allows for recursion..
  tree = messages.MessageField('GitCommit', 7)
  parents = messages.MessageField('GitCommit', 8, repeated=True)
  # fields that live on the tree api responses..
  path = messages.StringField(9)
  mode = messages.StringField(10)
  type = messages.StringField(11)
  size = messages.IntegerField(12, default=0)

class RepoCommit(messages.Message):
  author = messages.MessageField('User', 1)
  url = messages.StringField(2)
  sha = messages.StringField(3)
  parents = messages.MessageField('GitCommit', 4, repeated=True)
  commit = messages.MessageField('GitCommit', 5)
  tree = messages.MessageField('GitCommit', 6)
  committer = messages.MessageField('User', 7)
  message = messages.StringField(8)

class RepoCommitResponse(messages.Message):
  response = messages.MessageField('RepoCommit', 1)

class RepoCommitsResponse(messages.Message):
  response = messages.MessageField('RepoCommit', 1, repeated=True)

class GitDataCommitsResponse(messages.Message):
  response = messages.MessageField('GitCommit', 1, repeated=True)

class Tree(messages.Message):
  url = messages.StringField(1)
  sha = messages.StringField(2)
  message = messages.StringField(3)
  tree = messages.MessageField('Tree', 4, repeated=True)
  # fields that live on the tree api responses..
  path = messages.StringField(5)
  mode = messages.StringField(6)
  type = messages.StringField(7)
  size = messages.IntegerField(8, default=0)
  content = messages.StringField(9)

class TreeRequest(messages.Message):
  # String of the SHA1 of the tree you want to update with new data
  base_tree = messages.StringField(1)
  # list of Tree's specifying a tree structure
  tree = messages.MessageField('Tree', 2, repeated=True)

class TreeResponse(messages.Message):
  response = messages.MessageField('Tree', 1, repeated=True)


class Tag(messages.Message):
  tag = messages.StringField(1)
  message = messages.StringField(2)
  tagger = messages.MessageField('User', 4)
  # fields for tag objects..
  object = messages.MessageField('Tag', 5)
  type = messages.StringField(6)
  sha = messages.StringField(7)
  url = messages.StringField(8)

class TagReponse(messages.Message):
  response = messages.MessageField('Tag', 1)

class TagsReponse(messages.Message):
  response = messages.MessageField('Tag', 1, repeated=True)


class Blob(messages.Message):
  content = messages.BytesField(1)
  encoding = messages.StringField(2, default='utf-8')
  sha = messages.StringField(3)
  size = messages.IntegerField(4, default=0)

class BlobReponse(messages.Message):
  response = messages.MessageField('Blob', 1, repeated=True)


class Org(messages.Message):
  billing_email = messages.StringField(1)
  company = messages.StringField(2)
  email = messages.StringField(3)
  location = messages.StringField(4)
  name = messages.StringField(5)

class Team(messages.Message):
  name = messages.StringField(1)
  repo_names = messages.StringField(2, repeated=True)
  permission = messages.StringField(3)

class GitDataReference(messages.Message):
  sha = messages.StringField(1)
  ref = messages.StringField(2)
  force = messages.BooleanField(3, default=False)

class PullRequest(messages.Message):
  title = messages.StringField(1)
  base = messages.StringField(2)
  head = messages.StringField(3)
  body = messages.StringField(4)
  issue = messages.StringField(5)

class CommitMessage(messages.Message):
  commit_message = messages.StringField(1)

class PullReviewComment(messages.Message):
  commit_message = messages.StringField(1)


class RepoHookRequest(messages.Message):
  name = messages.StringField(1)
  config = messages.StringField(2)
  events = messages.StringField(3)
  add_events = messages.BooleanField(4, default=True)
  remove_events = messages.BooleanField(5, default=True)
  active = messages.BooleanField(6, default=True)


class KeyListRequest(messages.Message):
  keys = messages.MessageField('Key', 1, repeated=True)

class Key(messages.Message):
  title = messages.StringField(1)
  key = messages.StringField(2)
