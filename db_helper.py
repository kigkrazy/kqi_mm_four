#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import traceback
import pymysql as MySQLdb
# import MySQLdb

import datetime
# -*- coding: UTF-8 -*-
def insert_data(table_name,data_dict):

    try:

        data_values = "(" + "%s," * (len(data_dict)) + ")"
        data_values = data_values.replace(',)', ')')

        dbField = data_dict.keys()
        dataTuple = tuple(data_dict.values())
        dbField = str(tuple(dbField)).replace("'",'')

        # conn = MySQLdb.connect("127.0.0.1", "root", "root", "kqi_db", charset='utf8')
        conn = MySQLdb.connect("192.168.3.101", "root", "root", "kqi_db", charset='utf8')
        print("数据库连接")
        print(conn)
        cursor = conn.cursor()

        sql = """ insert into %s %s values %s """ % (table_name,dbField,data_values)
        params = dataTuple
        cursor.execute(sql, params)
        conn.commit()
        cursor.close()

    except Exception:
        print("数据库连接异常")
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback)
        return 'false'

    return 'OK'

def test_insert_data():

    table_name = "mm_2018"
    # 插入的数据
    data_dict = {

        "product_name": "MM",
        "client": "android",
        "bussiness": "search",
        "data_type": "time_delay",
        "data_value": "1.75",
        "network": "wifi",
        "remark": "",
        "test_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    # insert_data(table_name, data_dict)
    result = insert_data(table_name, data_dict)
    print (result)


if __name__ == '__main__':
    test_insert_data()
