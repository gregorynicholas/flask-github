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
  name='flask_gitrpc',
  version='1.0.0',
  url='http://github.com/gregorynicholas/flask-gitrpc',
  license='MIT',
  author='gregorynicholas',
  description='Protocol Buffers for the Github API.',
  long_description=__doc__,
  packages=[
    'flask_gitrpc'
    'flask_gitrpc.github'
  ],
  namespace_packages=[
    'flask_gitrpc'
  ],
  py_modules=[
    'flask_gitrpc.gitrpc',
  ],
  zip_safe=False,
  platforms='any',
  install_requires=['flask', 'flask-oauth', 'flask_protorpc'],
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



from distutils import core

core.setup(
  name='gitrpc',
  version='0.1.1',
  author='Gregory Nicholas',
  description='',
  url='https://github.com/gregorynicholas/gitrpc',
  packages=[
    'gitrpc',
    'gitrpc.events',
    'gitrpc.gists',
    'gitrpc.gitdata',
    'gitrpc.issues',
    'gitrpc.orgs',
    'gitrpc.pullreqs',
    'gitrpc.repos',
    'gitrpc.users',
  ],
  py_modules=[
    'gitrpc.client',
    'gitrpc.config',
    'gitrpc.github',
    'gitrpc.messages',
  ],
  install_requires=[
    'requests',
    # -e git@github.com:gregorynicholas/google-protorpc.git#egg=protorpc
    'google-protorpc',
  ]
)
