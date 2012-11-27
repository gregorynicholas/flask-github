from ..messages import User
from ..messages import Tag
from ..messages import TagsResponse as Response

class GitDataTags:
  def __init__(self, github):
    self.github = github

  def get_tag(self, repo, sha, user=None):
    return self.github.get(
      'repos/%s/%s/git/tags/%s' % (self.username(user), repo, sha), Response)

  def create_tag(self, repo, tag, message, object, type, tagger_name,
      tagger_email, tagger_date, user=None):
    msg = Tag()
    msg.tag = tag
    msg.message = message
    msg.object = object
    msg.type = type
    msg.tagger = User()
    msg.tagger.name = tagger_name
    msg.tagger.name = tagger_email
    msg.tagger.date = tagger_date
    return self.github.post(
      'repos/%s/%s/git/tags' % (
        user, repo) % (self.username(user), repo), msg, Response)

  def username(self, user):
    return self.github.username if user is None else user
