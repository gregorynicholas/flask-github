import json

class IssuesComments:
    def __init__(self, github):
        self.__github = github

    def listIssueComments(self, repo, id, user=None):
        url = 'repos/%s/%s/issues/%s/comments' % (user, repo, id)
        return self.__github.get(url)

    def getIssueComment(self, repo, id, user=None):
        url = 'repos/%s/%s/issues/comments/%s' % (user, repo, id)
        return self.__github.get(url)

    def listIssues(self, repo, id, body, user=None):
        params = {
            'body': body
        }
        data = json.dumps(params)
        url = 'repos/%s/%s/issues/%s/comments' % (user, repo, id)
        return self.__github.post(url, data)

    def editComment(self, repo, id, body, user=None):
        params = {
            'body': body
        }
        data = json.dumps(params)
        url = 'repos/%s/%s/issues/comments/%s' % (user, repo, id)
        return self.__github.patch(url, data)

    def deleteComment(self, repo, id, user=None):
        url = 'repos/%s/%s/issues/comments/%s' % (user, repo, id)
        return self.__github.delete(url)