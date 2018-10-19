#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import subprocess
import sys
import time
import traceback
import requests
import random
import db_helper
import datetime
import unittest

from attr import attrs
from ui import UIman


class yyb(UIman):

    def setup_init(self):
        print("yyb setup_init")
        return attrs.yybattr

    def test_a_run(self):
        self.data_dict['product_name'] = 'yyb'
        print('yyb 开始start_test')
        print(self.driver.network_connection)
        if self.driver.network_connection == 4:
            self.network = '4G'
            print('检测到网络4G')
        else:
            self.network = 'wifi'
            print('检测到网络wifi')
        print("关掉app")
        self.driver.press_keycode(4)
        time.sleep(1)
        self.driver.press_keycode(3)
        time.sleep(1)
        self.closeapp()
        time.sleep(3)
        length = len(self.test_apps)
        print('len1: ' + str(length))
        self.selectAPPS()
        length = len(self.test_apps)
        print('len2: '+str(length))
        if self.network == '4G':
            self.test_apps_dic = self.test_apps[(length-2): length]
        else:
            self.test_apps_dic = self.test_apps[:]
        length = len(self.test_apps_dic)
        funcs = [self.startup, self.deletepackage, self.search, self.download]
        for x in range(length):
            print("=============开始第" + str(x + 1) + "次测试====================")
            self.test_app_name = self.test_apps_dic[x]
            for f in funcs:
                print('---------开始执行函数：'+str(f.__name__)+'--------------')
                try:
                    result = f()
                    if result == 'false':
                        # result = 'false ' + self.screenShot(f.__name__)
                        print(str(f.__name__)+'返回false,break')
                        break
                except RuntimeError:
                    raise
                except Exception:
                    exc_type, exc_value, exc_traceback = sys.exc_info()
                    traceback.print_exception(exc_type, exc_value, exc_traceback)
                    # result = 'false_' + self.screenShot(f.__name__ + "_error")
            print('开始复位')
            # self.driver.press_keycode(4)
            # time.sleep(1)
            self.driver.press_keycode(4)
            time.sleep(1)
            self.driver.press_keycode(3)
            time.sleep(1)
            self.closeapp()
            time.sleep(3)
            # def screenShot(self, name):
            # time_str = time.strftime('_%m%d_%H%M', time.localtime(time.time()))
            # folder = os.path.abspath(os.path.join(os.path.dirname(__file__), ".")) + '\\screenshots\\'
            # if not self.driver.get_screenshot_as_file(folder + name + time_str + ".png"):
            # print("screenshot error:",name)
        # print("testvar")
        # global testvar
        # print(testvar)
        # testvar = "应用宝"
        # print("testvar")
        # print(testvar)

    def selectAPPS(self):

        soft_sortdetail_v1 = {'影音工具': '678936512', '社区交友': '678936511','系统工具': '678936514', '网络视频': '678936530', '网络购物':'678936527'}

        url_first = "http://odp.mmarket.com/t.do?requestid=soft_sortdetail_v1&sortid={param}&needNewActivity=true&defaultType=1&seqtype=hotlist"

        headers = {'appname': 'MM6.5.1.001.01_CTAndroid_JT', 'ua': 'android-19-720x1280-VIVO XPLAY6', 'User-Agent': 'android-19-720x1280-VIVO XPLAY6'}

        index = random.randint(0,len(soft_sortdetail_v1.keys())-1)

        real_url = url_first.format(param=list(soft_sortdetail_v1.values())[index])

        try:
            result_str = requests.get(url=real_url,headers=headers)

            items = result_str.json()['items']

            for i in range(len(items)):

                self.test_apps.append(items[i]['name'])
                #print items[i]['name']
                #print items[i]['appSize']

        except Exception:
            return 'false'

    def startup(self):
        # try:
            self.driver.launch_app()
            time.sleep(5)
            current_activity = self.driver.current_activity
            print(current_activity)
            if current_activity == u'com.tencent.assistantv2.activity.MainActivity':
                print('启动：正常')
                return 'OK'
            else:
                return 'false'
        # except Exception:
        #     exc_type, exc_value, exc_traceback = sys.exc_info()
        #     traceback.print_exception(exc_type, exc_value, exc_traceback)
        #     return 'false'

    def search(self):
        # try:
            # current_activity = self.driver.current_activity
            # current_activity = '.app.TabBrowserActivity'
            # 搜索框
            el2 = self.findid("com.tencent.android.qqdownloader:id/awt")
            if el2:
                el2.click()
            else:
                return 'false'
            el = self.findid("com.tencent.android.qqdownloader:id/yv")
            if el is None:
                return 'false'
            s = self.test_app_name
            el.send_keys(s)
            print(s)
            self.clickid("com.tencent.android.qqdownloader:id/a5t")
            start_time = time.time()
            el = self.findid_for_search("com.tencent.android.qqdownloader:id/wt")
            rt_time = time.time() - start_time
            print(rt_time)
            if el:
                self.data_dict['bussiness'] = '搜索'
                self.data_dict['network'] = self.network
                self.data_dict['data_type'] = 'time_delay'
                self.data_dict['data_value'] = str(round(rt_time, 2))
                self.data_dict['test_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.data_dict['remark'] = self.test_app_name
                db_helper.insert_data("mm_2018", self.data_dict)
                print('搜索：正常')
                return 'OK'
            else:
                print('没搜到，不下载')
                self.driver.press_keycode(4)
                return 'false'
        # except Exception:
        #     exc_type, exc_value, exc_traceback = sys.exc_info()
        #     traceback.print_exception(exc_type, exc_value, exc_traceback)
        #     return 'false'

    def download(self):
        # try:
            el2 = self.findxpath("//android.widget.ListView/android.widget.RelativeLayout[2]")
            if el2 is None:
                print("not find")
                return 'false'
            el2.click()
            # el = self.findxpath("//android.widget.TextView[@resource-id='com.tencent.android.qqdownloader:id/r5' and contains(@text,' 下载 (')]")
            el = self.findid("com.tencent.android.qqdownloader:id/r5")
            # if not el
            # "com.tencent.android.qqdownloader:id/qy" "com.tencent.android.qqdownloader:id/r2"
            # "com.tencent.android.qqdownloader:id/r5"安装
            if el is None:
                print('没有找到下载条，return false')
                return 'false'
            # print u'下载条上的文本为：'
            # print el.text
            if u' 下载 ' in el.text:
                print('包含下载')
                # " 下载 (62.3MB)"
                app_size1 = el.text.replace(u' ', '').replace(u'下载', '').replace(u' ', '').replace(u'(', '').replace(u'MB', '').replace(u')', '')
                app_size = str(app_size1)
                print(app_size)
                el.click()
                start_time = time.time()
                # "com.tencent.android.qqdownloader:id/e6" 下载提示
                # 继续下载
            else:
                print('不含下载，return')
                return 'false'
            if self.network == '4G':
                kl = self.findid("com.tencent.android.qqdownloader:id/a30", 5)
                if kl:
                    print('点击继续下载')
                    kl.click()
                    start_time = time.time()
                # kl = self.findid("com.tencent.android.qqdownloader:id/a30", 2)
                # if kl:
                #     print('点击取消,大王卡提示')
                #     kl.click()
                # print("开始用current_Activity")
                # timeout1 = 30
                # while timeout1 > 0:
                #     # "com.android.packageinstaller/.PackageInstallerActivity"
                #     if "com.android.packageinstaller/.PackageInstallerActivity" == self.driver.current_activity:
                #         print('检测到在安装界面')
                #         el = 'ture'
                #         break
                #     else:
                #         time.sleep(1)
                #         print(timeout1)
                #         timeout1 = timeout1-1
                # el = self.findid("com.android.packageinstaller:id/ok_button", 20)
                # el = self.findidAndIdClick("com.android.packageinstaller:id/ok_button", "com.tencent.android.qqdownloader:id/a30", 60)
            # if self.network == 'wifi':
                # el = self.findidAndId("com.android.packageinstaller:id/ok_button","com.tencent.android.qqdownloader:id/a30",20)
                # print("开始用current_Activity")
                # timeout1 = 30
                # while timeout1 > 0:
                #     # "com.android.packageinstaller/.PackageInstallerActivity"
                #     uc = self.driver.current_activity
                #     print(uc)
                #     if ".PackageInstallerActivity" in uc:
                #         print('检测到在安装界面')
                #         el = 'ture'
                #         break
                #     else:
                #         time.sleep(1)
                #         timeout1 = timeout1-1
                #         print(timeout1)
                # el = self.findidyyb("com.android.packageinstaller:id/ok_button", 10)
            el = self.find_text_in_id("com.tencent.android.qqdownloader:id/r5", "安装", "com.android.packageinstaller:id/ok_button", 60)
            rt_time = time.time() - start_time
            print(rt_time)
                # 省心装"com.tencent.android.qqdownloader:id/a30" 取消,不清缓存的话只提示一次
                # "com.tencent.android.qqdownloader/com.tencent.pangu.activity.AppDetailActivityV5"
                # 安装"com.android.packageinstaller:id/ok_button"  取消"com.android.packageinstaller:id/cancel_button"
            if el:
                print('下载完成')
                self.data_dict['bussiness'] = '下载'
                self.data_dict['network'] = self.network
                self.data_dict['data_type'] = 'download_rate'
                self.data_dict['data_value'] = round(float(app_size) / rt_time * 8, 2)
                self.data_dict['remark'] = self.test_app_name+'|'+app_size+'M'
                self.data_dict['test_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                db_helper.insert_data("mm_2018", self.data_dict)
                if self.driver.current_activity == u'.PackageInstallerActivity':
                    self.clickid("com.android.packageinstaller:id/cancel_button")
                    print('找到 PackageInstallerActivity ,现在按返回 ')
                    # self.driver.press_keycode(self, 4)
                    # time.sleep(2)
                # self.driver.press_keycode(4)
                # time.sleep(1)
                self.driver.press_keycode(4)
                time.sleep(1)
                print('下载：正常')
                return 'OK'
            else:
                print(rt_time)
                print('秒内没找到ok_button，下载未完成')
                return 'false'
        # except Exception:
        #     exc_type, exc_value, exc_traceback = sys.exc_info()
        #     traceback.print_exception(exc_type, exc_value, exc_traceback)
        #     return 'false'

    def deletepackage(self):
        # try:
            self.findid("com.tencent.android.qqdownloader:id/ax5").click()
            cur_acti = self.driver.current_activity
            if cur_acti == u"com.tencent.pangu.activity.DownloadActivity":
                print("在下载管理页")
            el = self.findid("com.tencent.android.qqdownloader:id/u1", 10)
            if el:
                el.click()
                self.findid("com.tencent.android.qqdownloader:id/a32").click()
            self.driver.press_keycode(4)
            cur_acti = self.driver.current_activity
            if cur_acti == u"com.tencent.assistantv2.activity.MainActivity":
                print('正确复位到首页')
            print('删除之前下载的安装包：正常')
            return 'OK'
        # except Exception:
        #     exc_type, exc_value, exc_traceback = sys.exc_info()
        #     traceback.print_exception(exc_type, exc_value, exc_traceback)
        #     return 'false'

    def closeapp(self):
        # try:
            self.driver.close_app()
        # except Exception:
        #     print("yyb closeapp出现了异常")
        #     return 'false'

    def run_cmd(self, cmd):
        with subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as process:
            cmd_str = process.stdout.read().decode("utf-8")
            print(cmd)
        return cmd_str


if __name__ == '__main__':
    unittest.main()
    # 运行所有的测试用例