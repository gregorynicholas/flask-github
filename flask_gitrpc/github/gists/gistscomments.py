
class GistsComments:
  def __init__(self, client):
    self.client = client

  def list_gist_comments(self, id):
    return self.client.get('gists/%s/comments' % id)

  def get_gist_comment(self, id):
    return self.client.get('gists/comments/%s' % id)

  def create_gist_comment(self, id, body):
    msg = {
      'body': body
    }
    return self.client.post('gists/%s/comments' % id, msg)

  def edit_gist_comment(self, id, body):
    msg = {
      'body': body
    }
    return self.client.patch('gists/comments/%s' % id, msg)

  def delete_gist_comment(self, id):
    return self.client.delete('gists/comments/%s' % id)
