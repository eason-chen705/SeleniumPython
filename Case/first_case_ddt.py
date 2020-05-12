#coding=utf-8
import ddt
import unittest
import sys
import os
sys.path.append('D:\\www\\SeleniumPython')
from Business.register_business import RegisterBusiness
from selenium import webdriver
import HTMLTestRunner
import time
from Util.excel_util import ExcelUtil
#获取excel中的data
ex = ExcelUtil()
data = ex.get_data()

#mailbox,username,password,code,error_element,error_message

@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://www.5itest.cn/register')
        self.login = RegisterBusiness(self.driver)
        #self.file_name = "D:\\www\\SeleniumPython\\Image\\test001.png"

    def tearDown(self):
        time.sleep(2)
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                #print(case_name)
                file_path = os.path.join(os.getcwd()+"\\Report\\"+case_name+".png")
                #print(case_name,file_path)
                self.driver.save_screenshot(file_path)
        print("case post-condition")
        #self.driver.save_screenshot()
        self.driver.close()
    '''
    @ddt.data(
    ['23','cyj01','111111','code','user_email_error','请输入有效的电子邮件地址'],
    ['@qq.com','cyj01','111111','code','user_email_error','请输入有效的电子邮件地址'],
    ['23@qq.com','cyj01','111111','code','user_email_error','请输入有效的电子邮件地址']

    )
    @ddt.unpack
    '''
    @ddt.data(*data)
    def test_register_case(self,data):
        #list赋值
        print(data)
        email,username,password,code,assertCode,assertText = data
        email_error = self.login.register_function(email,username,password,code,assertCode,assertText)
        print("----email_error---:",email_error)
        self.assertFalse(email_error)

if __name__ == "__main__":
    #unittest.main()
    file_path = os.path.join(os.getcwd()+"\\Report\\"+"first_Case1.html")
    f = open(file_path,'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="This is report01",description="this is our first test report",verbosity=2)
    runner.run(suite)    