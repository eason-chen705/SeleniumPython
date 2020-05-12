#coding=utf-8
import unittest
class FirstCase02(unittest.TestCase):
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
    def testfirst001(self):
        print("case001")
    def testfirst002(self):
        print("case002")
    def testfirst003(self):
        print("case003")

if __name__ == "__main__":
    #unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(FirstCase02('testfirst002'))
    suite.addTest(FirstCase02('testfirst001'))
    suite.addTest(FirstCase02('testfirst003'))
    unittest.TextTestRunner().run(suite)
