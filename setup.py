# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from django_bootstrapr import __version__

setup(
    name='django_bootstrapr',
    version='.'.join(map(str, __version__)),
    author=u'Brandon Ashworth',
    author_email='brandon@brandonashworth.com',
    packages=['django_bootstrapr'],
    url='https://github.com/brandonvfx/django_bootstrapr',
    license='',
    description='A simple app for adding Twitter Bootstrap to your project. Includes 4 base templates from the Bootstrap examples page.',
    zip_safe=False,
    include_package_data=True,
)