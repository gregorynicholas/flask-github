from gitdatablobs import GitDataBlobs
from gitdatacommits import GitDataCommits
from gitdatareferences import GitDataReferences
from gitdatatags import GitDataTags
from gitdatatrees import GitDataTrees

class GitData:
  def __init__(self, github):
    self.github = github
    self.blobs = GitDataBlobs(self.github)
    self.commits = GitDataCommits(self.github)
    self.references = GitDataReferences(self.github)
    self.tags = GitDataTags(self.github)
    self.trees = GitDataTrees(self.github)

  def username(self, user):
    return self.github.username if user is None else user
