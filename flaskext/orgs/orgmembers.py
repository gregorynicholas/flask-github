
class OrgMembers:
  def __init__(self, github):
    self.github = github

  def list_members(self, org):
    return self.github.get(
      'orgs/%s/members' % org)

  def getMember(self, org, user=None):
    return self.github.get(
      'orgs/%s/members/%s' % (org, self.username(user)))

  def removeMember(self, org, user):
    return self.github.delete(
      'orgs/%s/members/%s' % (org, self.username(user)))

  def listPublic_members(self, org):
    return self.github.get(
      'orgs/%s/public_members' % org)

  def getIfUserIsPublic(self, org, user):
    return self.github.get(
      'orgs/%s/public_members/%s' % (org, self.username(user)))

  def publicizeUser(self, org, user):
    return self.github.put(
      'orgs/%s/public_members/%s' % (org, self.username(user)))

  def concealUser(self, org, user):
    return self.github.delete(
      'orgs/%s/public_members/%s' % (org, self.username(user)))

  def username(self, user):
    return self.github.username if user is None else user
