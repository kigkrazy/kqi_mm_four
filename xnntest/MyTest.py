import os
import time
import unittest

from xnntest import mydriver


class MyTest(unittest.TestCase):  # 继承unittest.TestCase
    def tearDown(self):
        # 每个测试用例执行之后做操作
        print('tearDown')

    def setup_init(self):
        print("yyb setup_init")
        return super.setup_init()

    def setUp(self):
        # 每个测试用例执行之前做操作
        self.driver = mydriver.get_driver()
        print('setUp')

    # @classmethod
    # def tearDownClass(self):
    #     # 必须使用 @ classmethod装饰器, 所有test运行完后运行一次
    #     print('tearDownClass')
    #
    # @classmethod
    # def setUpClass(self):
    #     # 必须使用@classmethod 装饰器,所有test运行前运行一次
    #     print('setUpClass')
    def screenShot(self, name):
        time_str = time.strftime('_%m%d_%H%M', time.localtime(time.time()))
        folder = os.path.abspath(os.path.join(os.path.dirname(__file__), ".")) + '\\screenshots\\'
        if not self.driver.get_screenshot_as_file(folder + name + time_str + ".png"):
            print("screenshot error:", name)
        else:
            print("screenshot success")

    def test_a_run(self):
        print("test_a_run")
        # screen_dir=os.path.dirname(os.path.realpath(__file__))
        # print(screen_dir)
        # result=self.driver.get_screenshot_as_file(screen_dir+"\\a.png")
        # print(result)
        # time.sleep(2)

        self.screenShot(__name__)



    # def test_b_run(self):
    #     print("test_b_run")
    #     self.assertEqual(2, 2)  # 测试用例


if __name__ == '__main__':
    unittest.main()  # 运行所有的测试用例