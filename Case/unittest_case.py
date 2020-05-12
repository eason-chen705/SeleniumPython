#coding=utf-8
import unittest
class FirstCase01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("pre-condition for all testcases")

    @classmethod
    def tearDownClass(cls):
        print("post-condition for all testcases")

    def setUp(self):
        print("case pre-condition")
    def tearDown(self):
        print("case post-condition")
    #@unittest.skip("case01 not execute")
    def testfirst01(self):
        print("case01")
    def testfirst02(self):
        print("case02")
    def testfirst03(self):
        print("case03")

if __name__ == "__main__":
    #unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(FirstCase01('testfirst02'))
    suite.addTest(FirstCase01('testfirst01'))
    suite.addTest(FirstCase01('testfirst03'))
    unittest.TextTestRunner().run(suite)
