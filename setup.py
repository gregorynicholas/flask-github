#!/usr/bin/env python
"""
flask-github
~~~~~~~~~~~~

github api v3 python client built using google's protocol buffers.


links:
``````

* `docs: <http://gregorynicholas.github.io/flask-github>`_
* `source: <http://github.com/gregorynicholas/flask-github>`_
* `package: <http://packages.python.org/flask-github>`_
* `travis-ci: <http://travis-ci.org/gregorynicholas/flask-github>`_
* `issues: <http://github.com/gregorynicholas/flask-github/issues>`_
* `development version: <http://github.com/gregorynicholas/flask-github/zipball/master#egg=flask-github-dev>`_

"""
try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

from os import path, listdir
import fnmatch as fm
import re


# parse version number
with open('flask_github/__init__.py', 'r') as f:
  v = re.findall(r'__version__\s*=\s*\'(.*)\'', f.read())
  __version__ = v[0]

with open("requirements.txt", "r") as f:
  requires = f.readlines()


setup(
  name='flask-github',
  version=__version__,
  url='http://github.com/gregorynicholas/flask-github',
  author='gregorynicholas',
  author_email='gn@gregorynicholas.com',

  description='github api v3 python client built using google protocol buffers.',
  long_description=__doc__,

  install_requires=requires,

  scripts=[
  ],

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
    # 'flask_github',
  ],

  py_modules=[
    # 'flask_github.github',
  ],

  test_suite='nose.collector',
  tests_require=[
    'flask-funktional',
    'nose',
    'nose-cov',
    'mock',
  ],

  dependency_links = [
    'https://github.com/gregorynicholas/flask-protorpc/tarball/master',
  ],
  license='MIT',
  zip_safe=False,
  platforms='any',
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
