#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import subprocess
import sys
import time
import traceback
import unittest
import requests
import random
import db_helper
import datetime
from attr import attrs
from ui import UIman


class mm(UIman):

    def setup_init(self):
        print("mm setup_init")
        return attrs.mmattr

    def test_a_run(self):
        print('mm 开始start_test')
        print(self.driver.network_connection)
        try:
            self.driver.open_notifications()
            self.findid("com.android.systemui:id/toolbox_bt").click()
            self.findxpath("//android.widget.GridView[@resource-id='com.android.systemui:id/grid_view']/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ImageView[1]").click()
            time.sleep(1)
            self.findxpath("//android.widget.GridView[@resource-id='com.android.systemui:id/grid_view']/android.widget.LinearLayout[5]/android.widget.LinearLayout[1]/android.widget.ImageView[1]").click()
            time.sleep(1)
            self.driver.press_keycode(3)
            print('ui操作后网络状态：')
            print(self.driver.network_connection)
            if self.driver.network_connection == 0:
                print("等于0")
                self.driver.open_notifications()
                self.findid("com.android.systemui:id/toolbox_bt").click()
                self.findxpath("//android.widget.GridView[@resource-id='com.android.systemui:id/grid_view']/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ImageView[1]").click()
                time.sleep(1)
                self.driver.press_keycode(3)
        except Exception:
            print("设置数据网络出现了问题,本轮不测试数据网络")
            return 'false'
        print("更改后网络为：")
        time.sleep(1)
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
            print('开始关掉app')
            self.closeapp()
            time.sleep(3)
            # def screenShot(self, name):
            # time_str = time.strftime('_%m%d_%H%M', time.localtime(time.time()))
            # folder = os.path.abspath(os.path.join(os.path.dirname(__file__), ".")) + '\\screenshots\\'
            # if not self.driver.get_screenshot_as_file(folder + name + time_str + ".png"):
            # print("screenshot error:",name)
        # print("testvar")
        # print(testvar)
        # global testvar
        # testvar = "MM"
        # print("testvar")
        # print(testvar)
        # time.sleep(10*60)

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
            el2 = self.findid("com.aspire.mm:id/search_text_view")
            if el2 is None:
                return 'false'
            el2.click()
            el = self.findid("com.aspire.mm:id/searchText")
            if el is None:
                return 'false'
            s = self.test_app_name
            el.send_keys(s)
            print(s)
            self.clickid("com.aspire.mm:id/searchButton")
            start_time = time.time()
            el = self.findid_for_search("com.aspire.mm:id/interested")
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
                self.driver.press_keycode(4)
                return 'false'
        # except Exception:
        #     exc_type, exc_value, exc_traceback = sys.exc_info()
        #     traceback.print_exception(exc_type, exc_value, exc_traceback)
        #     return 'false'

    def download(self):
    #     el = self.findid("com.aspire.mm:id/search_hot_flowview", 8)
    #     el2 = self.findxpath("//android.widget.ListView[@resource-id='android:id/list']/android.widget.RelativeLayout[2]")
        el2 = self.findxpath("//android.widget.ListView[@resource-id='android:id/list']/android.widget.RelativeLayout[1]")
        if el2:
            el2.click()
        else:
            return 'false'
        ell = self.findid("com.aspire.mm:id/download_btn", 30)
        if ell is None:
            print('没找到download_btn，return false')
            return 'false'
        el = self.findxpath("//android.widget.RelativeLayout[@resource-id='com.aspire.mm:id/footer_bar']//android.widget.TextView[contains(@text,'下载   ')]", 20)
        if el is None:
            print('app不符合要求，本轮不测试下载，return false')
            return 'false'
        app_size = el.text.replace(u'下载', '').replace(u' ', '').replace(u'M', '')
        el.click()
        start_time = time.time()
        # el = self.findClassText1("android.widget.TextView", "安装")
        el = self.findid("com.android.packageinstaller:id/cancel_button", 60)
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
            db_helper.insert_data("mm_2018", self.data_dict)
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
        # try:
            re = self.exc_command("rm -f /sdcard/mm/download/*")
            # re = self.exc_command("rm -f /sdcard/mm/cache/*")
            print('删除之前下载的安装包：正常')
            self.findid("com.aspire.mm:id/mgr_icon").click()
            el = self.findid("com.aspire.mm:id/iknow", 5)
            if el:
                el.click()
            # self.findid("//android.widget.TabWidget[@resource-id='android:id/tabs']/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]").click()
            el = self.findid("com.aspire.mm:id/downloadDelButton", 10)
            if el:
                el.click()
                self.findid("com.aspire.mm:id/button2").click()
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
    unittest.main()
    # 运行所有的测试用例