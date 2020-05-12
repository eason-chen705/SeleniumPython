#coding=utf-8
import unittest
import os
#create one main run file, invoke all the cases from multiple testcase.py files.
class RunCase(unittest.TestCase):
    def test_case01(self):
        case_path = os.path.join(os.getcwd(),'Case')
        suite = unittest.defaultTestLoader.discover(case_path,'unittest_*.py')
        unittest.TextTestRunner().run(suite)
if __name__ == "__main__":
    unittest.main()