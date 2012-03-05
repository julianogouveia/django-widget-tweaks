#!/usr/bin/env python
from distutils.core import setup
for cmd in 'egg_info', 'develop':
    import sys
    if cmd in sys.argv:
        from setuptools import setup

version='0.3'

setup(
    name = 'django-widget-tweaks',
    version = version,
    author = 'Mikhail Korobov',
    author_email = 'kmike84@gmail.com',
    url = 'http://bitbucket.org/kmike/django-widget-tweaks/',
    download_url = 'http://bitbucket.org/kmike/django-widget-tweaks/get/tip.zip',

    description = 'Tweak the form field rendering in templates, not in python-level form definitions.',
    long_description = open('README.rst').read(),
    license = 'MIT license',
    requires = ['django (>= 1.2)'],

    packages=['widget_tweaks', 'widget_tweaks.templatetags'],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
