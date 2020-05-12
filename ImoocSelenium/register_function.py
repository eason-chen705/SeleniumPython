#coding=utf-8
import sys
sys.path.append('D:/www/SeleniumPython')
from selenium import webdriver
import time
import random
from PIL import Image
from find_element import FindElement
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
from ShowapiRequest import ShowapiRequest


class RegisterFunction(object):
    def __init__(self,url,i):
        self.driver = self.get_driver(url,i)
    #get driver and open url
    def get_driver(self,url,i):
        if i == 0:
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()
        #else:
        #    driver = webdriver.Edge()

        driver.get(url)
        driver.maximize_window()
        time.sleep(3)
        return driver
    #input user info
    def send_user_info(self,key,data):
        self.get_user_element(key).send_keys(data)

    #locate user infor,get element
    def get_user_element(self,key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element
    
    #get a random number
    def get_range_user(self):
        user_info = ''.join(random.sample('1234567890abcdefghijklmnopqrstuvwxyz',8))
        return user_info

    #get Captcha picture
    def get_code_image(self,file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.get_user_element("code_image")
        #print(code_element.location) #{"x":123,"y":345}
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width']+left
        height = code_element.size['height']+top
        im = Image.open(file_name)
        #resize the screenshot
        img = im.crop((left,top,right,height)) 
        img.save(file_name)

    #Parsing Captcha picture via 3rd party API
    def code_online(self,file_name):
        self.get_code_image(file_name)
        r = ShowapiRequest("http://route.showapi.com/184-4","62626","d61950be50dc4dbd9969f741b8e730f5" )
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addFilePara("image", file_name) #文件上传时设置
        res = r.post()
        print(res.text)
        text = res.json()['showapi_res_body']['Result']
        return text

    def main(self):
        try:
            user_name_info = self.get_range_user()
            user_email = user_name_info+"@163.com"
            #file_name = "D:/www/SeleniumPython/Image/imooc.png"        
            #code_text = self.code_online(file_name)
            self.send_user_info('user_email',user_email)
            self.send_user_info('user_name',user_name_info)
            self.send_user_info('password',"111111")
            #self.send_user_info('code_text',code_text)
            self.send_user_info('code_text',"11111")
            self.get_user_element('register_button').click()
            code_error = self.get_user_element('code_text_error')
            if code_error == None:
                print("register succeeded")
            else:
                self.driver.save_screenshot("D:/www/SeleniumPython/Image/code_error.png")
            time.sleep(2)
            self.driver.close()
        except:
            self.driver.close()
            return("error")

if __name__ == "__main__":
    for i in range(2):
        register_function = RegisterFunction('http://www.5itest.cn/register',i)
        register_function.main()
