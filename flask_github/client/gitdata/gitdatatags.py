from __future__ import unicode_literals
from ..messages import User
from ..messages import Tag
from ..requests import TagResponse

class GitDataTags:
  def __init__(self, client):
    self.client = client

  def get(self, repo, sha, user=None):
    return self.client.get(
      'repos/%s/%s/git/tags/%s' % (
        self.client.user(user), repo, sha), msg_type=TagResponse)

  def create(self, repo, tag, message, object, type, tagger_name,
      tagger_email, tagger_date, user=None):
    msg = Tag(
      tag=tag,
      message=message,
      object=object,
      type=type)
    msg.tagger = User(
      name=tagger_name,
      email=tagger_email,
      date=tagger_date)
    return self._create(repo=repo, user=user, msg=msg)

  def _create(self, repo, msg, user=None):
    return self.github.post(
      'repos/%s/%s/git/tags' % (
        self.client.user(user), repo), data=msg, msg_type=TagResponse)
