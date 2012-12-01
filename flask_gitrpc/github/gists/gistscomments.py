
class GistsComments:
  def __init__(self, client):
    self.client = client

  def list_gist_comments(self, id):
    return self.client.get(
      'gists/%s/comments' % id, msg_type=None)

  def get_gist_comment(self, id):
    return self.client.get(
      'gists/comments/%s' % id, msg_type=None)

  def create_gist_comment(self, id, body):
    msg = {
      'body': body
    }
    return self.client.post(
      'gists/%s/comments' % id, data=msg)

  def edit_gist_comment(self, id, body):
    msg = {
      'body': body
    }
    return self.client.patch(
      'gists/comments/%s' % id, data=msg)

  def delete_gist_comment(self, id):
    return self.client.delete(
      'gists/comments/%s' % id)
