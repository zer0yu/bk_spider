#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zeroyu

import requests
from bs4 import BeautifulSoup

def info(url):
    #返回一个dict来存储
    info_data = {}
    name = []
    info = []

    req = requests.get(url)
    html = req.text

    soup = BeautifulSoup(html,"lxml")
    nodes = soup.find_all('dt', class_='basicInfo-item name')

    for node in nodes:
        name_temp = node.get_text().replace(u'\xa0',u'')    #解决&nbsp;
        name_temp = name_temp.encode('raw_unicode_escape').replace("\n","")
        name.append(name_temp)
    #print name

    info_nodes = soup.find_all('dd', class_='basicInfo-item value')
    for info_node in info_nodes:
        info_temp = info_node.get_text().encode('raw_unicode_escape').replace("\n","")
        info.append(info_temp)
    #print info

    info_data = dict(zip(name,info))    #dict(list)
    #print info_data
    return info_data