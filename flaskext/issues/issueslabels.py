import json

class IssuesLabels:
    def __init__(self, github):
        self.__github = github

    def listRepoLabels(self, repo, user=None):
        url = 'repos/%s/%s/labels' % (repo, user)
        return self.__github.get(url)

    def getLabel(self, repo, id, user=None):
        url = 'repos/%s/%s/labels/%s' % (repo, user, id)
        return self.__github.get(url)

    def createLabel(self, repo, name, color, user=None):
        params = {
            'name': name,
            'color': color
        }
        data = json.dumps(params)
        url = 'repos/%s/%s/labels' % (repo, user)
        return self.__github.post(url, data)

    def editLabel(self, repo, id, name, color, user=None):
        params = {
            'name': name,
            'color': color
        }
        data = json.dumps(params)
        url = 'repos/%s/%s/labels/%s' % (repo, user, id)
        return self.__github.patch(url, data)

    def deleteLabel(self, repo, id, user=None):
        url = 'repos/%s/%s/labels/%s' % (repo, user, id)
        return self.__github.delete(url)

    def getIssueLabels(self, repo, id, user=None):
        url = 'repos/%s/%s/issues/%s/labels' % (repo, user, id)
        return self.__github.get(url)

    def addIssueLabel(self, repo, id, labels, user=None):
        params = labels
        data = json.dumps(params)
        url = 'repos/%s/%s/issues/%s/labels' % (repo, user, id)
        return self.__github.post(url, data)

    def deleteIssueLabel(self, repo, issue_id, label_id, user=None):
        url = 'repos/%s/%s/issues/%s/labels/%s' % (
            repo, user, issue_id, label_id)
        return self.__github.delete(url)

    def replaceIssueLabels(self, repo, id, labels, user=None):
        params = labels
        data = json.dumps(params)
        url = 'repos/%s/%s/issues/%s/labels' % (repo, user, id)
        return self.__github.put(url, data)

    def removeIssueLabels(self, repo, id, user=None):
        url = 'repos/%s/%s/issues/%s/labels' % (repo, user, id)
        return self.__github.delete(url)

    def getIssueMilestoneLabels(self, repo, id, user=None):
        url = 'repos/%s/%s/milestones/%s/labels' % (repo, user, id)
        return self.__github.get(url)
