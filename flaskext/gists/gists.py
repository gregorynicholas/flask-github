import json

class Gists:
  def __init__(self, github):
    self.__github = github

  def listGists(self, user=None):
    url = 'users/%s/gists' % user if user else 'gists'
    return self.__github.get(url)

  def listPublicGists(self):
    return self.__github.get('gists/public')

  def listStarredGists(self):
    return self.__github.get('gists/starred')

  def getGist(self, id):
    return self.__github.get('gists/%s' % id)

  def createGist(self, public, files, description=None):
    params = {
      'description': description,
      'public': public,
      'files': files
    }
    params = self.__github.__removeEmptyParams(params)
    data = json.dumps(params)
    return self.__github.post('gists', data)

  def editGist(self, id, files=None, description=None):
    params = {
      'description': description,
      'files': files
    }
    params = self.__github.__removeEmptyParams(params)
    data = json.dumps(params)
    return self.__github.patch('gists/%s' % id, data)

  def starGist(self, id):
    return self.__github.put('gists/%s/star' % id)

  def unStarGist(self, id):
    return self.__github.delete('gists/%s/star' % id)

  def checkIfGistStarred(self, id):
    return self.__github.get('gists/%s/star' % id)

  def forkGist(self, id):
    return self.__github.post('gists/%s/fork' % id)

  def deleteGist(self, id):
    return self.__github.delete('gists/%s' % id)