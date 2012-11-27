import json

class ReposDownloads:
  def __init__(self, github):
    self.github = github

  def get_downloads(self, repo, user=None):
    return self.github.get(
      'repos/%s/%s/downloads' % (self.username(user), repo))

  def get_download(self, repo, id, user=None):
    return self.github.get(
      'repos/%s/%s/downloads/%s' % (self.username(user), repo, id) )

  def createNew_download(self, repo, name, size, description=None,
      content_type=None, user=None):
    msg = {
      'name': name,
      'size': size,
      'description': description,
      'content_type': content_type
    }
    response = self.github.post(
      'repos/%s/%s/downloads/%s' % (self.username(user), repo, id), msg)
    jresource = json.loads(response)
    # TODO

  def delete_download(self, repo, id, user=None):
    return self.github.delete(
      'repos/%s/%s/downloads/%s' % (self.username(user), repo, id))

  def username(self, user):
    return self.github.username if user is None else user
