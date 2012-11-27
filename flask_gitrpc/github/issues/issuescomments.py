
class IssuesComments:
  def __init__(self, client):
    self.client = client

  def list_issue_comments(self, repo, id, user=None):
    return self.client.get('repos/%s/%s/issues/%s/comments' % (
      self.client.username(user), repo, id))

  def get_issue_comment(self, repo, id, user=None):
    return self.client.get('repos/%s/%s/issues/comments/%s' % (
      self.client.username(user), repo, id))

  def list_issues(self, repo, id, body, user=None):
    msg = {
      'body': body
    }
    return self.client.post('repos/%s/%s/issues/%s/comments' % (
      self.client.username(user), repo, id), msg)

  def edit_comment(self, repo, id, body, user=None):
    msg = {
      'body': body
    }
    return self.client.patch('repos/%s/%s/issues/comments/%s' % (
      self.client.username(user), repo, id), msg)

  def delete_comment(self, repo, id, user=None):
    return self.client.delete('repos/%s/%s/issues/comments/%s' % (
      self.client.username(user), repo, id))
