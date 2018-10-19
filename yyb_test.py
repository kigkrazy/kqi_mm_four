#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess
import sys
import time
import traceback
import requests
import random

from selenium.common.exceptions import WebDriverException

import db_helper
import datetime

from appium import webdriver

import select_apps
from attr import attrs
from ui import UIman


class yyb(UIman):

    def __init__(self, test_apps, test_apps_4g):
        print("yyb __init__")
        self.limit_size = attrs.limit_size_4g
        self.attrs = attrs.yybattr
        self.test_apps = test_apps
        self.test_apps_4g = test_apps_4g
        self.network = ''
        self.test_app_name = ''
        self.test_apps_dic = []
        self.data_dict = {
            "product_name": "YYB",
            "client": "android",
            "bussiness": "",
            "data_type": "",
            "data_value": "",
            "network": "",
            "remark": "",
            "test_time": "",
            "is_delete": "0"
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4735/wd/hub', self.attrs[0])
        print(self.driver)
        print(self.attrs[0]["appPackage"])

    def start_test(self):
        # for i in self.test_apps:
        #     print(i)
        # time.sleep(3)
        self.test_a_run()
        if self.driver is not None:
            print("tearDown")
            self.driver.quit()
        else:
            print("driver is None")

    def test_a_run(self):
        print('YYB 开始start_test')
        print(self.driver.network_connection)
        if self.driver.network_connection == 4:
            self.network = '4G'
            print('检测到网络4G')
        else:
            self.network = 'WIFI'
            print('检测到网络WIFI')
        print("关掉app")
        self.driver.press_keycode(4)
        time.sleep(1)
        self.driver.press_keycode(3)
        time.sleep(1)
        self.closeapp()
        time.sleep(3)
        if len(self.test_apps) == 0:
            print("应用宝需要选app")
            for uw in range(0, 5):
                tmp1, tmp1_4g = select_apps.selectAPPS()
                for t1 in tmp1:
                    self.test_apps.append(t1)
                for t1_4g in tmp1_4g:
                    self.test_apps_4g.append(t1_4g)
                length = len(self.test_apps)
                length1 = len(self.test_apps_4g)
                if self.network == 'WIFI' and length > 8:
                    break
                if self.network == '4G' and length1 > 2:
                    break
                time.sleep(10)
        length = len(self.test_apps)
        length1 = len(self.test_apps_4g)
        print('WIFI length: ' + str(length))
        print("4G length1: " + str(length1))
        if length < 3:
            print("app长度小于3返回")
            return
        if self.network == '4G' and length1 < 2:
            print("4G app长度小于2返回")
            return
        if self.network == '4G':
            self.test_apps_dic = self.test_apps_4g[(length1 - 1): length1]
        else:
            if length > 10:
                self.test_apps_dic = self.test_apps[(length - 10): length]
            else:
                self.test_apps_dic = self.test_apps[:]
        length = len(self.test_apps_dic)
        # funcs = [self.startup, self.deletepackage, self.search]
        funcs = [self.startup, self.deletepackage, self.search, self.download]
        print("应用宝需要跑 " + str(length) + " 次")
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
                        self.screenShot(f.__name__ + "_false_yyb")
                        break
                except WebDriverException:
                    print("将异常抛到start_test,结束测试")
                    raise
                except Exception:
                    exc_type, exc_value, exc_traceback = sys.exc_info()
                    traceback.print_exception(exc_type, exc_value, exc_traceback)
                    self.screenShot(f.__name__ + "_error_yyb")
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

    def startup(self):
        # try:
        self.driver.launch_app()
        ell = self.ele_mgr(5, lambda x: x.find_element_by_id('com.huawei.systemmanager:id/btn_allow'))
        if ell:
            ell.click()
        ell = self.ele_mgr(2, lambda x: x.find_element_by_id('com.android.packageinstaller:id/permission_allow_button'))
        if ell:
            ell.click()
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
            # "com.aspire.mm/.app.TabBrowserActivity"
            # 搜索框
            el2 =self.ele_mgr(20, lambda x: x.find_element_by_id('com.tencent.android.qqdownloader:id/awt'))
            # el2 = self.findid("com.tencent.android.qqdownloader:id/awt")
            if el2:
                el2.click()
            else:
                return 'false'
            print(self.test_app_name)
            el = self.ele_mgr(20, lambda x: x.find_element_by_id('com.tencent.android.qqdownloader:id/yv'))
            # el = self.findid("com.tencent.android.qqdownloader:id/yv")
            if el is None:
                return 'false'
            el.click()

            el = self.ele_mgr(20, lambda x: x.find_element_by_id('com.tencent.android.qqdownloader:id/yv'))
            # el = self.findid("com.tencent.android.qqdownloader:id/yv")
            if el is None:
                return 'false'
            el.send_keys(self.test_app_name)
            self.clickid("com.tencent.android.qqdownloader:id/a5t")
            start_time = time.time()

            # el = self.ele_mgr_forserch(20, lambda x: x.find_element_by_id('com.tencent.android.qqdownloader:id/wt'))
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
                # print(self.driver.current_activity)
                if self.driver.current_activity != "com.tencent.nucleus.search.SearchActivity" or rt_time > 10:
                    # print("满足")
                    self.data_dict['is_delete'] = '1'
                else:
                    self.data_dict['is_delete'] = '0'
                # print(self.data_dict)
                db_helper.insert_data("mm_2018", self.data_dict)
                print('搜索：正常')
                return 'OK'
            else:
                print('没搜到，不下载')
                # self.driver.press_keycode(4)
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
                app_size1 = el.text.replace(u' ', '').replace(u'下载', '').replace(u' ', '').replace(u'(', '').replace(u'MB', '').replace(u')', '').replace(u'KB','')
                app_size = str(app_size1)
                f_app_size = float(app_size)
                print(f_app_size)
                if f_app_size < 20.0:
                    print("小于20M不下")
                    return 'true'
                if self.network == '4G':
                    if f_app_size > self.limit_size:
                        print("大于50, 4G环境不下载")
                        return 'true'
                self.clickid("com.tencent.android.qqdownloader:id/r5")
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
            # if self.network == 'WIFI':
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

            el = self.findid("com.android.packageinstaller:id/cancel_button", 120)
            # el = self.find_text_in_id("com.tencent.android.qqdownloader:id/r5", "安装", "com.android.packageinstaller:id/ok_button", 80)
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
                self.data_dict['is_delete'] = '0'
                db_helper.insert_data("mm_2018", self.data_dict)
                print(self.data_dict)
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
            ele = self.ele_mgr(17, lambda x: x.find_element_by_id('com.tencent.android.qqdownloader:id/ax5'))
            if ele:
                ele.click()
            else:
                elc = self.ele_mgr(3, lambda x: x.find_element_by_id('com.huawei.systemmanager:id/btn_forbbid'))
                if elc:
                    elc.click()
                else:
                    raise RuntimeError('没找到删除入口')
            # self.findid("com.tencent.android.qqdownloader:id/ax5").click()
            cur_acti = self.driver.current_activity
            if cur_acti == u"com.tencent.pangu.activity.DownloadActivity":
                print("在下载管理页")
            el = self.ele_mgr(10, lambda x: x.find_element_by_id('com.tencent.android.qqdownloader:id/u1'))
            # el = self.findid("com.tencent.android.qqdownloader:id/u1", 10)
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
        self.driver.close_app()


    def run_cmd(self, cmd):
        with subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as process:
            cmd_str = process.stdout.read().decode("utf-8")
            print(cmd)
        return cmd_str


if __name__ == '__main__':
    test_apps =[]
    test_apps_4g= []
    # test_apps = ['wifi万能钥匙','爱看', '快视频', '腾讯wifi管家',  '好运万年历']
    try:
        y = yyb(test_apps, test_apps_4g)
        y.start_test()
    except Exception:
        print("360异常")
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback)
    print("等待五分钟")
    # time.sleep(5 * 60)