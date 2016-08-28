#!/usr/bin/env python
'''
PyPI setup.py file
'''

from distutils.core import setup

ver = '0.1.1'

setup(name='couchpotato',
      packages=['couchpotato'],
      version=ver,
      description='Module for lazily evaluating Python functions',
      author='Buck Baskin',
      author_email='mobile.wbaskin+pypi@gmail.com',
      url='https://github.com/buckbaskin/couchpotato',
      download_url='https://github.com/buckbaskin/couchpotato/tarball/%s' % ver,
      keywords=['couchpotato', 'lazy'],
      classifiers=[],)
