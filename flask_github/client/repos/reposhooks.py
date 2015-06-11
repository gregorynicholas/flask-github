from __future__ import unicode_literals
from ..messages import Hook, HookConfig
from ..requests import HookResponse
from ..requests import HookTestResponse
from ..requests import HookListResponse

class ReposHooks:
  def __init__(self, client):
    self.client = client

  def list(self, repo, user=None):
    return self.client.get(
      'repos/%s/%s/hooks' % (
        self.client.user(user), repo), msg_type=HookListResponse)

  def get(self, repo, id, user=None):
    return self.client.get(
      'repos/%s/%s/hooks/%s' % (
        self.client.user(user), repo, id), msg_type=HookResponse)

  def create(self, repo, name, url, events=None, active=True,
      user=None):
    msg = Hook(
      name=name,
      config=HookConfig(
        url=url),
      events=events,
      active=active)
    return self._create(repo=repo, msg=msg, user=user)

  def _create(self, repo, msg, user=None):
    return self.client.post(
      'repos/%s/%s/hooks' % (
        self.client.user(user), repo), data=msg, msg_type=HookResponse)

  def edit(self, repo, id, name=None, config=None, events=None,
      add_events=None, remove_events=None, active=True, user=None):
    msg = Hook(
      name=name,
      config=config,
      active=active,
      events=events or [],
      add_events=add_events or [],
      remove_events=remove_events or [])
    return self._edit(repo=repo, msg=msg, user=user)

  def _edit(self, repo, msg, user=None):
    return self.client.patch(
      'repos/%s/%s/hooks/%s' % (
        self.client.user(user), repo, id), data=msg, msg_type=HookResponse)

  def test(self, repo, id, user=None):
    return self.client.post(
      'repos/%s/%s/hooks/%s/test' % (
        self.client.user(user), repo, id))

  def delete(self, repo, id, user=None):
    return self.client.delete(
      'repos/%s/%s/hooks/%s' % (self.client.user(user), repo, id))
