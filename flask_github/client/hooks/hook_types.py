'''
  :push: Any git push to a Repository.
  :issues: Any time an Issue is opened or closed.
  :issue_comment: Any time an Issue is commented on.
  :commit_comment: Any time a Commit is commented on.
  :pull_request: Any time a Pull Request is opened, closed, or synchronized
     (updated due to a new push in the branch that the pull request
     is tracking).
  :gollum: Any time a Wiki page is updated.
  :watch: Any time a User watches the Repository.
  :download: Any time a Download is added to the Repository.
  :fork: Any time a Repository is forked.
  :fork_apply: Any time a patch is applied to the Repository from the Fork Queue.
  :member: Any time a User is added as a collaborator to a non-Organization Repository.
  :public: Any time a Repository changes from private to public.
  :status: Any time a Repository has a status update from the API
'''
from __future__ import unicode_literals

EVENTS = dict(
  PUSH='push',
  ISSUES='issues',
  ISSUE_COMMENT='issue_comment',
  COMMIT_COMMENT='commit_comment',
  PULL_REQUEST='pull_request',
  GOLLUM='gollum',
  WATCH='watch',
  DOWNLOAD='download',
  FORK='fork',
  FORK_APPLY='fork_apply',
  MEMBER='member',
  PUBLIC='public',
  STATUS='status',
)
