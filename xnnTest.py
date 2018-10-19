import os
import random
import sys
import traceback

import requests

from attr import attrs


def selectAPPS():
    # soft_sortdetail_v1 = {'影音工具': '678936512' , '系统工具': '678936514', '网络视频': '678936530', '安全防护': '678936516', '报刊杂志': '678936534'}
    # soft_page_v1 = {'影音工具': 29, '系统工具': 4, '网络视频': 15, '安全防护': 2, '报刊杂志': 4}
    soft_sortdetail_v1 = {'影音工具': '678936512', '社区交友': '678936511', '系统工具': '678936514', '网络视频': '678936530',
                          '网络购物': '678936527', '摄影录像': '678936523', '安全防护': '678936516', '报刊杂志': '678936534',
                          '餐饮美食': '678936536', '电子书籍': '678936519', '儿童应用': '678936532', '健康医疗': '678936528',
                          '交通导航': '678936522', '教育教学': '678936525','金融理财': '678936531', '卡通动漫': '678936535',
                          '浏览器': '678936515', '旅游出行': '678936524', '美化壁纸': '678936517', '商务办公': '678936526',
                          '生活助手': '678936513', '输入法': '678936520', '数字音乐': '678936533','通话通信': '678936521',
                          '新闻资讯': '678936529', '娱乐八卦': '678936518'}
    soft_totalRows_v1 = {'影音工具': 299, '社区交友': 139, '系统工具': 40, '网络视频': 165,
                          '网络购物': 110, '摄影录像': 55, '安全防护': 32, '报刊杂志': 42,
                          '餐饮美食': 22, '电子书籍': 244, '儿童应用': 263, '健康医疗': 89,
                          '交通导航': 28, '教育教学': 50, '金融理财': 183, '卡通动漫': 37,
                          '浏览器': 24, '旅游出行': 62, '美化壁纸': 175, '商务办公': 400,
                          '生活助手': 300, '输入法': 10, '数字音乐': 38, '通话通信': 82,
                          '新闻资讯': 90, '娱乐八卦': 111}

    soft_page_v1 = {'影音工具': 20, '社区交友': 14, '系统工具': 4, '网络视频': 6,
                         '网络购物': 10, '摄影录像': 6, '安全防护': 4, '报刊杂志': 5,
                         '餐饮美食': 3, '电子书籍': 20, '儿童应用': 15, '健康医疗': 7,
                         '交通导航': 3, '教育教学': 3, '金融理财': 15, '卡通动漫': 2,
                         '浏览器': 3, '旅游出行': 7, '美化壁纸': 15, '商务办公': 46,
                         '生活助手': 5, '输入法': 1, '数字音乐': 2, '通话通信': 5,
                         '新闻资讯': 5, '娱乐八卦': 5}
    # soft_page_v1 = {'影音工具': 29, '社区交友': 14, '系统工具': 4, '网络视频': 6,
    #                 '网络购物': 10, '摄影录像': 6, '安全防护': 4, '报刊杂志': 5,
    #                 '餐饮美食': 3, '电子书籍': 25, '儿童应用': 27, '健康医疗': 9,
    #                 '交通导航': 3, '教育教学': 5, '金融理财': 18, '卡通动漫': 2,
    #                 '浏览器': 3, '旅游出行': 7, '美化壁纸': 18, '商务办公': 40,
    #                 '生活助手': 10, '输入法': 1, '数字音乐': 2, '通话通信': 5,
    #                 '新闻资讯': 9, '娱乐八卦': 9}
    # soft_sortdetail_v1 = {'影音工具': '300029004', '社区交友': '300029005', '系统工具': '300029006', '网络视频': '300029007',
    #                       }
    # url_first = "http://odp.mmarket.com/t.do?requestid=app_game_labellist&labelid={param}&number=25&mark=xxx&categoryname=WIFI&type=1&number=25&mark=2"
    url_first = "http://odp.mmarket.com/t.do?requestid=soft_sortdetail_v1&sortid={param}&needNewActivity=true&defaultType=2&seqtype=hotlist&currentPage={paramcurrentPage}&totalRows={paramtotalRows}"

    headers = {'appname': 'MM6.5.1.001.01_CTAndroid_JT', 'ua': 'android-19-720x1280-VIVO XPLAY6',
               'User-Agent': 'android-19-720x1280-VIVO XPLAY6'}

    # index = random.randint(0, len(soft_sortdetail_v1.keys()) - 1)

    # for index in range(len(soft_sortdetail_v1.keys())):
    index=0
    key_index = list(soft_sortdetail_v1.keys())[index]
    print(key_index)
    key_index='商务办公'
    total_page = soft_page_v1.get(key_index)
    print("------------------------------------")
    for mc in range(0, total_page):
        test_apps = []
        tmp_app_sizes=[]
        tmp_apps = []
        yingyong = soft_sortdetail_v1.get(key_index)
        print(yingyong)
    # random_page = random.randint(0, total_page-1)
    # print(random_page)
        real_url = url_first.format(param=soft_sortdetail_v1.get(key_index), paramcurrentPage=str(mc), paramtotalRows='1000')

        try:
            result_str = requests.get(url=real_url, headers=headers)
            if not result_str:
                print('result_str None')
                return
            print("-----+++++++++++++++++++")
            # print(result_str.json())
            items = result_str.json()['items']
            total_page1=result_str.json()['pageInfo'].get('totalPage')
            totalRows = result_str.json()['pageInfo'].get('totalRows')
            curPage = result_str.json()['pageInfo'].get('curPage')
            print(total_page1)
            print(totalRows)
            print(curPage)
            for i in range(len(items)):
                app_size = items[i]['appSize']
                tmp_app_sizes.append(items[i]['appSize'])
                tmp_apps.append(items[i]['name'])
                if app_size > 20000:
                    test_apps.append(items[i]['name'])
            print(test_apps)
            print(tmp_apps)
            print(tmp_app_sizes)
                # print items[i]['appSize']

        except Exception:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback)
            print("selectApp Exception")
            return 'false'

# os.popen("adb shell am start -n com.aspire.mm/.app.HotSaleActivity")
# print(attrs.udids[0])
# appP=str(attrs.mmattr[0]['appPackage'])
# appA=str(attrs.mmattr[0]['appActivity'])
# print(appP)
# print(appA)
# os.popen("adb -s "+attrs.udids[0]+" shell am start -n com.aspire.mm/.app.HotSaleActivity")
# bb=[]
# print(len(bb))
selectAPPS()
