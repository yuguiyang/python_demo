# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 10:40:45 2017

@author: yuguiyang
"""

import http.cookiejar, urllib.request

cookie = http.cookiejar.MozillaCookieJar('cookie.txt')
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)