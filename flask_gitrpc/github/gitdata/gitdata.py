from gitdatatags import GitDataTags
from gitdatatrees import GitDataTrees
from gitdatablobs import GitDataBlobs
from gitdatacommits import GitDataCommits
from gitdatareferences import GitDataReferences

class GitData:
  def __init__(self, client):
    self.client = client
    self.tags = GitDataTags(self.client)
    self.trees = GitDataTrees(self.client)
    self.blobs = GitDataBlobs(self.client)
    self.commits = GitDataCommits(self.client)
    self.references = GitDataReferences(self.client)
