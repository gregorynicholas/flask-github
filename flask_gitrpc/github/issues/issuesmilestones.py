
class IssuesMilestones:
  def __init__(self, client):
    self.client = client

  def list(self, repo, state=None, sort=None, direction=None, user=None):
    query = {
      'state': state,
      'sort': sort,
      'direction': direction}
    return self.client.get('repos/%s/%s/milestones' % (
      self.client.user(user), repo), query=query, msg_type=None)

  def get(self, repo, number, user=None):
    return self.client.get('repos/%s/%s/milestones/%s' % (
      repo, user, number), msg_type=None)

  def create(self, repo, title, state=None, description=None,
      due_on=None, user=None):
    msg = {
      'title': title,
      'state': state,
      'description': description,
      'due_on': due_on
    }
    return self.client.post('repos/%s/%s/milestones' % (
      repo, self.client.user(user)), data=msg)

  def update(self, repo, number, title, state=None, description=None,
      due_on=None, user=None):
    msg = {
      'title': title,
      'state': state,
      'description': description,
      'due_on': due_on
    }
    return self.client.patch('repos/%s/%s/milestones/%s' % (
      repo, self.client.user(user), number), data=msg)

  def delete(self, repo, number, user=None):
    return self.client.delete('repos/%s/%s/milestones/%s' % (
      repo, self.client.user(user), number))
