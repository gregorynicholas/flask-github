from ..messages import RepoHook
from ..requests import RepoHookResponse
from ..requests import RepoHookListResponse

class ReposHooks:
  def __init__(self, client):
    self.client = client

  def list_hooks(self, repo, user=None):
    return self.client.get(
      'repos/%s/%s/hooks' % (
        self.client.user(user), repo), msg_type=RepoHookListResponse)

  def get_hook(self, repo, id, user=None):
    return self.client.get(
      'repos/%s/%s/hooks/%s' % (
        self.client.user(user), repo, id), msg_type=RepoHookResponse)

  def create_hook(self, repo, name, config, events=None, active=True,
      user=None):
    msg = RepoHook(
      name=name,
      config=config,
      events=events,
      active=active)
    return self.client.post(
      'repos/%s/%s/hooks' % (
        self.client.user(user), repo), msg)

  def edit_hook(self, repo, id, name, config, events=None, add_events=None,
      remove_events=None, active=True, user=None):
    msg = RepoHook(
      name=name,
      config=config,
      events=events,
      active=active,
      add_events=add_events,
      remove_events=remove_events)
    return self.client.patch(
      'repos/%s/%s/hooks/%s' % (
        self.client.user(user), repo, id), msg)

  def test_hook(self, repo, id, user=None):
    return self.client.post(
      'repos/%s/%s/hooks/%s/test' % (
        self.client.user(user), repo, id))

  def delete_hook(self, repo, id, user=None):
    return self.client.delete(
      'repos/%s/%s/hooks/%s' % (
        self.client.user(user), repo, id))
