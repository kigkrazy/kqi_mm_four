import subprocess
import sys
import time
import traceback
import requests
import random

from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import WebDriverException

import db_helper
import datetime

from appium import webdriver
from attr import attrs
from ui import UIman
import yyb_test
class check_nk(UIman):

    def __init__(self):
        print("mm setup_init")
        self.attrs = attrs.mmattr
        self.network = ''
        self.test_app_name = ''
        self.test_apps = []
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
        self.change_network()
        if self.driver is not None:
            print("tearDown")
            self.driver.quit()
        else:
            print("driver is None")
        # except Exception:
        #     print("MM test_a_run 应该是webDriverException异常,不执行quit,结束测试")
        #     exc_type, exc_value, exc_traceback = sys.exc_info()
        #     traceback.print_exception(exc_type, exc_value, exc_traceback)
    def check_network(self):
        print(self.driver.network_connection)
        self.driver.open_notifications()
        self.findid("com.android.systemui:id/toolbox_bt").click()
        self.screenShot("check_network_status")
        self.findxpath("//android.widget.GridView[@resource-id='com.android.systemui:id/grid_view']/android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.ImageView[1]",15).click()
        elc=self.findxpath("//android.widget.TextView[@text='WLAN']",15)
        if elc is None:
            print("没有找到wlan")
            self.screenShot("not find wlan")
            return
        elc.click()
        # //android.widget.TextView[@text='CMCC-Prpy']
        # //android.widget.TextView[@text='H3C2']
        ele=self.findxpath("//android.widget.TextView[@text='H3C']",10)
        if ele is None:
            self.findxpath("//android.widget.Switch[@resource-id='android:id/switchWidget']",15).click()
        ele=self.findxpath("//android.widget.TextView[@text='H3C']",10)
        if ele is None:
            print("开启网络后，还是没有找到h3c")
            self.screenShot("not find h3c")
            return
        ele.click()

        elc=self.findid("com.android.settings:id/password",15)
        if elc is None:
            print("没找到密码框")
            ecq = self.findid("android:id/button1")
            if ecq:
                ecq.click()
                time.sleep(2)
            return
        elc.send_keys("aaaa1111")
        ele=self.findid("com.android.settings:id/btn_wifi_connect",15)
        if ele is None:
            print("没找到连接按钮")
            self.screenShot("not find connect button")
            return
        ele.click()
        time.sleep(10)
        self.screenShot("change_network_succOrNot")
        # # print("网络截图")
        # self.screenShot("network_after_change_")
        # time.sleep(2)
        # elc= self.findxpath(
        #     "//android.widget.GridView[@resource-id='com.android.systemui:id/grid_view']/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ImageView[1]").click()
        # ta=TouchAction()
        # ta.long_press(elc,3000)

        # self.driver.press_keycode(3)
        # print('ui操作后网络状态：')
        # print(self.driver.network_connection)
        # if self.driver.network_connection == 0:
        #     print("等于0")
        #     self.driver.open_notifications()
        #     self.findid("com.android.systemui:id/toolbox_bt").click()
        #     self.findxpath(
        #         "//android.widget.GridView[@resource-id='com.android.systemui:id/grid_view']/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ImageView[1]").click()
        #     time.sleep(1)
        #     self.driver.press_keycode(3)

if __name__ == '__main__':
    test_apps = []
    try:
        t = check_nk()
        t.check_network()
    except Exception:
        print("设置数据网络出现了问题,本轮不测试数据网络")
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback)
