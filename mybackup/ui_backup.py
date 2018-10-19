#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import re
import sys
import time
import traceback
import unittest
from appium import webdriver
import xlrd
import xlwt

from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
import xlutils.copy

TIMEOUT = 30
TIMEGAP = 0.5

__all__ = ['UIman']


class UIman(unittest.TestCase):
    # def setup_init(self):
    #     print("UIman setup_init")
    #     return []

    def setup_init(self):
        print("UIman setup_init")
        return super.setup_init()

    def setUp(self):
        print("UIman setUp")
        self.attrs = self.setup_init()
        self.network = ''
        self.test_app_name = ''
        # self.test_apps = ['wifi万能钥匙', "作业帮"]
        self.test_apps = ['qq', '微信', 'wifi万能钥匙', '快手', '支付宝', '宜搜小说', '作业帮', '美团', '饿了么']
        self.test_apps_dic = []
        self.data_dict = {
            "product_name": "MM",
            "client": "android",
            "bussiness": "",
            "data_type": "",
            "data_value": "",
            "network": "",
            "remark": "",
            "test_time": ""
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4735/wd/hub',  self.attrs[0])
        print(self.driver)
        print(self.attrs[0]["appPackage"])

    def tearDown(self):
        print("UIman tearDown")
        self.driver.quit()

    # def setdriver(self, driver=None):
    #     self.driver = driver

    def longtouch(self, el):
        act = TouchAction(self.driver)
        act.long_press(el, None, None, duration=3000).perform()
        return el

    def searchIdMap(self, idmap):
        for i, v in idmap.items():
            try:
                el = self.driver.find_element_by_id(id)
                return i, el
            except NoSuchElementException:
                pass
            except Exception:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                traceback.print_exception(exc_type, exc_value, exc_traceback)
                print(idmap)
        return None

    def searchClassList(self, classname):
        time.sleep(2)
        return self.driver.find_elements_by_class_name(classname)

    def findidAndIdClick(self, id, id2, timeout=TIMEOUT):
        while timeout > 0:
            try:
                time.sleep(0.2)
                el = self.driver.find_element_by_id(id)
                return el
            except NoSuchElementException:
                print(' 找不到元素1')
                try:
                    el = self.driver.find_element_by_id(id2)
                    if el:
                        el.click()
                except NoSuchElementException:
                    print(' 找不到元素2 ')
                except Exception:
                    print (' 找元素2 Exception')
                timeout -= 1
                print ('时间减1')
            except Exception:
                print (' 找元素1 Exception')
                # exc_type, exc_value, exc_traceback = sys.exc_info()
                # traceback.print_exception(exc_type, exc_value, exc_traceback)
                # print(id)
                pass
        return None
    def find_text_in_id(self, id, text1, id2, timeout=TIMEOUT):
        print("开始找元素")
        while timeout > 0:
            try:
                time.sleep(TIMEGAP)
                tt1 = time.time()
                el = self.driver.find_element_by_id(id)
                if el.text == text1:
                    return 'true'
                e2 = self.driver.find_element_by_id(id2)
                return 'true'
            except NoSuchElementException:
                t1 = time.time() - tt1
                if t1 > timeout:
                    print(t1)
                    print("超时")
                    return None
                timeout = timeout - 1
            except Exception:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                traceback.print_exception(exc_type, exc_value, exc_traceback)
                print("find_text_in_id 过程中出现了异常")
                print(id)
                print(self.driver)
                raise RuntimeError('testError')
        return None

    def findid(self, id, timeout=TIMEOUT):
        while timeout > 0:
            try:
                time.sleep(TIMEGAP)
                el = self.driver.find_element_by_id(id)
                return el
            except NoSuchElementException:
                timeout -= 1
            except Exception:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                traceback.print_exception(exc_type, exc_value, exc_traceback)
                print("查找此id过程中出现了异常")
                print(id)
                print(self.driver)
                raise RuntimeError('testError')
        return None

    def findid_for_search(self, id, timeout=TIMEOUT):
        while timeout > 0:
            try:
                # time.sleep(TIMEGAP)
                el = self.driver.find_element_by_id(id)
                return el
            except NoSuchElementException:
                timeout -= 1
            except Exception:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                traceback.print_exception(exc_type, exc_value, exc_traceback)
                print("查找此id过程中出现了异常")
                print(id)
                print(self.driver)
                raise RuntimeError('testError')
        return None

    def findidyyb(self, id, timeout=TIMEOUT):
        print("开始找元素")
        while timeout > 0:
            try:
                time.sleep(1)
                tt1 = time.time()
                el = self.driver.find_element_by_id(id)
                return el
            except NoSuchElementException:
                print(time.time() - tt1)
                timeout -= 1
            except Exception:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                traceback.print_exception(exc_type, exc_value, exc_traceback)
                print("应用宝，查找此id过程中出现了异常")
                print(id)
                print(self.driver)
                raise RuntimeError('testError')
        return None

    def clickid(self, id, timeout=TIMEOUT):
        el = self.findid(id, timeout)
        if el:
            el.click()
        else:
            self.screenShot("clickid_" + self._parseid(id))
        return None

    def findids(self, timeout=TIMEOUT):
        while timeout > 0:
            try:
                time.sleep(TIMEGAP)
                el = self.driver.find_elements_by_id(id)
                return el
            except NoSuchElementException:
                timeout -= 1
            except Exception:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                traceback.print_exception(exc_type, exc_value, exc_traceback)
                print("findids 过程中出现 了异常")
                print(id)
                print(self.driver)
                raise RuntimeError('testError')
        return None

    def findIdText(self, id, text, timeout=TIMEOUT):
        while timeout > 0:
            try:
                time.sleep(TIMEGAP)
                els = self.driver.find_elements_by_id(id)
                for el in els:
                    if el.text == text:
                        return el
                timeout -= 1
            except NoSuchElementException:
                timeout -= 1
            except Exception:
                # exc_type, exc_value, exc_traceback = sys.exc_info()
                # traceback.print_exception(exc_type, exc_value, exc_traceback)
                # print(id)
                # print(text)
                pass
        self.screenShot("findIdText_" + self._parseid(id))
        return None

    def findClassText1(self, classname, text, timeout=TIMEOUT):
        while timeout > 0:
            try:
                time.sleep(0.3)
                els = self.driver.find_elements_by_class_name(classname)
                print(els[len(els)-1].text)
                timeout -= 1
                if "安装" == els[len(els)-1].text:
                    return 'true'
                el = self.driver.find_element_by_id("com.android.packageinstaller:id/cancel_button")
                return 'true'
            except NoSuchElementException:
                timeout -= 1
                print(str(classname)+text+str(classname))
            except Exception:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                traceback.print_exception(exc_type, exc_value, exc_traceback)
                print(classname)
                print(text)
        return None
    def findClassText(self, classname, text, timeout=TIMEOUT):
        while timeout > 0:
            try:
                time.sleep(TIMEGAP)
                els = self.driver.find_elements_by_class_name(classname)
                for el in els:
                    if text in el.text:
                        return el
                timeout -= 1
            except NoSuchElementException:
                timeout -= 1
                print (str(classname)+text+str(classname))
            except Exception:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                traceback.print_exception(exc_type, exc_value, exc_traceback)
                print(classname)
                print(text)
        return None

    def findIdTextIn(self, id, text, timeout=TIMEOUT):
        while timeout > 0:
            try:
                time.sleep(TIMEGAP)
                els = self.driver.find_elements_by_id(id)
                for el in els:
                    if text in el.text:
                        return el
                timeout -= 1
            except NoSuchElementException:
                timeout -= 1
            except Exception:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                traceback.print_exception(exc_type, exc_value, exc_traceback)
                print(id)
                print(text)
        return None

    def writeToExcel(self, data, filename, sheetname):
        if os.path.exists(filename):
            self.writeOldExcel(data, filename, sheetname)
        else:
            self.writeNewExcel(data, filename, sheetname)

    def writeNewExcel(self, data, filename, sheetname):
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet(sheetname, cell_overwrite_ok=True)
        l = len(data)
        for i in range(l):
            worksheet.write(0, i, str(data[i]))
        workbook.save(filename)

    def writeOldExcel(self, data, filename, sheetname):
        oldWb = xlrd.open_workbook(filename)
        newWb = xlutils.copy(oldWb)
        if sheetname in oldWb.sheet_names():
            rows = oldWb.sheet_by_name(sheetname).nrows
            newWs = newWb.get_sheet(sheetname)
        else:
            newWs = newWb.add_sheet(sheetname, cell_overwrite_ok=True)
            rows = 0
        l = len(data)
        for i in range(l):
            newWs.write(rows, i, str(data[i]))
        newWb.save(filename)

    def findxpath(self, xpath, timeout=TIMEOUT):
        while timeout > 0:
            try:
                time.sleep(TIMEGAP)
                el = self.driver.find_element_by_xpath(xpath)
                return el
            except NoSuchElementException:
                # if (timeout >= 15 and timeout % 15 == 0):
                timeout = timeout-TIMEGAP
                if timeout < 1:
                    print('------ not find xpath :', xpath)
                    # exc_type, exc_value, exc_traceback = sys.exc_info()
                    # traceback.print_exception(exc_type, exc_value, exc_traceback)
            except Exception:
                # pass
                exc_type, exc_value, exc_traceback = sys.exc_info()
                traceback.print_exception(exc_type, exc_value, exc_traceback)
                print("findxpath 过程中出现了其他异常")
                print(self.driver)
                raise RuntimeError('testError')
        return None

    def screenShot(self, name):
        time_str = time.strftime('_%m%d_%H%M', time.localtime(time.time()))
        folder = os.path.abspath(os.path.join(os.path.dirname(__file__), ".")) + '\\screenshots\\'
        print("folder--> "+str(folder)+"  "+str(folder + name + time_str + ".png"))
        if not self.driver.get_screenshot_as_file(folder + name + time_str + ".png"):
            print("screenshot error:", name)
        return 'false '

    def _parseid(self, name):
        if name.find("/") > 0 or name.find(".") > 0:
            m = re.search("[a-zA-Z0-9]+$", name)
            return m.group()

    def exc_command(self,command):
        result = self.driver.execute_script('mobile: shell', {
            'command': command,
            'args': [''],
            'includeStderr': False,
            'timeout': 5000
        })
        return result