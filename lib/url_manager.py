#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zeroyu

import requests
import re

#返回一个info的list
def herf(url):
    info_url = []

    req = requests.get(url)
    html = req.text
    url_re = re.compile(r'<a class="title nslog:7450" href="(.+?)" (rel|title|target)')
    for i in re.findall(url_re,html):
        info_herf = 'http://baike.baidu.com'+i[0]
        print info_herf
        info_url.append(info_herf)
    return info_url