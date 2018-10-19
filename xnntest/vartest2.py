import unittest as unittest

from attr.testGlobal import global_var


class testvar2(unittest.TestCase):
    def setUp(self):
        print(" testvar2 setUp")
    def tearDown(self):
        print('testvar2 testDown')
    def test_all(self):
        print("test_all")
        print(global_var.getdict())
        global_var.setdict(['ll', 'mm'])
        print(global_var.getdict())



if __name__ == '__main__':
    unittest.main