from reposkeys import ReposKeys
from reposhooks import ReposHooks
from reposforks import ReposForks
from reposcommits import ReposCommits
from reposwatching import ReposWatching
from reposstarring import ReposStarring
from reposdownloads import ReposDownloads
from reposcollaborators import ReposCollaborators

from ..messages import Repo
from ..requests import RepoResponse
from ..requests import RepoListResponse
from ..requests import TagListResponse
from ..requests import UserListResponse
from ..requests import TeamListResponse


class Repos:
  def __init__(self, client):
    self.client = client
    self.keys = ReposKeys(self.client)
    self.forks = ReposForks(self.client)
    self.hooks = ReposHooks(self.client)
    self.commits = ReposCommits(self.client)
    self.starring = ReposStarring(self.client)
    self.watching = ReposWatching(self.client)
    self.downloads = ReposDownloads(self.client)
    self.collaborators = ReposCollaborators(self.client)

  def list_user_repos(self, user=None):
    url = 'user/repos'
    if user and user != self.client._username:
      url = 'users/%s/repos' % self.client.user(user)
    return self.client.get(url, msg_type=RepoListResponse)

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
    return self.client.post(
      'user/repos', msg, msg_type=RepoResponse)

  def list_org_repos(self, org):
    return self.client.get(
      'orgs/%s/repos' % org, msg_type=RepoListResponse)

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
    return self.client.post(
      'orgs/%s/repos' % org, msg, msg_type=RepoResponse)

  def get_repo(self, repo, user=None):
    return self.client.get(
      'repos/%s/%s' % (
        self.client.user(user), repo), msg_type=RepoResponse)

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
    return self.client.patch(
      'repos/%s/%s' % (
        self.client.user(user), repo), msg)

  def list_contributors(self, repo, user=None):
    return self.client.get(
      'repos/%s/%s/contributors' % (
        self.client.user(user), repo), msg_type=UserListResponse)

  def list_tags(self, repo, user=None ):
    return self.client.get(
      'repos/%s/%s/tags' % (
        self.client.user(user), repo), msg_type=TagListResponse)

  def list_langs(self, repo, user=None ):
    return self.client.get(
      'repos/%s/%s/languages' % (
        self.client.user(user), repo))

  def list_teams(self, repo, user=None):
    return self.client.get(
      'repos/%s/%s/teams' % (
        self.client.user(user), repo), msg_type=TeamListResponse)

  def list_branches(self, repo, user=None ):
    return self.client.get(
      'repos/%s/%s/branches' % (
        self.client.user(user), repo))
