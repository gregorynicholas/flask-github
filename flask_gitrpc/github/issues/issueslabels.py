
class IssuesLabels:
  def __init__(self, client):
    self.client = client

  def list_repo_labels(self, repo, user=None):
    return self.client.get('repos/%s/%s/labels' % (
      repo, self.client.user(user)), msg_type=None)

  def get_label(self, repo, id, user=None):
    return self.client.get('repos/%s/%s/labels/%s' % (
      repo, self.client.user(user), id), msg_type=None)

  def create_label(self, repo, name, color, user=None):
    msg = {
      'name': name,
      'color': color
    }
    return self.client.post('repos/%s/%s/labels' % (
      repo, self.client.user(user)), msg)

  def edit_label(self, repo, id, name, color, user=None):
    msg = {
      'name': name,
      'color': color
    }
    return self.client.patch('repos/%s/%s/labels/%s' % (
      repo, self.client.user(user), id), msg)

  def delete_label(self, repo, id, user=None):
    return self.client.delete('repos/%s/%s/labels/%s' % (
      repo, self.client.user(user), id))

  def get_issue_labels(self, repo, id, user=None):
    return self.client.get('repos/%s/%s/issues/%s/labels' % (
      repo, self.client.user(user), id), msg_type=None)

  def add_issue_label(self, repo, id, labels, user=None):
    msg = labels
    return self.client.post('repos/%s/%s/issues/%s/labels' % (
      repo, self.client.user(user), id), msg)

  def delete_issue_label(self, repo, issue_id, label_id, user=None):
    return self.client.delete(url = 'repos/%s/%s/issues/%s/labels/%s' % (
      repo, self.client.user(user), issue_id, label_id))

  def replace_issue_labels(self, repo, id, labels, user=None):
    msg = labels
    return self.client.put('repos/%s/%s/issues/%s/labels' % (
      repo, self.client.user(user), id), msg)

  def remove_issue_labels(self, repo, id, user=None):
    return self.client.delete('repos/%s/%s/issues/%s/labels' % (
      repo, self.client.user(user), id))

  def get_issue_milestone_labels(self, repo, id, user=None):
    return self.client.get('repos/%s/%s/milestones/%s/labels' % (
      repo, self.client.user(user), id), msg_type=None)
