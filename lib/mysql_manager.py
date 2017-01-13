#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zeroyu

import MySQLdb

def SQLmanager(dictionary):
    
    list_sql = list_dict(dictionary)   #取出info—字典中的需要的信息组成一个list

    conn= MySQLdb.connect(
        host='127.0.0.1',
        port = 3306,
        user='root',
        passwd='root',
        db ='dbname',
        )

    cur = conn.cursor()

    cur.execute("create table infomation(id int AUTO_INCREMENT,name varchar(50),nationality varchar(50),nation varchar(50),place_of_domicile varchar(50),birthday varchar(50),category varchar(50),graduate_institutions varchar(50),sex varchar(50)")

    sql = "insert into infomation(name,nationality,nation,place_of_domicile,birthday,category,graduate_institutions,sex)values(%s,%s,%s,%s,%s,%s,%s,%s)"
    
    cursor.executemany(sql,list_sql)

    cur.close()
    conn.commit()
    conn.close()

def list_dict(dictionary):
    #传入一个dict,返回一个list
    dict_list = []

    try:
        dict_list.append(dictionary['中文名'].decode('utf-8'))

        if dictionary.has_key('国籍'):
            dict_list.append(dictionary['国籍'].decode('utf-8'))
        else:
            dict_list.append('中国'.decode('utf-8'))

        if dictionary.has_key('民族'):
            dict_list.append(dictionary['民族'].decode('utf-8'))
        else:
            ndict_list.append('汉'.decode('utf-8'))

        if dictionary.has_key('出生地'):
            dict_list.append(dictionary['出生地'].decode('utf-8'))
        else:
            dict_list.append('中华人民共和国'.decode('utf-8'))

        if dictionary.has_key('出生日期'):
            dict_list.append(dictionary['出生日期'].decode('utf-8'))
        else:
            dict_list.append('不详'.decode('utf-8'))

        if dictionary.has_key('职业'):
            dict_list.append(dictionary['职业'].decode('utf-8'))
        else:
            dict_list.append('未知'.decode('utf-8'))

        if dictionary.has_key('毕业院校'):
            dict_list.append(dictionary['毕业院校'].decode('utf-8'))
        else:
            dict_list.append('未知'.decode('utf-8'))
            
        if dictionary['性别'] == 'male':
            dict_list.append('男'.decode('utf-8'))
        elif dictionary['性别'] == 'female':
            dict_list.append('女'.decode('utf-8'))
        else:
            dict_list.append(dictionary['性别'].decode('utf-8'))
    except Exception:
        pass
    
    return dict_list