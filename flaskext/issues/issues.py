import json
import urllib
from issuescomments import IssuesComments
from issuesevents import IssuesEvents
from issueslabels import IssuesLabels
from issuesmilestones import IssuesMilestones

class Issues:
    def __init__(self, github):
        self.__github = github
        self.comments = IssuesComments(self.__github)
        self.events = IssuesEvents(self.__github)
        self.labels = IssuesLabels(self.__github)
        self.milestones = IssuesMilestones(self.__github)

    def listIssues(self, filter='assigned', state='open', labels=None,
                   sort='created', direction='desc', since=None):
        params = {
            'filter': filter,
            'state': state,
            'labels': labels,
            'sort': sort,
            'direction': direction,
            'since': since
        }
        params = self.__github.__removeEmptyParams(params)
        url = 'issues?%s' % urllib.urlencode(params)
        return self.__github.get(url)

    def listRepoIssues(self, repo, milestone=None, assignee=None,
                       mentioned=None, state='open', labels=None,
                       sort='created', direction='desc', since=None,
                       user=None):
        params = {
            'state': state,
            'assignee': assignee,
            'mentioned': mentioned,
            'labels': labels,
            'sort': sort,
            'direction': direction,
            'since': since,
            'milestone': milestone
        }
        params = self.__github.__removeEmptyParams(params)
        url = 'repos/%s/%s/issues?%s' % (
            user, repo, urllib.urlencode(params))
        return self.__github.get(url)

    def getIssue(self, repo, number, user=None):
        username = self.__github.username if user is None else user
        return self.__github.get(
            'repos/%s/%s/issues/%s' % (username, repo, number))

    def createIssue(self, repo, title, body=None, assignee=None,
                    milestone=None, labels=None, user=None):
        params = {
            'title': title,
            'body': body,
            'assignee': assignee,
            'milestone': milestone,
            'labels': labels
        }
        params = self.__github.__removeEmptyParams(params)
        data = json.dumps(params)
        return self.__github.post('repos/%s/%s/issues' % (user, repo), data)

    def editIssue(self, repo, id, title=None, body=None, assignee=None,
                  state=None, milestone=None, labels=None,
                  user=None):
        username = self.__github.username if user is None else user
        params = {
            'title': title,
            'body': body,
            'assignee': assignee,
            'state': state,
            'milestone': milestone,
            'labels': labels
        }
        params = self.__github.__removeEmptyParams(params)
        data = json.dumps(params)
        return self.__github.post(
            'repos/%s/%s/issues/%s' % (username, repo, id), data)

    