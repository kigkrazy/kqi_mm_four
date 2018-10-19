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


class baidu(UIman):
    def __init__(self, test_apps ,test_app_4g):
        print("baidu __init__")
        self.limit_size = attrs.limit_size_4g
        self.attrs = attrs.bdattr
        self.test_apps = test_apps
        self.test_apps_4g = test_app_4g
        self.network = ''
        self.test_app_name = ''
        self.test_apps_dic = []
        self.data_dict = {
            "product_name": "BAIDU",
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
        # if len(self.test_apps) == 0:
        #     print("华为需要选app")
        #     self.selectAPPS()
        #     length = len(self.test_apps)
        #     print('len1: ' + str(length))
        #     self.selectAPPS()
        #     length = len(self.test_apps)
        #     print('len2: ' + str(length))
        # # length = len(self.test_apps)
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
        print('百度手机助手 开始start_test')
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
            print("百度手机助手需要选app")
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
        print("百度手机助手需要跑 " + str(length) + " 次")
        for x in range(length):
            print("=============开始第" + str(x + 1) + "次测试====================")
            self.test_app_name = self.test_apps_dic[x]
            print(self.test_app_name)
            for f in funcs:
                print('---------开始执行函数：'+str(f.__name__)+'--------------')
                try:
                    result = f()
                    if result == 'false':
                        # result = 'false ' + self.screenShot(f.__name__)
                        print(str(f.__name__)+'返回false,break')
                        self.screenShot(f.__name__ + "_false_baidu")
                        break
                except WebDriverException:
                    print("将异常抛到start_test,结束测试")
                    raise
                except Exception:
                    exc_type, exc_value, exc_traceback = sys.exc_info()
                    traceback.print_exception(exc_type, exc_value, exc_traceback)
                    self.screenShot(f.__name__ + "_error_baidu")
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
        if current_activity == u'.MainActivity':
            print('启动：正常')
            return 'OK'
        else:
            return 'false'
        # except Exception:
        #     exc_type, exc_value, exc_traceback = sys.exc_info()
        #     traceback.print_exception(exc_type, exc_value, exc_traceback)
        #     return 'false'

    def search(self):
        # 返回首页
        # self.driver.start_activity(self.attrs[0]["appPackage"],self.attrs[0]["appActivity"])
        # self.driver.start_activity(self.attrs[0]["appPackage"], self.attrs[0]["appWaitActivity"])
        self.driver.launch_app()
        time.sleep(8)
        # current_activity = self.driver.current_activity
        # if current_activity == u'.LauncherActivity':
        #     print('启动：正常')
        #     return 'OK'
        # # 搜索框

        el2 = self.ele_mgr(20, lambda x: x.find_element_by_id("com.baidu.appsearch:id/libui_titlebar_search_textinput"))
        if el2 is None:
            print('找不到搜索框')
            return "false"
        el2.click()
        #         输入搜索应用
        # el= self.ele_mgr(20, lambda x: x.find_element_by_id("com.baidu.appsearch:id/search_result_search_textinput"))
        self.findid("com.baidu.appsearch:id/search_result_search_textinput").send_keys(self.test_app_name)

        # el.sendkey(self.test_app_name)
        el = self.ele_mgr(20, lambda x: x.find_element_by_id("com.baidu.appsearch:id/search_result_search"))
        if el is None:
            print('找不到搜索按钮')
            return "false"
        el.click()
        # 开始时间
        starttime = time.time()
        el = self.findid_for_search("com.baidu.appsearch:id/app_item")
        rt_time = time.time() - starttime
        print("百度搜索时延为" +str(rt_time))
        if el:
            self.data_dict['bussiness'] = '搜索'
            self.data_dict['network'] = self.network
            self.data_dict['data_type'] = 'time_delay'
            self.data_dict['data_value'] = str(round(rt_time, 2))
            self.data_dict['test_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.data_dict['remark'] = self.test_app_name
            # print(self.driver.current_activity)
            if self.driver.current_activity == ".distribute.MainActivity" or rt_time > 10:
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

    def download(self):
        # 点击首个搜索结果
        el2=self.findid("com.baidu.appsearch:id/app_item")
        if el2 is None:
            print('找不到搜索结果')
            return 'false'
        el2.click()
        # 点击下载按钮
        ell = self.ele_mgr(20, lambda x: x.find_element_by_id('com.baidu.appsearch:id/app_content_btn_control_text'))
        if ell is None:
            print('没找到app_content_btn_control_text，return false')
            return 'false'
        app_szie = self.findid("com.baidu.appsearch:id/app_content_btn_control_text").text
        if '下载' not in app_szie:
            print('app不符合要求，本轮不测试下载，return false')
            return 'false'
        print(app_szie)
        # app_size = app_szie.split('下载','M','()')
        # app_size= filter(str.isdigit,str(app_szie))
        app_size = app_szie.replace(u'下载', '').replace(u'', '').replace(u'(', '').replace(u')', '').replace(u'M', '').replace(u'KB','')
        print(app_size)
        f_app_size = float(app_size)
        print(f_app_size)
        if f_app_size < 20.0:
            print("小于20M不下")
            return 'true'
        if self.network == '4G':
            if f_app_size > self.limit_size:
                print("小于10或大于100, 4G环境不下载")
                return 'true'
        # 点击下载
        ell.click()
        start_time = time.time()
        if self.network == '4G':
            eel = self.findid("com.baidu.appsearch:id/libui_ok", 4)
            if eel:
                eel.click()
                start_time = time.time()
        el = self.findid("com.android.packageinstaller:id/cancel_button", 120)

        rt_time = time.time() - start_time
        print(str(rt_time))
        if el:
            print('下载完成')
            self.data_dict['bussiness'] = '下载'
            self.data_dict['network'] = self.network
            self.data_dict['data_type'] = 'download_rate'
            self.data_dict['data_value'] = round(float(app_size) / rt_time * 8, 2)
            self.data_dict['remark'] = self.test_app_name + '|' + app_size + 'M'
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
            # self.exc_command("input tap 556 1842")
            return 'false'


    def deletepackage(self):
        # ele = self.findClassText("android.widget.TextView","管理",8)
        # if ele:
        #     ele.click()
        # else:
        #     elc = self.ele_mgr(3, lambda x: x.find_element_by_id('com.huawei.systemmanager:id/btn_forbbid'))
        #     if elc:
        #         elc.click()
        #     else:
        #         raise RuntimeError('没找到删除入口')
        # 点击下载管理按钮
        # el = self.findid('com.baidu.appsearch:id/text_title_poke')
        # if el.size ==1:
        #     print("无安装包")
        #     return 'ture'

        # el2 = self.findClassText("android.widget.TextView", "下载管理", 5)
        # if el2:
        #     el2.click()
        # else:
        #     elc = self.ele_mgr(3, lambda x: x.find_element_by_id('com.huawei.systemmanager:id/btn_forbbid'))
        #     if elc:
        #         elc.click()
        #     else:
        #         raise RuntimeError('没找到下载管理')
        el = self.ele_mgr(20, lambda x: x.find_element_by_id('com.baidu.appsearch:id/cover_view'))
        if el is None:
            print("没找到右上角下载管理入口")
            return "false"
        el.click()
        el = self.findid("com.baidu.appsearch:id/downloading_title", 15)
        if el is None:
            print("无需删除安装包")
            return 'true'
        # 删除下载任务
        downloadtext = self.findid("com.baidu.appsearch:id/downloading_title").text
        if "下载任务" in downloadtext:
            self.ele_mgr(60, lambda x: x.find_element_by_id('com.baidu.appsearch:id/title_action2')).click()
            for i in self.findids("com.baidu.appsearch:id/deletebtn",20):
                el = self.findClassText("android.widget.Button","删除")
                if el:
                    self.findClassText("android.widget.Button", "删除").click()
                    self.ele_mgr(20, lambda x: x.find_element_by_id('com.baidu.appsearch:id/libui_cancel')).click()
            # el = self.findid("com.baidu.appsearch:id/downloaded_none_text", 10)
            # if el is None:
            #     print("删除全部的下载任务")
            #     return 'true'
        elc = self.findid("com.baidu.appsearch:id/downloading_title",10)
        if elc:
            downloadtext = self.findid("com.baidu.appsearch:id/downloading_title",10).text
            if "未安装" in downloadtext:
                self.ele_mgr(20, lambda x: x.find_element_by_id('com.baidu.appsearch:id/title_action2')).click()
                self.ele_mgr(20, lambda x: x.find_element_by_id('com.baidu.appsearch:id/downloading_title_action')).click()
                self.findid("com.baidu.appsearch:id/libui_cancel", 20).click()
        el= self.findid("com.baidu.appsearch:id/downloaded_none_text",10)
        if el is None:
            print("删除安装包失败")
            return 'false'
        else:
            print("删除安装包成功")
    #         下载暂停或无法下载时删除该任务
    # def downloadingdelet(self):

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
    test_apps = []
    test_app_4g = []
    # test_apps = ['爱看', '快视频', '腾讯wifi管家', 'wifi万能钥匙', '好运万年历']
    try:
        y = baidu(test_apps, test_app_4g)
        y.start_test()
    except Exception:
        print("360异常")
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback)
    print("等待五分钟")
    # time.sleep(5 * 60)