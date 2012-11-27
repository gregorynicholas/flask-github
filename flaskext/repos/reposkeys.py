from ..messages import Key

class ReposKeys:
  def __init__(self, github):
    self.github = github

  def list_keys(self, repo, user=None):
    return self.github.get(
      'repos/%s/%s/keys' % (self.username(user), repo))

  def get_key(self, repo, id, user=None):
    return self.github.get(
      'repos/%s/%s/keys/%s' % (self.username(user), repo, id))

  def create_key(self, repo, title, key, user=None):
    msg = Key()
    msg.title = title
    msg.key = key
    return self.github.post(
      'repos/%s/%s/keys' % (self.username(user), repo), msg)

  def edit_key(self, repo, id, title=None, key=None, user=None):
    msg = Key()
    msg.title = title
    msg.key = key
    return self.github.patch(
      'repos/%s/%s/keys/%s' % (self.username(user), repo, id), msg)

  def delete_key(self, repo, id, user=None):
    return self.github.delete(
      'repos/%s/%s/keys/%s' % (self.username(user), repo, id))

  def username(self, user):
    return self.github.username if user is None else user
