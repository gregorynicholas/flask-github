#!/usr/bin/python
"""
flask_gitrpc
--------------

Protocol Buffers for the Github API.

http://github.com/gregorynicholas/flask_gitrpc
`````

* `documentation <http://packages.python.org/flask_gitrpc>`_
* `development version
  <http://github.com/gregorynicholas/flask_gitrpc/zipball/master#egg=flask_gitrpc-dev>`_

"""
from setuptools import setup

setup(
  name='flask-gitrpc',
  version='1.0.0',
  url='http://github.com/gregorynicholas/flask-gitrpc',
  license='MIT',
  author='gregorynicholas',
  description='Protocol Buffers for the Github API.',
  long_description=__doc__,
  packages=[
    'flask_gitrpc.github',
    'flask_gitrpc.github.events',
    'flask_gitrpc.github.gists',
    'flask_gitrpc.github.gitdata',
    'flask_gitrpc.github.issues',
    'flask_gitrpc.github.orgs',
    'flask_gitrpc.github.pullreqs',
    'flask_gitrpc.github.repos',
    'flask_gitrpc.github.users',
  ],
  namespace_packages=[
    'flask_gitrpc',
  ],
  py_modules=[
    'flask_gitrpc.gitrpc',
  ],
  zip_safe=False,
  platforms='any',
  install_requires=['flask', 'flask-oauth', 'flask-protorpc'],
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
