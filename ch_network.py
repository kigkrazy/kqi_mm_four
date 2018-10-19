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
from attr import attrs
from ui import UIman
import yyb_test
class change_nk(UIman):

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
    def change_network(self):
        print(self.driver.network_connection)
        self.driver.open_notifications()
        self.findid("com.android.systemui:id/toolbox_bt").click()
        self.findxpath(
            "//android.widget.GridView[@resource-id='com.android.systemui:id/grid_view']/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ImageView[1]").click()
        time.sleep(2)
        self.findxpath(
            "//android.widget.GridView[@resource-id='com.android.systemui:id/grid_view']/android.widget.LinearLayout[5]/android.widget.LinearLayout[1]/android.widget.ImageView[1]").click()
        time.sleep(3)
        self.screenShot("network_status")
        self.driver.press_keycode(3)
        print('ui操作后网络状态：')
        print(self.driver.network_connection)
        if self.driver.network_connection == 0:
            print("等于0")
            self.driver.open_notifications()
            self.findid("com.android.systemui:id/toolbox_bt").click()
            self.findxpath(
                "//android.widget.GridView[@resource-id='com.android.systemui:id/grid_view']/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ImageView[1]").click()
            time.sleep(1)
            self.driver.press_keycode(3)

if __name__ == '__main__':
    test_apps = []
    try:
        t = change_nk()
        t.change_network()
    except Exception:
        print("设置数据网络出现了问题,本轮不测试数据网络")
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback)
