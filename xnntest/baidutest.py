import datetime
import random
import subprocess
import sys
import time
import traceback

import requests
from appium.webdriver import webdriver
from selenium.common.exceptions import WebDriverException

from attr import attrs
from ui import UIman


class baidu(UIman):
    def __init__(self):
        print("baidu setup_init")
        self.attrs = attrs.hwattr
        self.test_apps = test_apps
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
        print('------------paodao zheli le --------------')
        print(self.driver)
        print(self.attrs[0]["appPackage"])

    def start_test(self):
        # if len(self.test_apps) == 1:
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
        if len(self.test_apps) == 1:
            print("百度需要选app")
            self.selectAPPS()
            length = len(self.test_apps)
            print('len1: ' + str(length))
            self.selectAPPS()
            length = len(self.test_apps)
            print('len2: ' + str(length))
        length = len(self.test_apps)
        if length < 3:
            print("app长度小于3返回")
            return
        if self.network == '4G':
            self.test_apps_dic = self.test_apps[(length-2): length]
        else:
            self.test_apps_dic = self.test_apps[:]
        length = len(self.test_apps_dic)
        # funcs = [self.startup, self.deletepackage, self.search]
        funcs = [self.startup, self.search, self.download]
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
                except WebDriverException:
                    print("将异常抛到start_test,结束测试")
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

        # soft_sortdetail_v1 = {'影音工具': '678936512', '社区交友': '678936511','系统工具': '678936514', '网络视频': '678936530', '网络购物':'678936527'}
        soft_sortdetail_v1 = {'影音工具': '678936512', '社区交友': '678936511', '系统工具': '678936514', '网络视频': '678936530',
                              '网络购物': '678936527', '摄影录像': '678936523', '安全防护': '678936516', '报刊杂志': '678936534',
                              '餐饮美食': '678936536',
                              '电子书籍': '678936519', '儿童应用': '678936532', '健康医疗': '678936528', '交通导航': '678936522',
                              '教育教学': '678936525',
                              '金融理财': '678936531', '卡通动漫': '678936535', '浏览器': '678936515', '旅游出行': '678936524',
                              '美化壁纸': '678936517',
                              '商务办公': '678936526', '生活助手': '678936513', '输入法': '678936520', '数字音乐': '678936533',
                              '通话通信': '678936521',
                              '新闻资讯': '678936529', '娱乐八卦': '678936518'}
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
            print(self.test_apps)

        except Exception:
            return 'false'

    def startup(self):
        # try:
            self.driver.launch_app()
            time.sleep(5)
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
    def search(self):
        # 搜索框
        el2=self.ele_mgr(20, lambda  x: x.find_element_by_id("com.baidu.appsearch:id/libui_titlebar_search_textinput"))
        if el2 is None:
            print('找不到搜索框')
            return "flase"
        el2.click()
#         输入搜索应用
        el= self.ele_mgr(20,lambda x:x.find_element_by_id("com.baidu.appsearch:id/libui_titlebar_search_textinput"))
        el.sendkey(self.test_app_name)
        el=self.ele_mgr(20, lambda x:x.find_element_by_id("com.baidu.appsearch:id/search_result_search"))
        if el is None:
            print('找不到搜索按钮')
            return  "flase"
        el.click()
        # 开始时间
        starttime = time.time()
        el = self.findid_for_search("com.baidu.appsearch:id/app_item")
        rt_time= time.time()- starttime
        print("百度手机助手的搜索时延为"+rt_time)
        if el:
            self.data_dict['bussiness'] = '搜索'
            self.data_dict['network'] = self.network
            self.data_dict['data_type'] = 'time_delay'
            self.data_dict['data_value'] = str(round(rt_time, 2))
            self.data_dict['test_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.data_dict['remark'] = self.test_app_name
            # print(self.driver.current_activity)
            if self.driver.current_activity != ".distribute.MainActivity" or rt_time > 10:
                self.data_dict['is_delete'] = '1'
            # print(self.data_dict)
            # db_helper.insert_data("mm_2018", self.data_dict)
            print('搜索：正常')
            return 'OK'
        else:
            self.driver.press_keycode(4)
            return 'false'
    #     下载时延
    def download(self):
        # 点击首个搜索结果
        el2=self.findid("com.baidu.appsearch:id/app_item")
        if el2 is None:
            print('找不到搜索结果')
            return  'flase'
        el2[0].click()
        # 点击下载按钮
        ell = self.ele_mgr(20, lambda x: x.find_element_by_id('com.baidu.appsearch:id/app_content_btn_control_text'))
        if ell is None:
            print('没找到app_content_btn_control_text，return false')
            return 'false'
        app_szie = self.findid("com.baidu.appsearch:id/app_content_btn_control_text").text
        if '下载' not in app_szie:
            print('app不符合要求，本轮不测试下载，return false')
            return  'flase'
        app_size = app_szie.text.replace(u'下载', '').replace(u' ', '').replace(u'M', '')
        f_app_size = float(app_size)
        print(f_app_size)
        if self.network == '4G':
            if f_app_size > 50.0:
                print("大于50, 4G环境不下载")
                return 'true'
        # 点击下载
        ell.click()
        start_time=time.time()
        el=self.findid("com.android.packageinstaller:id/cancel_button",80)
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
            # db_helper.insert_data("mm_2018", self.data_dict)
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




if __name__ == '__main__':
    test_apps = ['爱看', '快视频', '腾讯wifi管家', 'wifi万能钥匙', '好运万年历']
    for i in range(2000):
        print("------第" + str(i) + "遍-----------")
        try:
            y = baidu(test_apps)
            y.start_test()
        except Exception:
            print("360异常")
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback)
        print("等待五分钟")
        time.sleep(5 * 60)
