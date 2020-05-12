#coding=utf-8
import sys
import os
sys.path.append('D:\\www\\SeleniumPython')
from Business.register_business import RegisterBusiness
from selenium import webdriver
from Log.user_log import Userlog
import unittest
import HTMLTestRunner
import time


class FirstCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("pre-condition for all testcases")
        cls.file_name = "D:\\www\\SeleniumPython\\Image\\test001.png"
        #实例化log
        cls.log = Userlog()
        cls.logger = cls.log.get_log()

    @classmethod
    def tearDownClass(cls):
        print("post-condition for all testcases")
        cls.log.close_handle()
      

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://www.5itest.cn/register')
        self.logger.info("this is Chrome")
        
        #time.sleep(2)
        self.login = RegisterBusiness(self.driver)

    def tearDown(self):
        time.sleep(2)
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(os.getcwd()+"/Report/"+case_name+".png")
                print(case_name,file_path)
                self.driver.save_screenshot(file_path)

        print("case post-condition")
        #self.driver.save_screenshot()
        self.driver.close()
        
        

    def test_login_email_error(self):
        email_error = self.login.login_email_error('1uiu3xx3@qq.com','uss1','111111',self.file_name)
        print("----email_error---:",email_error)
        self.assertFalse(email_error)
        #if email_error == True:
            #print("-----register success,case failed")
    def test_login_username_error(self):
        username_error = self.login.login_name_error('1911@qq.com','ss','111111',self.file_name)
        self.assertFalse(username_error)

    def test_login_code_error(self):
        code_error = self.login.login_name_error('1011@qq.com','ss','111111',self.file_name)
        self.assertFalse(code_error)

    def test_login_password_error(self):
        password_error = self.login.login_password_error('1101@qq.com','ss','111111',self.file_name)
        self.assertFalse(password_error)

    def test_login_success(self):
        success = self.login.user_base('1011@qq.com','ss','111111',self.file_name)
        self.assertFalse(success)



'''
def main():
    first = FirstCase()
    first.test_login_code_error()
    first.test_login_email_error()
    first.test_login_password_error()
    first.test_login_username_error()
    first.test_login_success()
'''

if __name__ == '__main__':
    #unittest.main()
    file_path = os.path.join(os.getcwd()+"/Report/"+"first_Case.html")
    f = open(file_path,'wb')
    suite = unittest.TestSuite()
    suite.addTest(FirstCase('test_login_email_error'))
    #suite.addTest(FirstCase('test_login_username_error'))
    #suite.addTest(FirstCase('test_login_password_error'))
    #suite.addTest(FirstCase('test_login_code_error'))
    #suite.addTest(FirstCase('test_login_success'))
    #unittest.TextTestRunner().run(suite)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="This is first case report",description="this is our first test report",verbosity=2)
    runner.run(suite)
