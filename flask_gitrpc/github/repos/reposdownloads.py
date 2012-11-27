import json

class ReposDownloads:
  def __init__(self, client):
    self.client = client

  def get_downloads(self, repo, user=None):
    return self.client.get(
      'repos/%s/%s/downloads' % (
        self.client.username(user), repo))

  def get_download(self, repo, id, user=None):
    return self.client.get(
      'repos/%s/%s/downloads/%s' % (
        self.client.username(user), repo, id))

  def create_new_download(self, repo, name, size, description=None,
      content_type=None, user=None):
    msg = {
      'name': name,
      'size': size,
      'description': description,
      'content_type': content_type
    }
    response = self.client.post(
      'repos/%s/%s/downloads/%s' % (
        self.client.username(user), repo, id), msg)
    data = json.loads(response)
    return data
    # TODO

  def delete_download(self, repo, id, user=None):
    return self.client.delete(
      'repos/%s/%s/downloads/%s' % (
        self.client.username(user), repo, id))
