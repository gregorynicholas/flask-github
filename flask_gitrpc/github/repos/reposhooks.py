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
        self.client.user(user), repo), data=msg, msg_type=RepoHook)

  def edit_hook(self, repo, id, name=None, config=None, events=None,
      add_events=None, remove_events=None, active=True, user=None):
    msg = RepoHook(
      name=name,
      config=config,
      active=active,
      events=events or [],
      add_events=add_events or [],
      remove_events=remove_events or [])
    return self.client.patch(
      'repos/%s/%s/hooks/%s' % (
        self.client.user(user), repo, id), data=msg, msg_type=RepoHook)

  def test_hook(self, repo, id, user=None):
    return self.client.post(
      'repos/%s/%s/hooks/%s/test' % (
        self.client.user(user), repo, id))

  def delete_hook(self, repo, id, user=None):
    return self.client.delete(
      'repos/%s/%s/hooks/%s' % (
        self.client.user(user), repo, id))
