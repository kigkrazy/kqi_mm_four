#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import random
import time

import requests


def selectAPPS():
    # 11到36
    soft_sortdetail_v1 = {'影音工具': '678936512', '社区交友': '678936511', '系统工具': '678936514', '网络视频': '678936530',
                          '网络购物': '678936527','摄影录像':'678936523','安全防护':'678936516','报刊杂志':'678936534','餐饮美食':'678936536',
                          '电子书籍': '678936519','儿童应用':'678936532','健康医疗':'678936528','交通导航':'678936522','教育教学':'678936525',
                          '金融理财': '678936531','卡通动漫':'678936535','浏览器':'678936515','旅游出行':'678936524','美化壁纸':'678936517',
                          '商务办公': '678936526','生活助手':'678936513','输入法':'678936520','数字音乐':'678936533','通话通信':'678936521',
                          '新闻资讯': '678936529','娱乐八卦':'678936518'}
    # url_first = "http://odp.mmarket.com/t.do?requestid=soft_sortdetail_v1"
    # url_first = "http://odp.mmarket.com/t.do?requestid=soft_sortdetail_v1&sortid={param}&needNewActivity=true&defaultType=1&seqtype=hotlist"
    url_first = "http://odp.mmarket.com/t.do?requestid=soft_sortdetail_v1&sortid={param}&needNewActivity=true&defaultType=1&seqtype=hotlist"
    headers = {'appname': 'MM6.5.1.001.01_CTAndroid_JT', 'ua': 'android-19-720x1280-VIVO XPLAY6',
               'User-Agent': 'android-19-720x1280-VIVO XPLAY6'}

    # index = random.randint(0, len(soft_sortdetail_v1.keys()) - 1)
    for index in range(0, len(soft_sortdetail_v1.keys())):
        print("-------------  "+str(index)+"  ----------------")
        real_url = url_first.format(param=list(soft_sortdetail_v1.values())[index])
        print(real_url)
        try:
            result_str = requests.get(url=real_url, headers=headers)

            items = result_str.json()['items']

            for i in range(len(items)):
                # self.test_apps.append(items[i]['name'])
                print(items[i]['name'])
                print(items[i]['appSize'])

        except Exception:
            print("异常")
            return 'false'


if __name__ == '__main__':
    # selectAPPS()
    screenShot("test")