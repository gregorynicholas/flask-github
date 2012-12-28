#!/usr/bin/python
"""
flask-github
--------------

Github API v3 python client built using Google's Protocol Buffers.

http://github.com/gregorynicholas/flask-github
`````

* `documentation <http://packages.python.org/flask-github>`_
* `development version
  <http://github.com/gregorynicholas/flask-github/tarball/master#egg=flask-github-dev>`_

"""
from setuptools import setup

setup(
  name='flask-github',
  version='1.0.0',
  url='http://github.com/gregorynicholas/flask-github',
  license='MIT',
  author='gregorynicholas',
  description=''''Github API v3 python client built using Google's Protocol Buffers.''',
  long_description=__doc__,
  download_url='https://github.com/gregorynicholas/flask-github/tarball/master',
  packages=[
    'flask_github.client',
    'flask_github.client.events',
    'flask_github.client.gists',
    'flask_github.client.gitdata',
    'flask_github.client.issues',
    'flask_github.client.orgs',
    'flask_github.client.pullreqs',
    'flask_github.client.repos',
    'flask_github.client.users',
  ],
  namespace_packages=[
    'flask_github',
  ],
  py_modules=[
    'flask_github.github',
  ],
  zip_safe=False,
  platforms='any',
  install_requires=[
    'flask',
    'flask-oauth',
    'flask-protorpc',
  ],
  dependency_links = [
    'https://github.com/gregorynicholas/flask-protorpc/tarball/master',
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development :: Libraries :: Python Modules'
  ]
)
