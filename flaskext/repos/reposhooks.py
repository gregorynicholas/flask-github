from ..messages import RepoHookRequest

class ReposHooks:
  def __init__(self, github):
    self.github = github

  def list_hooks(self, repo, user=None):
    return self.github.get(
      'repos/%s/%s/hooks' % (self.username(user), repo))

  def get_hook(self, repo, id, user=None):
    return self.github.get(
      'repos/%s/%s/hooks/%s' % (self.username(user), repo, id))

  def create_hook(self, repo, name, config, events=None, active=True, user=None):
    msg = RepoHookRequest()
    msg.name = name,
    msg.config = config,
    msg.events = events,
    msg.active = active
    return self.github.post(
      'repos/%s/%s/hooks' % (self.username(user), repo), msg)

  def edit_hook(self, repo, id, name, config, events=None, add_events=None,
      remove_events=None, active=True, user=None):
    msg = RepoHookRequest()
    msg.name = name,
    msg.config = config,
    msg.events = events,
    msg.active = active
    msg.add_events = add_events
    msg.remove_events = remove_events
    return self.github.patch(
      'repos/%s/%s/hooks/%s' % (self.username(user), repo, id), msg)

  def test_hook(self, repo, id, user=None):
    return self.github.post(
      'repos/%s/%s/hooks/%s/test' % (self.username(user), repo, id))

  def delete_hook(self, repo, id, user=None):
    return self.github.delete(
      'repos/%s/%s/hooks/%s' % (self.username(user), repo, id))

  def username(self, user):
    return self.github.username if user is None else user
