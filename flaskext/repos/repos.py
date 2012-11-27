from reposkeys import ReposKeys
from reposhooks import ReposHooks
from reposforks import ReposForks
from reposcommits import ReposCommits
from reposwatching import ReposWatching
from reposstarring import ReposStarring
from reposdownloads import ReposDownloads
from reposcollaborators import ReposCollaborators

from ..messages import Repo
from ..messages import RepoResponse
from ..messages import ReposResponse
from ..messages import TagsResponse
from ..messages import UsersResponse


class Repos:
  def __init__(self, github):
    self.github = github
    self.collaborators = ReposCollaborators(self.github)
    self.commits = ReposCommits(self.github)
    self.downloads = ReposDownloads(self.github)
    self.forks = ReposForks(self.github)
    self.keys = ReposKeys(self.github)
    self.watching = ReposWatching(self.github)
    self.starring = ReposStarring(self.github)
    self.hooks = ReposHooks(self.github)

  def list_user_repos(self, user=None):
    url = 'user/repos'
    if user and user != self.github.username:
      url = 'users/%s/repos' % self.username(user)
    return self.github.get(url, ReposResponse)

  def create_user_repo(self, name, description=None, homepage=None,
       private=False, has_issues=True, has_wiki=True, has_downloads=True):
    msg = Repo(
      name=name,
      private=private,
      has_issues=has_issues,
      has_wiki=has_wiki,
      has_downloads=has_downloads,
      description=description,
      homepage=homepage)
    return self.github.post('user/repos', msg, RepoResponse)

  def list_org_repos(self, org):
    return self.github.get('orgs/%s/repos' % org, ReposResponse)

  def create_org_repo(self, org, name, description=None, homepage=None,
      private=False, has_issues=True, has_wiki=True, has_downloads=True):
    msg = Repo(
      name=name,
      private=private,
      has_issues=has_issues,
      has_wiki=has_wiki,
      has_downloads=has_downloads,
      description=description,
      homepage=homepage)
    return self.github.post('orgs/%s/repos' % org, msg, RepoResponse)

  def get_repo(self, repo, user=None):
    return self.github.get(
      'repos/%s/%s' % (self.username(user), repo), RepoResponse)

  def edit_repo(self, repo, name, description=None, homepage=None, private=False,
      has_issues=True, has_wiki=True, has_downloads=True, user=None):
    msg = Repo(
      name=name,
      private=private,
      has_issues=has_issues,
      has_wiki=has_wiki,
      has_downloads=has_downloads,
      description=description,
      homepage=homepage)
    return self.github.patch(
      'repos/%s/%s' % (self.username(user), repo), msg)

  def list_contributors(self, repo, user=None):
    return self.github.get(
      'repos/%s/%s/contributors' % (self.username(user), repo), UsersResponse)

  def list_tags(self, repo, user=None ):
    return self.github.get(
      'repos/%s/%s/tags' % (self.username(user), repo), TagsResponse)

  def list_langs(self, repo, user=None ):
    return self.github.get(
      'repos/%s/%s/languages' % (self.username(user), repo))

  def list_teams(self, repo, user=None):
    return self.github.get(
      'repos/%s/%s/teams' % (self.username(user), repo))

  def list_branches(self, repo, user=None ):
    return self.github.get(
      'repos/%s/%s/branches' % (self.username(user), repo))

  def username(self, user):
    return self.github.username if user is None else user
