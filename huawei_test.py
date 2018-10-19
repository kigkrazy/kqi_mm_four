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

class huawei(UIman):

    def __init__(self, test_apps, test_app_4g):
        print("huawei __init__")
        self.limit_size = attrs.limit_size_4g
        self.attrs = attrs.hwattr
        # self.test_apps = ['爱看', '快视频', '腾讯wifi管家', 'wifi万能钥匙', '好运万年历']
        self.test_apps = test_apps
        self.test_apps_4g = test_app_4g
        self.network = ''
        self.test_app_name = ''
        self.test_apps_dic = []
        self.data_dict = {
            "product_name": "HW",
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
        self.dl_app_name = ""

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
        print('华为 开始start_test')
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
        time.sleep(2)
        length = 0
        if len(self.test_apps) == 0:
            print("华为手机助手需要选app")
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
        # funcs = [self.startup, self.search, self.download]
        funcs = [self.startup, self.deletepackage, self.search, self.download]
        print("华为应用市场需要跑 " + str(length) + " 次")
        for x in range(length):
            print("=============开始第" + str(x + 1) + "次测试====================")
            self.test_app_name = self.test_apps_dic[x]
            for  f in funcs:
                print('---------开始执行函数：'+str(f.__name__)+'--------------')
                try:
                    result = f()
                    if result == 'false':
                        # result = 'false ' + self.screenShot(f.__name__)
                        print(str(f.__name__)+'返回false,break')
                        self.screenShot(f.__name__ + "_false_hw")
                        break
                except WebDriverException:
                    print("将异常抛到start_test,结束测试")
                    raise
                except Exception:
                    exc_type, exc_value, exc_traceback = sys.exc_info()
                    traceback.print_exception(exc_type, exc_value, exc_traceback)
                    self.screenShot(f.__name__ + "_error_hw")
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
        self.startup()
        self.deletepackage()

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
        if current_activity == u'.MarketActivity':
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
        self.driver.close_app()
        time.sleep(2)
        self.driver.launch_app()
        #el2 =self.ele_mgr(20, lambda x: x.find_element_by_id('com.huawei.appmarket:id/search_edit_text'))
        el2 = self.ele_mgr(20, lambda x: x.find_element_by_id('com.huawei.appmarket:id/fixed_search_view'))
        # el2 = self.findid("com.tencent.android.qqdownloader:id/awt")
        if el2:
            el2.click()
        else:
            return 'false'
        print(self.test_app_name)
        #el = self.ele_mgr(20, lambda x: x.find_element_by_id('com.huawei.appmarket:id/searchText'))
        el = self.ele_mgr(20, lambda x: x.find_element_by_id('android:id/search_src_text'))
        # el = self.findid("com.tencent.android.qqdownloader:id/yv")
        if el is None:
            return 'false'
        el.send_keys(self.test_app_name)
        #self.clickid("com.huawei.appmarket:id/search_title_icon_layout")
        self.clickid("com.huawei.appmarket:id/search_text_button")
        start_time = time.time()

        # el = self.ele_mgr_forserch(20, lambda x: x.find_element_by_id('com.tencent.android.qqdownloader:id/wt'))
        el = self.findid_for_search("com.huawei.appmarket:id/ItemTitle")
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
            if self.driver.current_activity == ".MarketActivity" or rt_time > 10:
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
        # except NoSuchElementException:
            # exc_type, exc_value, exc_traceback = sys.exc_info()
            # traceback.print_exception(exc_type, exc_value, exc_traceback)
            # return 'false'

    def download(self):
        #el = self.ele_mgr(20, lambda x: x.find_element_by_id('com.huawei.appmarket:id/ItemText'))
        temp_text = self.ele_mgr(20, lambda x: x.find_element_by_id('com.huawei.appmarket:id/ItemTitle')).text
        elh = self.ele_mgr(20, lambda x: x.find_element_by_id('com.huawei.appmarket:id/ItemTitle'))
        elh.click()
        el = self.ele_mgr(20, lambda x: x.find_element_by_id('com.huawei.appmarket:id/detail_appinfo_size_textview'))
        app_size = el.text.replace(u'MB','').replace(u' ','').replace(u'KB','')
        print(type(app_size))
        f_app_size = float(app_size)
        print(f_app_size)
        #self.driver.press_keycode(4)
        if f_app_size < 20.0:
            print("小于20M不下")
            return 'true'
        if self.network == '4G':
            if f_app_size > self.limit_size:
                print("大于50, 4G环境不下载")
                return 'true'
        #temp_text = self.ele_mgr(20, lambda x: x.find_element_by_id('com.huawei.appmarket:id/ItemTitle')).text()
        #self.ele_mgr(20, lambda x: x.find_element_by_id('com.huawei.appmarket:id/ItemTitle')).click()
        # temp_text = self.ele_mgr(10, lambda x: x.find_element_by_id('com.huawei.appmarket:id/detail_head_app_name_textview')).text
        # el2 = self.ele_mgr(20, lambda x: x.find_element_by_id('com.huawei.appmarket:id/detail_download_button'))
        # if el2 is None:
        #     print("not find")
        #     return 'false'
        # text_in_download = el2.get_attribute("name")
        # print(text_in_download)
        #ele2 =self.findxpath("//android.view.View[@resource-id='com.huawei.appmarket:id/detail_download_button' and @content-desc='安装']",20)
        ele2 = self.findxpath(
            "//android.widget.ProgressBar[@resource-id='com.huawei.appmarket:id/hwDownloadProgress']",20)
        if ele2:
            print("xpath找到")
            self.dl_app_name = temp_text
            ele2.click()

            start_time = time.time()
        else:
            print('不含下载，return')
            return 'false'
        kl =self.ele_mgr(4, lambda x: x.find_element_by_id('android:id/button1'))
        # 761,1507
        # kl = self.findid("android:id/button1", 4)
        if kl:
            print('点击继续下载')
            kl.click()
            start_time = time.time()
        #ele2 = self.findxpath(
         #   "//android.view.View[@resource-id='com.huawei.appmarket:id/detail_download_button' and @content-desc='安装中']",120)
        ele2 = self.findxpath(
            "//android.widget.TextView[@resource-id='com.huawei.appmarket:id/hwdownload_percentage' and @text='打开']",80)
        rt_time = time.time() - start_time
        print(rt_time)
            # 省心装"com.tencent.android.qqdownloader:id/a30" 取消,不清缓存的话只提示一次
            # "com.tencent.android.qqdownloader/com.tencent.pangu.activity.AppDetailActivityV5"
            # 安装"com.android.packageinstaller:id/ok_button"  取消"com.android.packageinstaller:id/cancel_button"
        if ele2:
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
            # time.sleep(10)
            # if self.driver.current_activity == u'.PackageInstallerActivity':
            #     self.clickid("com.android.packageinstaller:id/cancel_button")
            #     print('找到 PackageInstallerActivity ,现在按返回 ')
            #ele2 = self.findxpath(
             #   "//android.widget.ProgressBar[@resource-id='com.huawei.appmarket:id/hwDownloadProgress' and @content-desc='打开']", 60)
            if ele2:
                print('安装完成')
            else:
                print('安装未完成')
            # self.driver.press_keycode(4)
            # time.sleep(1)
            print('下载：正常')
            return 'OK'
        else:
            print(rt_time)
            kl = self.ele_mgr(4, lambda x: x.find_element_by_id('com.huawei.appmarket:id/detail_download_cancel_imageview'))
            if kl:
                kl.click()
            print('秒内没找到安装中，下载未完成')
            return 'false'

    def deletepackage(self):
        # el = self.findids("com.huawei.appmarket:id/tab_name")
        # # print(el)
        # for ele in el:
        #     # print(ele.text)
        #     if ele.text == '管理':
        #         print('找到管理')
        #         ele.click()
        #         break
        #self.findxpath("//android.widget.TextView[@resource-id='com.huawei.appmarket:id/tab_name' and @text='管理']", 20).click()
        self.findxpath("//android.widget.TextView[@resource-id='com.huawei.appmarket:id/content' and @text='管理']",
                       20).click()
        el = self.findids("com.huawei.appmarket:id/setItemTitle")
        for ele in el:
            if ele.text == '安装管理':
                print('找到安装管理')
                ele.click()
                break
        # "没下载完""com.huawei.appmarket:id/expand_arrow_view1"
        ele2 = self.ele_mgr(3, lambda x: x.find_element_by_id('com.huawei.appmarket:id/record_operate_textview'))
        if ele2:
            ele2.click()
        #     view1是暂停的任务或者正在安装的任务， view2是还在下载的任务
        ele2 = self.ele_mgr(10, lambda x: x.find_element_by_id('com.huawei.appmarket:id/expand_arrow_view1'))
        if ele2:
            print('安装中')
            self.driver.find_element_by_id('com.huawei.appmarket:id/expand_arrow_view1').click()
            ele3 =self.ele_mgr(20, lambda x: x.find_element_by_id('com.huawei.appmarket:id/delete_button'))
            if ele3:
                ele3.click()
                time.sleep(5)
        for k in range(0, 3):
            ec = self.ele_mgr(20, lambda x: x.find_element_by_id('com.huawei.appmarket:id/localpackage_item_name_view'))
            app_text = ec.text
            if "Unlock" in app_text or u"Unlock" in app_text:
                print('没有需要卸载的app了')
                break
            else:
                if "Appium" in app_text or u"Appium" in app_text:
                    print('没有需要卸载的app了')
                    break
                time.sleep(2)
                ec = self.ele_mgr(10, lambda x: x.find_element_by_id('com.huawei.appmarket:id/localpackage_item_name_view'))
                app_text = ec.text
                if "Unlock" in app_text or u"Unlock" in app_text:
                    print('没有需要卸载的app了')
                    break
                print("开始卸载 "+str(app_text))
                self.ele_mgr(20, lambda x: x.find_element_by_id('com.huawei.appmarket:id/localpackage_item_date_arrow')).click()
                el3 = self.ele_mgr(20, lambda x: x.find_element_by_id('com.huawei.appmarket:id/localpackage_option_button'))
                if el3:
                    self.driver.find_element_by_id('com.huawei.appmarket:id/localpackage_option_button').click()
                else:
                    return 'false'
                self.ele_mgr(20, lambda x: x.find_element_by_id('android:id/button1')).click()
                time.sleep(6)
                el3 = self.ele_mgr(3, lambda x: x.find_element_by_id('android:id/button1'))
                if el3:
                    el3.click()
                ec1 = self.ele_mgr(20, lambda x: x.find_element_by_id('com.huawei.appmarket:id/localpackage_item_name_view'))
                app_text_aff = ec1.text
                if app_text_aff == app_text:
                    print('卸载'+app_text+'失败')
                    # return 'false'
                else:
                    print('卸载'+app_text+'成功')
        print('返回')
        return 'true'
        # self.driver.press_keycode(4)
        # time.sleep(2)
        # cur_acti = self.driver.current_activity
        # print(cur_acti)
        # if cur_acti == u".MarketActivity":
        #     print("回到首页")
        # self.findxpath("//android.widget.TextView[@text='推荐']").click()
        # print('删除之前下载的安装包：正常')


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
    test_apps_4g= []
    # test_apps = [ u'爱看',u'乐趣', u'快视频']
    # test_apps = ['爱看', '快视频', '腾讯wifi管家', 'wifi万能钥匙', '好运万年历']
    try:
        y = huawei(test_apps,test_apps_4g)
        y.start_test()
    except Exception:
        print("华为异常")
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback)
    print("等待五分钟")
    # time.sleep(5 * 60)