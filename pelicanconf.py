#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Nikhil Kalige'
SITENAME = u'Pelican Plugins'
SITEURL = ''

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'templates'
DEFAULT_DATE = 'fs'
DIRECT_TEMPLATES = ['index']
PAGINATED_DIRECT_TEMPLATES = []
#TYPOGRIFY = True
STATIC_PATHS = [
    'images',
    'extras'
    ]
EXTRA_PATH_METADATA = {
    'extras/htaccess': {'path': '.htaccess'},
    }
