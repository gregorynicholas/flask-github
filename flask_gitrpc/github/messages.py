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

class Repo(msgs.Message):
  id = msgs.IntegerField(1, default=0)
  name = msgs.StringField(2)
  full_name = msgs.StringField(3)
  description = msgs.StringField(4)
  owner = msgs.MessageField('User', 5)
  created_at = msgs.StringField(6)
  pushed_at = msgs.StringField(7)
  updated_at = msgs.StringField(8)
  has_wiki = msgs.BooleanField(9, default=False)
  has_issues = msgs.BooleanField(10, default=False)
  has_downloads = msgs.BooleanField(11, default=False)
  private = msgs.BooleanField(12, default=False)
  size = msgs.IntegerField(13, default=0)
  forks = msgs.IntegerField(14, default=0)
  forks_count = msgs.IntegerField(15, default=0)
  watchers = msgs.IntegerField(16, default=0)
  watchers_count = msgs.IntegerField(17, default=0)
  open_issues_count = msgs.IntegerField(18, default=0)
  open_issues = msgs.IntegerField(19, default=0)
  language = msgs.StringField(20)
  fork = msgs.BooleanField(21, default=False)
  permissions = msgs.MessageField('RepoPermission', 22, repeated=True)
  url = msgs.StringField(23)
  git_url = msgs.StringField(24)
  svn_url = msgs.StringField(25)
  ssh_url = msgs.StringField(26)
  html_url = msgs.StringField(27)
  clone_url = msgs.StringField(28)
  mirror_url = msgs.StringField(29)
  homepage = msgs.StringField(30)
  ref = msgs.StringField(31)
  master_branch = msgs.StringField(32)

class RepoPermission(msgs.Message):
  push = msgs.BooleanField(1, default=False)
  pull = msgs.BooleanField(2, default=False)
  admin = msgs.BooleanField(3, default=False)

class Commit(msgs.Message):
  url = msgs.StringField(1)
  sha = msgs.StringField(2)
  committer = msgs.MessageField('User', 3)
  author = msgs.MessageField('User', 4)
  comment_count = msgs.IntegerField(5, default=0)
  message = msgs.StringField(6)
  # string reference allows for recursion..
  tree = msgs.MessageField('Commit', 7)
  parents = msgs.MessageField('Commit', 8, repeated=True)
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
  commit = msgs.MessageField('Commit', 18)

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
  commit = msgs.MessageField('Commit', 2)
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

class Ref(msgs.Message):
  sha = msgs.StringField(1)
  ref = msgs.StringField(2)
  force = msgs.BooleanField(3, default=False)

class RefType(msgs.Enum):
  TAG = 1
  BRANCH = 2

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

class Hook(msgs.Message):
  id = msgs.IntegerField(1, default=0)
  name = msgs.StringField(2)
  events = msgs.StringField(3, repeated=True)
  add_events = msgs.StringField(4, repeated=True)
  remove_events = msgs.StringField(5, repeated=True)
  active = msgs.BooleanField(6, default=True)
  config = msgs.MessageField('HookConfig', 7)

class HookConfig(msgs.Message):
  url = msgs.StringField(1)
  insecure_ssl = msgs.StringField(2)
  content_type = msgs.StringField(3)

class Key(msgs.Message):
  id = msgs.IntegerField(1, default=0)
  title = msgs.StringField(2)
  key = msgs.StringField(3)

class HookCommit(msgs.Message):
  before = msgs.StringField(1)
  after = msgs.StringField(2)
  # refs/heads/master
  ref = msgs.StringField(3)
  pusher = msgs.MessageField('HookUser', 4)
  commits = msgs.MessageField('Commit', 5)
  repository = msgs.MessageField('Repo', 6)
  head_commit = msgs.MessageField('Commit', 7)
  # https://github.com/:user/:repo/compare/27766a14cfc5...36ddb3e3047b
  compare = msgs.StringField(8)
  forced = msgs.BooleanField(9, default=False)
  deleted = msgs.BooleanField(10, default=False)
  created = msgs.BooleanField(11, default=False)

class HookUser(msgs.Message):
  name = msgs.StringField(1)

class RepoDownload(msgs.Message):
  '''
  {
    "url": "https://api.github.com/repos/octocat/Hello-World/downloads/1",
    "html_url": "https://github.com/repos/octocat/Hello-World/downloads/new_file.jpg",
    "id": 1,
    "name": "new_file.jpg",
    "description": "Description of your download",
    "size": 1024,
    "download_count": 40,
    "content_type": ".jpg"
  }
  '''
  pass

class Comment(msgs.Message):
  '''
  {
    "url": "https://api.github.com/repos/octocat/Hello-World/pulls/comments/1",
    "id": 1,
    "body": "Great stuff",
    "path": "file1.txt",
    "position": 4,
    "commit_id": "6dcb09b5b57875f334f61aebed695e2e4193db5e",
    "user": {
      "login": "octocat",
      "id": 1,
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "gravatar_id": "somehexcode",
      "url": "https://api.github.com/users/octocat"
    },
    "created_at": "2011-04-14T16:00:49Z",
    "updated_at": "2011-04-14T16:00:49Z",
    "_links": {
      "self": {
        "href": "https://api.github.com/octocat/Hello-World/pulls/comments/1"
      },
      "html": {
        "href": "https://github.com/octocat/Hello-World/pull/1#discussion-diff-1"
      },
      "pull_request": {
        "href": "https://api.github.com/octocat/Hello-World/pulls/1"
      }
    }
  }
  '''
  pass

class Event(msgs.Message):
  '''
  {
    "type": "Event",
    "public": true,
    "payload": {

    },
    "repo": {
      "id": 3,
      "name": "octocat/Hello-World",
      "url": "https://api.github.com/repos/octocat/Hello-World"
    },
    "actor": {
      "login": "octocat",
      "id": 1,
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "gravatar_id": "somehexcode",
      "url": "https://api.github.com/users/octocat"
    },
    "org": {
      "login": "octocat",
      "id": 1,
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "gravatar_id": "somehexcode",
      "url": "https://api.github.com/users/octocat"
    },
    "created_at": "2011-09-06T17:26:27Z",
    "id": "12345"
  }
  '''
  pass

class Gist(msgs.Message):
  '''
  {
    "url": "https://api.github.com/gists/ce31e712fff6a9f1b86d",
    "id": "1",
    "description": "description of gist",
    "public": true,
    "user": {
      "login": "octocat",
      "id": 1,
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "gravatar_id": "somehexcode",
      "url": "https://api.github.com/users/octocat"
    },
    "files": {
      "ring.erl": {
        "size": 932,
        "filename": "ring.erl",
        "raw_url": "https://gist.github.com/raw/365370/8c4d2d43d178df44f4c03a7f2ac0ff512853564e/ring.erl"
      }
    },
    "comments": 0,
    "comments_url": "https://api.github.com/gists/3ade1a5eea22f140de20/comments/",
    "html_url": "https://gist.github.com/1",
    "git_pull_url": "git://gist.github.com/1.git",
    "git_push_url": "git@gist.github.com:1.git",
    "created_at": "2010-04-14T02:15:15Z",
    "forks": [
      {
        "user": {
          "login": "octocat",
          "id": 1,
          "avatar_url": "https://github.com/images/error/octocat_happy.gif",
          "gravatar_id": "somehexcode",
          "url": "https://api.github.com/users/octocat"
        },
        "url": "https://api.github.com/gists/4c468075839a695a96ab",
        "created_at": "2011-04-14T16:00:49Z"
      }
    ],
    "history": [
      {
        "url": "https://api.github.com/gists/14a2302d4083e5331759",
        "version": "57a7f021a713b1c5a6a199b54cc514735d2d462f",
        "user": {
          "login": "octocat",
          "id": 1,
          "avatar_url": "https://github.com/images/error/octocat_happy.gif",
          "gravatar_id": "somehexcode",
          "url": "https://api.github.com/users/octocat"
        },
        "change_status": {
          "deletions": 0,
          "additions": 180,
          "total": 180
        },
        "committed_at": "2010-04-14T02:15:15Z"
      }
    ]
  }
  '''
  pass
