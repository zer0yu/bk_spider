#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zeroyu

import xlwt;
import xlrd;
from xlutils.copy import copy;

def initialize():
    file = xlwt.Workbook(encoding = 'utf-8')   
    #指定file以utf-8的格式打开
    table = file.add_sheet('info')           
    #指定打开的文件名

    col = 0

    datas = ['姓名','国籍','民族','户籍地','出生年月日','职业类别','毕业院校','性别','血型','配偶',
            '别名(别号)','身高','儿女','英文名','体重','所处朝代','婚姻状态','学历','籍贯',
            '政治面貌','学位','居住地','宗教信仰','专业']  #只要性别之前的信息

    for data in datas:
        table.write(0, col, data)
        col = col + 1

    file.save('infomations.xls')

def callback(dictionary,rows):
#传入爬取的dict
#open existed xls file
#newWb = xlutils.copy(fileName);
#newWb = copy(fileName);
    oldWb = xlrd.open_workbook('infomations.xls', formatting_info=True)
    newWb = copy(oldWb)
    newWs = newWb.get_sheet(0) #获取第一个表名
    try:
        newWs.write(rows, 0, dictionary['中文名'].decode('utf-8'))

        if dictionary.has_key('国籍'):
            newWs.write(rows, 1, dictionary['国籍'].decode('utf-8'))
        else:
            newWs.write(rows, 1, '中国'.decode('utf-8'))

        if dictionary.has_key('民族'):
            newWs.write(rows, 2, dictionary['民族'].decode('utf-8'))
        else:
            newWs.write(rows, 2, '汉'.decode('utf-8'))

        if dictionary.has_key('出生地'):
            newWs.write(rows, 3, dictionary['出生地'].decode('utf-8'))
        else:
            newWs.write(rows, 3, '中华人民共和国'.decode('utf-8'))

        if dictionary.has_key('出生日期'):
            newWs.write(rows, 4, dictionary['出生日期'].decode('utf-8'))
        else:
            newWs.write(rows, 4, '不详'.decode('utf-8'))

        if dictionary.has_key('职业'):
            newWs.write(rows, 5, dictionary['职业'].decode('utf-8'))
        else:
            newWs.write(rows, 5,'未知'.decode('utf-8'))

        if dictionary.has_key('毕业院校'):
            newWs.write(rows, 6, dictionary['毕业院校'].decode('utf-8'))
        else:
            newWs.write(rows, 6, '未知'.decode('utf-8'))
            
        if dictionary['性别'] == 'male':
            newWs.write(rows, 7, '男'.decode('utf-8'))
        elif dictionary['性别'] == 'female':
            newWs.write(rows, 7, '女'.decode('utf-8'))
        else:
            newWs.write(rows, 7, dictionary['性别'].decode('utf-8'))

        print "write new values ok"
        newWb.save('infomations.xls')
        print "save with same name ok"
    except Exception:
        pass
