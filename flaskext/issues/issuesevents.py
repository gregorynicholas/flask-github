class IssuesEvents:
    def __init__(self, github):
        self.__github = github

    def listIssueEvents(self, repo, issue_id, user=None):
        url = 'repos/%s/%s/issues/%s/events' % (user, repo, issue_id)
        return self.__github.get(url)

    def listRepoIssueEvents(self, repo, user=None):
        url = 'repos/%s/%s/issues/events' % (user, repo)
        return self.__github.get(url)

    def getEvent(self, repo, id, user=None):
        url = 'repos/%s/%s/issues/events/%s' % (user, repo, id)
        return self.__github.get(url)