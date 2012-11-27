import json

class GistsComments:
  def __init__(self, github):
    self.__github = github

  def listGistComments(self, id):
    return self.__github.get('gists/%s/comments' % id)

  def getGistComment(self, id):
    return self.__github.get('gists/comments/%s' % id)

  def createGistComment(self, id, body):
    params = {
      'body': body
    }
    data = json.dumps(params)
    return self.__github.post('gists/%s/comments' % id, data)

  def editGistComment(self, id, body):
    params = {
      'body': body
    }
    data = json.dumps(params)
    return self.__github.patch('gists/comments/%s' % id, data)

  def deleteGistComment(self, id):
    return self.__github.delete('gists/comments/%s' % id)
