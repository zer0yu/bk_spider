#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zeroyu

import ngender

def GuessSex(name):
    sex = ngender.guess(name)
    return sex[0]
