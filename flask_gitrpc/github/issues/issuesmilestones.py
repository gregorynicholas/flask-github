import urllib

class IssuesMilestones:
  def __init__(self, client):
    self.client = client

  def list_repo_milestones(self, repo, state=None, sort=None, direction=None,
      user=None):
    params = {
      'state': state,
      'sort': sort,
      'direction': direction}
    return self.client.get('repos/%s/%s/milestones?%s' % (
      self.client.username(user), repo, urllib.urlencode(params)))

  def get_milestone(self, repo, number, user=None):
    return self.client.get('repos/%s/%s/milestones/%s' % (repo, user, number))

  def create_milestone(self, repo, title, state=None, description=None,
      due_on=None, user=None):
    msg = {
      'title': title,
      'state': state,
      'description': description,
      'due_on': due_on
    }
    return self.client.post('repos/%s/%s/milestones' % (
      repo, self.client.username(user)), msg)

  def update_milestone(self, repo, number, title, state=None, description=None,
      due_on=None, user=None):
    msg = {
      'title': title,
      'state': state,
      'description': description,
      'due_on': due_on
    }
    return self.client.patch('repos/%s/%s/milestones/%s' % (
      repo, self.client.username(user), number), msg)

  def delete_milestone(self, repo, number, user=None):
    return self.client.delete('repos/%s/%s/milestones/%s' % (
      repo, self.client.username(user), number))
