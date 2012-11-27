import json
import urllib

class IssuesMilestones:
    def __init__(self, github):
        self.__github = github

    def listRepoMilestones(self, repo, state=None, sort=None, direction=None,
                           user=None):
        params = {
            'state': state,
            'sort': sort,
            'direction': direction,
            }
        params = self.__github.__removeEmptyParams(params)
        url = 'repos/%s/%s/milestones?%s' % (
            user, repo, urllib.urlencode(params))
        return self.__github.get(url)

    def getMilestone(self, repo, number, user=None):
        url = 'repos/%s/%s/milestones/%s' % (repo, user, number)
        return self.__github.get(url)

    def createMilestone(self, repo, title, state=None, description=None,
                        due_on=None, user=None):
        params = {
            'title': title,
            'state': state,
            'description': description,
            'due_on': due_on
        }
        params = self.__github.__removeEmptyParams(params)
        data = json.dumps(params)
        url = 'repos/%s/%s/milestones' % (repo, user)
        return self.__github.post(url, data)

    def updateMilestone(self, repo, number, title, state=None, description=None
    , due_on=None, user=None):
        params = {
            'title': title,
            'state': state,
            'description': description,
            'due_on': due_on
        }
        params = self.__github.__removeEmptyParams(params)
        data = json.dumps(params)
        url = 'repos/%s/%s/milestones/%s' % (repo, user, number)
        return self.__github.patch(url, data)

    def deleteMilestone(self, repo, number, user=None):
        url = 'repos/%s/%s/milestones/%s' % (repo, user, number)
        return self.__github.delete(url)