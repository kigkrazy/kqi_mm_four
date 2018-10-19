import unittest as unittest
from attr import testGlobal
from attr.testGlobal import global_var


class testvar1(unittest.TestCase):
    def setUp(self):
        print("setUp")
    def tearDown(self):
        print('testDown')
    def test_all(self):
        self.assertIs('uu', 'uu')
        # print("test_all")
        # print(global_var.getdict())
        # if global_var.getdict()[0] in 'll':
        #     raise RuntimeError(global_var.getdict()[0])
        # global_var.setdict(['ii','kk'])
        # print(global_var.getdict())


if __name__ == '__main__':
    unittest.main
