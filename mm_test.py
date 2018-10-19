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

import baidu_test
import huawei_test
import qihoo_test
import select_apps
from attr import attrs
from ch_network import change_nk
from ui import UIman
import yyb_test


class mm(UIman):

    def __init__(self):
        print("mm setup_init")
        self.limit_size = attrs.limit_size_4g
        self.attrs = attrs.mmattr
        self.network = ''
        self.test_app_name = ''
        self.test_apps = []
        self.test_apps_4g = []
        # self.test_apps = ['qq', '微信', 'WIFI万能钥匙', '快手', '支付宝', '宜搜小说', '作业帮', '美团', '饿了么']
        self.test_apps_dic = []
        self.data_dict = {
            "product_name": "MM",
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
        # self.selectAPPS()
        # length = len(self.test_apps)
        # print(length)
        # global test_apps
        # test_apps = self.test_apps
        # time.sleep(3)
        # try:
        self.test_a_run()
        if self.driver is not None:
            print("tearDown")
            self.driver.quit()
        else:
            print("driver is None")
        # except Exception:
        #     print("MM test_a_run 应该是webDriverException异常,不执行quit,结束测试")
        #     exc_type, exc_value, exc_traceback = sys.exc_info()
        #     traceback.print_exception(exc_type, exc_value, exc_traceback)

    def test_a_run(self):
        print("更改后网络为：")
        time.sleep(1)
        print(self.driver.network_connection)
        if self.driver.network_connection == 4:
            self.network = '4G'
            print('检测到网络4G')
        else:
            self.network = 'WIFI'
            print('检测到网络WIFI,等待一分钟待wifi稳定')
            time.sleep(60)
        print("关掉app")
        self.driver.press_keycode(4)
        time.sleep(1)
        self.driver.press_keycode(3)
        time.sleep(1)
        self.closeapp()
        time.sleep(3)
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
            print('选几次app长度还是小于3，本轮不测试')
            return
        if self.network == '4G' and length1 < 2:
            print("4G app长度小于2返回")
            return
        global test_apps
        test_apps = self.test_apps
        global test_apps_4g
        test_apps_4g = self.test_apps_4g
        # test_apps = self.test_apps[(length-3): length]
        if self.network == '4G':
            self.test_apps_dic = self.test_apps_4g[(length1-1): length1]
        else:
            if length > 10:
                self.test_apps_dic = self.test_apps[(length - 10): length]
            else:
                self.test_apps_dic = self.test_apps[:]
        length = len(self.test_apps_dic)
        # funcs = [self.startup, self.deletepackage, self.search]
        funcs = [self.startup, self.deletepackage, self.search, self.download]
        print("MM需要跑 " + str(length) + " 次")
        # self.screenShot("aa下载")
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
                        self.screenShot(f.__name__ + "_false_mm")
                        break
                except WebDriverException:
                    print("将异常抛到start_test,结束测试")
                    raise
                except Exception:
                    exc_type, exc_value, exc_traceback = sys.exc_info()
                    traceback.print_exception(exc_type, exc_value, exc_traceback)
                    self.screenShot(f.__name__ + "_error_mm")
            print('开始关掉app')
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

    def startup(self):
        # try:
        self.driver.launch_app()
        # time.sleep(8)
        ell = self.ele_mgr(8, lambda x: x.find_element_by_id('com.huawei.systemmanager:id/btn_allow'))
        if ell:
            ell.click()
        ell = self.ele_mgr(2, lambda x: x.find_element_by_id('com.android.packageinstaller:id/permission_allow_button'))
        if ell:
            ell.click()
        current_activity = self.driver.current_activity
        if current_activity == u'.app.HomeActivity':
            print('启动：正常')
            return 'OK'
        else:
            self.driver.press_keycode(4)
            time.sleep(1)
            return 'false'
        # except Exception:
        #     print("startup 出现异常")
        #     return 'false'

    def search(self):
        # try:
            # current_activity = self.driver.current_activity
            # current_activity = '.app.TabBrowserActivity'
            # 搜索框
            el2 = self.ele_mgr(20, lambda x: x.find_element_by_id('com.aspire.mm:id/search_text_view'))
            # el2 = self.findid("com.aspire.mm:id/search_text_view")
            if el2 is None:
                return 'false'
            el2.click()
            print(self.test_app_name)
            el = self.ele_mgr(20, lambda x: x.find_element_by_id('com.aspire.mm:id/searchText'))
            # el = self.findid("com.aspire.mm:id/searchText")
            if el is None:
                return 'false'
            el.click()
            time.sleep(3)
            ts1 = time.time()
            self.findxpath_for_search("//android.widget.TextView[@resource-id='com.aspire.mm:id/search_hot_title' and @text='娱乐']")
            ts2 = time.time()-ts1
            el = self.ele_mgr(20, lambda x: x.find_element_by_id('com.aspire.mm:id/searchText'))
            el.send_keys(self.test_app_name)
            el = self.ele_mgr(20, lambda x: x.find_element_by_id('com.aspire.mm:id/searchButton'))
            if el is None:
                return 'false'
            el.click()
            # self.clickid("com.aspire.mm:id/searchButton")
            # appP=str(attrs.mmattr[0]['appPackage'])
            # appA=str(attrs.mmattr[0]['appActivity'])
            # print(appP)
        #             # print(appA)
        #     try:
        #         # self.driver.start_activity(appP, appA)
        #         os.popen("adb -s " + attrs.udids[0] + " shell am start -n com.aspire.mm/.app.HotSaleActivity")
        #     except Exception:
        #         print("start_activity 异常")
        #         exc_type, exc_value, exc_traceback = sys.exc_info()
        #         traceback.print_exception(exc_type, exc_value, exc_traceback)
            # os.popen("adb -s " + attrs.udids[0] + " shell am start -n com.aspire.mm/.app.HotSaleActivity")
            start_time = time.time()
            # el = self.ele_mgr_forserch(20, lambda x: x.find_element_by_id('com.aspire.mm:id/interested'))
            el = self.findid_for_search("com.aspire.mm:id/interested")
            rt_time = time.time() - start_time
            if el:
                print(ts2)
                print(rt_time)
                print(rt_time - ts2)
                if ts2 < 0.8:
                    rt_time = rt_time-ts2
                self.data_dict['bussiness'] = '搜索'
                self.data_dict['network'] = self.network
                self.data_dict['data_type'] = 'time_delay'
                self.data_dict['data_value'] = str(round(rt_time, 2))
                self.data_dict['test_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.data_dict['remark'] = self.test_app_name
                # print(self.driver.current_activity)
                if self.driver.current_activity == ".app.HomeActivity" or rt_time > 10:
                    self.data_dict['is_delete'] = '1'
                else:
                    self.data_dict['is_delete'] = '0'
                # print(self.data_dict)
                db_helper.insert_data("mm_2018", self.data_dict)
                print('搜索：正常')
                return 'OK'
            else:
                # self.driver.press_keycode(4)
                return 'false'
        # except Exception:
        #     exc_type, exc_value, exc_traceback = sys.exc_info()
        #     traceback.print_exception(exc_type, exc_value, exc_traceback)
        #     return 'false'

    def download(self):
    #     el = self.findid("com.aspire.mm:id/search_hot_flowview", 8)
    #     el2 = self.findxpath("//android.widget.ListView[@resource-id='android:id/list']/android.widget.RelativeLayout[2]")
    # "com.aspire.mm:id/tv_name"
        el2 = self.ele_mgr(20, lambda x: x.find_element_by_id('com.aspire.mm:id/tv_name'))
        # el2 = self.findxpath("//android.widget.ListView[@resource-id='android:id/list']/android.widget.RelativeLayout[1]")
        if el2:
            el2.click()
        else:
            return 'false'
        ell = self.ele_mgr(20, lambda x: x.find_element_by_id('com.aspire.mm:id/download_btn'))
        # ell = self.findid("com.aspire.mm:id/download_btn", 30)
        if ell is None:
            print('没找到download_btn，return false')
            return 'false'
        el = self.findxpath("//android.widget.RelativeLayout[@resource-id='com.aspire.mm:id/footer_bar']//android.widget.TextView[contains(@text,'下载   ')]", 20)
        if el is None:
            print('app不符合要求，本轮不测试下载，return false')
            return 'false'
        app_size = el.text.replace(u'下载', '').replace(u' ', '').replace(u'M', '').replace(u'KB','')
        f_app_size = float(app_size)
        minSize = False
        print(f_app_size)
        if f_app_size < 20.0:
            print("小于20M不下")
            return 'true'
        if self.network == '4G':
            if f_app_size > self.limit_size:
                print("大于50, 4G环境不下载")
                return 'true'
            if f_app_size > 10.0:
                minSize = True

        el = self.findxpath("//android.widget.RelativeLayout[@resource-id='com.aspire.mm:id/footer_bar']//android.widget.TextView[contains(@text,'下载   ')]",20)
        el.click()
        start_time = time.time()
        if self.network == '4G' and minSize:
            el3 = self.findid("com.aspire.mm:id/btn_ok", 4)
            if el3:
                el3.click()
                start_time = time.time()
        # el = self.findClassText1("android.widget.TextView", "安装")
        el = self.findid("com.android.packageinstaller:id/cancel_button", 120)
        rt_time = time.time() - start_time
        print(str(rt_time))
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
                self.driver.press_keycode(4)
                print('找到 PackageInstallerActivity ,现在按返回 ')
                time.sleep(1)
            self.driver.press_keycode(4)
            time.sleep(1)
            # self.driver.press_keycode(4)
            # time.sleep(1)
            print('下载：正常')
            return 'OK'
        else:
            print('未完成')
            # self.screenShot("mm下载_error")
            # self.exc_command("input tap 556 1842")
            return 'false'


    def deletepackage(self):
        # try:
            re = self.exc_command("rm -f /sdcard/mm/download/*")
            # re = self.exc_command("rm -f /sdcard/mm/cache/*")
            print('删除之前下载的安装包：正常')
            # "com.huawei.systemmanager:id/btn_forbbid"
            ele = self.ele_mgr(17, lambda x: x.find_element_by_id('com.aspire.mm:id/mgr_icon'))
            if ele:
                ele.click()
            else:
                elc = self.ele_mgr(3, lambda x: x.find_element_by_id('com.huawei.systemmanager:id/btn_forbbid'))
                if elc:
                    elc.click()
                else:
                    raise RuntimeError('没找到删除入口')
            # self.findid("com.aspire.mm:id/mgr_icon").click()
            el = self.ele_mgr(5, lambda x: x.find_element_by_id('com.aspire.mm:id/iknow'))
            # el = self.findid("com.aspire.mm:id/iknow", 5)
            if el:
                el.click()
            # self.findid("//android.widget.TabWidget[@resource-id='android:id/tabs']/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]").click()
            el1 = self.ele_mgr(6, lambda x: x.find_element_by_id('com.aspire.mm:id/toptab_text'))
            if el1:
                el1.click()
                e2 = self.ele_mgr(6, lambda x: x.find_element_by_id('com.aspire.mm:id/downloadDelButton'))
                # el = self.findid("com.aspire.mm:id/downloadDelButton", 10)
                if e2:
                    e2.click()
                    self.ele_mgr(10, lambda x: x.find_element_by_id('com.aspire.mm:id/button2')).click()
                    # self.findid("com.aspire.mm:id/button2").click()
            self.driver.press_keycode(4)
            current_activity = self.driver.current_activity
            print(current_activity)
            if current_activity == u'.app.HomeActivity':
                print('删除应用后回到正常的首页')
                return 'OK'
            else:
                print("没在首页")
                return 'false'
        # except Exception:
        #     print('删除包异常')
        #     return 'false'

    def closeapp(self):
        # try:
            self.driver.close_app()
        # except Exception:
        #     print('删除包异常')
        #     return 'false'

    def run_cmd(self, cmd):
        with subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as process:
            cmd_str = process.stdout.read().decode("utf-8")
            print(cmd)
        return cmd_str


if __name__ == '__main__':
    test_apps = []
    test_apps_4g = []
    # test_apps = [ u'腾讯微博手机客户端',u'天涯社区',u'爱看',u'乐趣', u'快视频']
    try:
        t = change_nk()
        t.change_network()
    except Exception:
        print("设置数据网络出现了问题,本轮不测试数据网络")
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback)
    try:
        t = mm()
        t.start_test()
    except Exception:
        print("MM 异常")
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback)
    try:
        y = yyb_test.yyb(test_apps, test_apps_4g)
        y.start_test()
    except Exception:
        print("应用宝 异常")
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback)
    try:
        y = huawei_test.huawei(test_apps, test_apps_4g)
        y.start_test()
    except Exception:
        print("华为手机助手 异常")
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback)
    try:
        y = baidu_test.baidu(test_apps, test_apps_4g)
        y.start_test()
    except Exception:

        print("百度手机助手 异常")
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback)
    try:
        y = qihoo_test.qihoo(test_apps, test_apps_4g)
        y.start_test()
    except Exception:
        print("360手机助手 异常")
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback)
    print("等待60 seconds")
    time.sleep(60)