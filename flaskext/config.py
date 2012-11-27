from base.cache.properties import cached

class APIConfig:
  name = 'github'
  api_key = ''
  api_secret = ''
  base_url = 'https://api.github.com/'
  authorize_url = 'https://github.com/login/oauth/authorize'
  access_token_url = 'https://github.com/login/oauth/access_token'
  request_token_url = None
  read_scope = ['user', 'public_repo', 'repo', 'repo:status', 'delete_repo',
  'notifications']
  write_scope = ['gist']

  def __init__(self, user=None):
    self.user = user

  @cached
  def scope(self):
    r_value = ','.join([s for s in self.read_scope])
    w_value = ','.join([s for s in self.write_scope])
    return r_value + ',' + w_value

  def __str__(self):
    return '''<APIConfig::
  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s>''' % (
      self.name, self.api_key, self.api_secret, self.base_url,
      self.authorize_url, self.access_token_url, self.request_token_url,
      self.read_scope, self.write_scope)
