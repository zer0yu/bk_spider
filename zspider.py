#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zeroyu

import click

from lib.info_feature import *
from lib.guess_sex  import *
from lib.url_manager    import *
from lib.output_manager import *
from lib.mysql_manager import *


#将信息dict存在list里
#return一个存储了info_dict的list
def list_dict(list_url):
    list_d = []
    for list_herf in list_url:
        infos = info(list_herf) #得到一个info的dict
        if infos.has_key('性别'):
            pass
        else:
            try:
                infos['性别'] = GuessSex(infos['中文名'])    #GuessSex猜测性别
            except Exception:
                pass
        list_d.append(infos)
    return list_d

def out_xls(url):
    initialize()    #初始化xls
    lists_herf = herf(url) #返回url_list
    list_dic = list_dict(lists_herf)
    row = 1

    for i in list_dic:
        if i :
            callback(i,row) #callback存入xls
            row = row + 1
        else:
            pass

def out_sql(url):
    lists_herf = herf(url) #返回url_list
    list_dic = list_dict(lists_herf)

    for i in list_dict:
        if i :
            SQLmanager(i) #SQLmanager存入mysql数据库
        else:
            pass

def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('Version 1.0')
    ctx.exit()


@click.command()
@click.option('--version', is_flag=True, callback=print_version,
              expose_value=False, is_eager=True)
@click.option('--count', default=10, help='需要爬取信息的数目'.decode('utf-8'))
@click.option('--obj', type=click.Choice(['sc_zh', 'star_zh','star_korea','em_zh','so_zh','his_zh','vir_w','ec_world','news','athlete','cartoon']),default='sc_zh', help='设置爬虫对象'.decode('utf-8'))
@click.option('--output', type=click.Choice(['xls', 'sql']),default='xls', help='数据输出后保存的位置'.decode('utf-8'))
def main(count,obj,output):
    """\033[01;34m
        \033[01;31m__/\033[01;34m
    ____\033[01;33m/ \033[01;31m__/\033[01;34m
   / __ \ \033[01;33m_/\033[01;34m
  / /_/ / 
  \____/
    \033[01;37m\033[01;m Version 1.0 by zeroyu mail:zeroyu.xyz@gmail.com \033[01;37m\033[0m
    \n"""
    
    if obj == 'sc_zh':
        sc_url = "http://baike.baidu.com/fenlei/%E4%B8%AD%E5%9B%BD%E7%A7%91%E5%AD%A6%E5%AE%B6?limit={}&index=1&offset={}".format(count,count)
        url = sc_url
    elif obj == 'em_zh':
        em_url = "http://baike.baidu.com/fenlei/%E4%B8%AD%E5%9B%BD%E7%9A%87%E5%B8%9D?limit={}&index=1&offset={}".format(count,count)
        url = em_url
    elif obj == 'star_zh':
        star_url = "http://baike.baidu.com/fenlei/%E4%B8%AD%E5%9B%BD%E6%98%8E%E6%98%9F?limit={}&index=1&offset={}".format(count,count)
        url = star_url
    elif obj == 'so_zh':
        soldier_url = "http://baike.baidu.com/fenlei/%E4%B8%AD%E5%9B%BD%E5%86%9B%E4%BA%8B%E4%BA%BA%E7%89%A9?limit={}&index=1&offset={}".format(count,count)
        url = soldier_url
    elif obj == 'his_zh':
        his_url = "http://baike.baidu.com/fenlei/%E5%8E%86%E5%8F%B2%E4%BA%BA%E7%89%A9?limit={}&index=1&offset={}".format(count,count)
        url = his_url
    elif obj == 'star_korea':
        ko_star_url = "http://baike.baidu.com/fenlei/%E9%9F%A9%E5%9B%BD%E6%98%8E%E6%98%9F?limit={}&index=1&offset={}".format(count,count)
        url = ko_star_url
    elif obj == 'vir_w':
        virtual_url = "http://baike.baidu.com/fenlei/%E8%99%9A%E6%8B%9F%E4%BA%BA%E7%89%A9?limit={}&index=1&offset={}".format(count,count)
        url = virtual_url
    elif obj == 'ec_world':
        ec_url = "http://baike.baidu.com/fenlei/%E7%BB%8F%E6%B5%8E%E4%BA%BA%E7%89%A9?limit={}&index=1&offset={}".format(count,count)
        url = ec_url
    elif obj == 'news':
        news_url = "http://baike.baidu.com/fenlei/%E6%96%B0%E9%97%BB%E4%BA%BA%E7%89%A9?limit={}&index=1&offset={}".format(count,count)
        url = news_url
    elif obj == 'athlete':
        athlete_url = "http://baike.baidu.com/fenlei/%E4%BD%93%E8%82%B2%E4%BA%BA%E7%89%A9?limit={}&index=1&offset={}".format(count,count)
        url = athlete_url
    elif obj == 'cartoon':
        cartoon = "http://baike.baidu.com/fenlei/%E5%8A%A8%E6%BC%AB%E4%BA%BA%E7%89%A9?limit={}&index=1&offset={}".format(count,count)
        url = cartoon
    else:
        pass
    
    if output == 'xls':
        out_xls(url)
    elif output == 'sql':
        out_sql(url)
    else:
        pass

if __name__ == '__main__':
    main()