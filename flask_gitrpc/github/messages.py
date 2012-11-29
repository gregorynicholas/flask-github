from flask_protorpc.proto import messages as msgs

class Link(msgs.Message):
  href = msgs.StringField(1)
  git = msgs.MessageField('Link', 2)
  self = msgs.MessageField('Link', 3)
  html = msgs.MessageField('Link', 4)

class User(msgs.Message):
  name = msgs.StringField(1)
  email = msgs.StringField(2)
  id = msgs.IntegerField(3, default=0)
  login = msgs.StringField(4)
  url = msgs.StringField(5)
  blog = msgs.StringField(6)
  company = msgs.StringField(7)
  location = msgs.StringField(8)
  hireable = msgs.BooleanField(9, default=False)
  bio = msgs.StringField(10)
  avatar_url = msgs.StringField(11)
  gravatar_id = msgs.StringField(12)
  _links = msgs.MessageField('Link', 13, repeated=True)
  # 2012-10-15T18:37:04-07:00
  date = msgs.StringField(14)
  created_at = msgs.StringField(15)
  type = msgs.StringField(16)
  following = msgs.IntegerField(17, default=0)
  followers = msgs.IntegerField(18, default=0)
  public_repos = msgs.IntegerField(19, default=0)
  public_gists = msgs.IntegerField(20, default=0)
  total_private_repos = msgs.IntegerField(21, default=0)
  owned_private_repos = msgs.IntegerField(22, default=0)
  private_gists = msgs.IntegerField(23, default=0)
  disk_usage = msgs.IntegerField(24, default=0)
  collaborators = msgs.IntegerField(25, default=0)
  html_url = msgs.StringField(26)
  repos_url = msgs.StringField(27)
  events_url = msgs.StringField(28)
  members_url = msgs.StringField(29)
  public_members_url = msgs.StringField(30)

class RepoPermission(msgs.Message):
  push = msgs.BooleanField(1, default=False)
  pull = msgs.BooleanField(2, default=False)
  admin = msgs.BooleanField(3, default=False)

class Repo(msgs.Message):
  created_at = msgs.StringField(1)
  has_downloads = msgs.BooleanField(2, default=False)
  url = msgs.StringField(3)
  description = msgs.StringField(4)
  owner = msgs.MessageField('User', 5)
  pushed_at = msgs.StringField(6)
  svn_url = msgs.StringField(7)
  forks = msgs.IntegerField(8, default=0)
  has_issues = msgs.BooleanField(9, default=False)
  updated_at = msgs.StringField(10)
  git_url = msgs.StringField(11)
  has_wiki = msgs.BooleanField(12, default=False)
  forks_count = msgs.IntegerField(13, default=0)
  _links = msgs.MessageField('Link', 14, repeated=True)
  size = msgs.IntegerField(15, default=0)
  watchers_count = msgs.IntegerField(16, default=0)
  language = msgs.StringField(17)
  html_url = msgs.StringField(18)
  fork = msgs.BooleanField(19, default=False)
  full_name = msgs.StringField(20)
  permissions = msgs.MessageField('RepoPermission', 21, repeated=True)
  open_issues = msgs.IntegerField(22, default=0)
  watchers = msgs.IntegerField(23, default=0)
  clone_url = msgs.StringField(24)
  name = msgs.StringField(25)
  homepage = msgs.StringField(26)
  open_issues_count = msgs.IntegerField(27, default=0)
  private = msgs.BooleanField(28, default=False)
  id = msgs.IntegerField(29, default=0)
  ssh_url = msgs.StringField(30)
  mirror_url = msgs.StringField(31)


class GitCommit(msgs.Message):
  url = msgs.StringField(1)
  sha = msgs.StringField(2)
  committer = msgs.MessageField('User', 3)
  author = msgs.MessageField('User', 4)
  comment_count = msgs.IntegerField(5, default=0)
  message = msgs.StringField(6)
  # string reference allows for recursion..
  tree = msgs.MessageField('GitCommit', 7)
  parents = msgs.MessageField('GitCommit', 8, repeated=True)
  # fields that live on the tree api responses..
  path = msgs.StringField(9)
  mode = msgs.StringField(10)
  type = msgs.StringField(11)
  size = msgs.IntegerField(12, default=0)
  # fields for the hooks payload..
  id = msgs.StringField(13)
  timestamp = msgs.StringField(14)
  added = msgs.StringField(15, repeated=True)
  removed = msgs.StringField(16, repeated=True)
  modified = msgs.StringField(17, repeated=True)

class RepoCommit(msgs.Message):
  author = msgs.MessageField('User', 1)
  url = msgs.StringField(2)
  sha = msgs.StringField(3)
  parents = msgs.MessageField('GitCommit', 4, repeated=True)
  commit = msgs.MessageField('GitCommit', 5)
  tree = msgs.MessageField('GitCommit', 6)
  committer = msgs.MessageField('User', 7)
  message = msgs.StringField(8)

class Tree(msgs.Message):
  url = msgs.StringField(1)
  sha = msgs.StringField(2)
  message = msgs.StringField(3)
  tree = msgs.MessageField('Tree', 4, repeated=True)
  # fields that live on the tree api responses..
  path = msgs.StringField(5)
  mode = msgs.StringField(6)
  type = msgs.StringField(7)
  size = msgs.IntegerField(8, default=0)
  content = msgs.StringField(9)
  # String of the SHA1 of the tree you want to update with new data
  base_tree = msgs.StringField(10)


class Tag(msgs.Message):
  tag = msgs.StringField(1)
  message = msgs.StringField(2)
  tagger = msgs.MessageField('User', 4)
  # fields for tag objects..
  object = msgs.MessageField('Tag', 5)
  type = msgs.StringField(6)
  sha = msgs.StringField(7)
  url = msgs.StringField(8)

class RepoTag(msgs.Message):
  name = msgs.StringField(1)
  commit = msgs.MessageField('GitCommit', 2)
  zipball_url = msgs.StringField(3)
  tarball_url = msgs.StringField(4)

class Blob(msgs.Message):
  content = msgs.BytesField(1)
  encoding = msgs.StringField(2, default='utf-8')
  sha = msgs.StringField(3)
  size = msgs.IntegerField(4, default=0)


class Org(msgs.Message):
  id = msgs.IntegerField(1, default=0)
  login = msgs.StringField(2)
  company = msgs.StringField(3)
  billing_email = msgs.StringField(4)
  email = msgs.StringField(5)
  location = msgs.StringField(6)
  name = msgs.StringField(7)
  members = msgs.MessageField('User', 8, repeated=True)
  url = msgs.StringField(9)
  repos_url = msgs.StringField(10)
  events_url = msgs.StringField(11)
  avatar_url = msgs.StringField(12)
  members_url = msgs.StringField(13)
  public_members_url = msgs.StringField(14)

class Team(msgs.Message):
  name = msgs.StringField(1)
  repo_names = msgs.StringField(2, repeated=True)
  permission = msgs.StringField(3)

class GitDataReference(msgs.Message):
  sha = msgs.StringField(1)
  ref = msgs.StringField(2)
  force = msgs.BooleanField(3, default=False)

class PullRequest(msgs.Message):
  title = msgs.StringField(1)
  base = msgs.StringField(2)
  head = msgs.StringField(3)
  body = msgs.StringField(4)
  issue = msgs.StringField(5)

class CommitMessage(msgs.Message):
  commit_message = msgs.StringField(1)

class PullReviewComment(msgs.Message):
  commit_message = msgs.StringField(1)

class RepoHook(msgs.Message):
  id = msgs.IntegerField(1, default=0)
  name = msgs.StringField(2)
  events = msgs.StringField(3, repeated=True)
  add_events = msgs.BooleanField(4, default=True)
  remove_events = msgs.BooleanField(5, default=True)
  active = msgs.BooleanField(6, default=True)
  config = msgs.MessageField('RepoHookConfig', 7)

class RepoHookConfig(msgs.Message):
  url = msgs.StringField(1)
  insecure_ssl = msgs.StringField(2)
  content_type = msgs.StringField(3)

class CommitHookPayload(msgs.Message):
  before = msgs.StringField(1)
  after = msgs.StringField(2)
  ref = msgs.StringField(3)
  commits = msgs.MessageField('GitCommit', 4)
  repository = msgs.MessageField('Repo', 5)

class Key(msgs.Message):
  title = msgs.StringField(1)
  key = msgs.StringField(2)
