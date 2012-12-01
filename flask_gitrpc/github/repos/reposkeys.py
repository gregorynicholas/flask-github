from ..messages import Key

class ReposKeys:
  def __init__(self, client):
    self.client = client

  def list_keys(self, repo, user=None):
    return self.client.get(
      'repos/%s/%s/keys' % (
        self.client.user(user), repo), msg_type=None)

  def get_key(self, repo, id, user=None):
    return self.client.get(
      'repos/%s/%s/keys/%s' % (
        self.client.user(user), repo, id), msg_type=None)

  def create_key(self, repo, title, key, user=None):
    msg = Key(
      title=title,
      key=key)
    return self.client.post(
      'repos/%s/%s/keys' % (
        self.client.user(user), repo), data=msg)

  def edit_key(self, repo, id, title=None, key=None, user=None):
    msg = Key(
      title=title,
      key=key)
    return self.client.patch(
      'repos/%s/%s/keys/%s' % (
        self.client.user(user), repo, id), data=msg)

  def delete_key(self, repo, id, user=None):
    return self.client.delete(
      'repos/%s/%s/keys/%s' % (
        self.client.user(user), repo, id))
