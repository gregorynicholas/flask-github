from ..messages import Key

class ReposKeys:
  def __init__(self, client):
    self.client = client

  def list_keys(self, repo, user=None):
    return self.client.get(
      'repos/%s/%s/keys' % (
        self.client.username(user), repo))

  def get_key(self, repo, id, user=None):
    return self.client.get(
      'repos/%s/%s/keys/%s' % (
        self.client.username(user), repo, id))

  def create_key(self, repo, title, key, user=None):
    msg = Key(
      title=title,
      key=key)
    return self.client.post(
      'repos/%s/%s/keys' % (
        self.client.username(user), repo), msg)

  def edit_key(self, repo, id, title=None, key=None, user=None):
    msg = Key(
      title=title,
      key=key)
    return self.client.patch(
      'repos/%s/%s/keys/%s' % (
        self.client.username(user), repo, id), msg)

  def delete_key(self, repo, id, user=None):
    return self.client.delete(
      'repos/%s/%s/keys/%s' % (
        self.client.username(user), repo, id))
