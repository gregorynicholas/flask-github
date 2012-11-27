
class Gists:
  def __init__(self, client):
    self.client = client

  def list_gists(self, user=None):
    url = 'users/%s/gists' % user if user else 'gists'
    return self.client.get(url)

  def list_public_gists(self):
    return self.client.get('gists/public')

  def list_starred_gists(self):
    return self.client.get('gists/starred')

  def get_gist(self, id):
    return self.client.get('gists/%s' % id)

  def create_gist(self, public, files, description=None):
    msg = {
      'description': description,
      'public': public,
      'files': files
    }
    return self.client.post('gists', msg)

  def edit_gist(self, id, files=None, description=None):
    msg = {
      'description': description,
      'files': files
    }
    return self.client.patch('gists/%s' % id, msg)

  def star_gist(self, id):
    return self.client.put('gists/%s/star' % id)

  def unStar_gist(self, id):
    return self.client.delete('gists/%s/star' % id)

  def check_if_gist_starred(self, id):
    return self.client.get('gists/%s/star' % id)

  def fork_gist(self, id):
    return self.client.post('gists/%s/fork' % id)

  def delete_gist(self, id):
    return self.client.delete('gists/%s' % id)
