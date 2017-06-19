#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Herman Tong'
SITENAME = u"Herman's Website"
SITEURL = ''
#SITEURL = 'http://tkherman.github.io'

PATH = 'content'
THEME = './pelican-blue'
TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Social widget
SOCIAL = (('github', 'http://github.com/tkherman'),
          ('linkedin', 'https://www.linkedin.com/in/herman-tong-b582b057'),)

DEFAULT_PAGINATION = False

SIDEBAR_DIGEST = 'Junior in Computer Science at Notre Dame'
MENUITEMS = (('About me', SITEURL), 
            ('Projects', SITEURL + '/pages/projects.html'),
            ('Blog', SITEURL + '/category/blog.html',))

STATIC_PATHS = ['images']

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
