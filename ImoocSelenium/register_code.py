#coding=utf-8
from selenium import webdriver
import time
import random
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
from Util.ShowapiRequest import ShowapiRequest

driver = webdriver.Chrome()

#browser iniliaze
def driver_init():
    driver.get("http://www.5itest.cn/register")
    driver.maximize_window()
    time.sleep(3)

#get element information
def get_element(id):
    element = driver.find_element_by_id(id)
    return element
#get a random number
def get_range_user():
    user_info = ''.join(random.sample('1234567890abcdefghijklmnopqrstuvwxyz',8))
    return user_info

#get Captcha picture
def get_code_image(file_name):
    driver.save_screenshot(file_name)
    code_element = driver.find_element_by_id("getcode_num")
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
def code_online(file_name):
    r = ShowapiRequest("http://route.showapi.com/184-4","62626","d61950be50dc4dbd9969f741b8e730f5" )
    r.addBodyPara("typeId", "35")
    r.addBodyPara("convert_to_jpg", "0")
    r.addFilePara("image", file_name) #文件上传时设置
    res = r.post()
    print(res.text)
    text = res.json()['showapi_res_body']['Result']
    return text

#main script
def run_main():
    user_name_info = get_range_user()
    user_email = user_name_info+"@163.com"
    file_name = "D:/www/SeleniumPython/Image/imooc.png"
    driver_init()
    get_element("register_email").send_keys(user_email)
    get_element("register_nickname").send_keys(user_name_info)
    get_element("register_password").send_keys("111111")
    get_code_image(file_name)
    text = code_online(file_name)
    get_element("captcha_code").send_keys(text)
    get_element("register-btn").click()
    time.sleep(2)
    driver.close()

run_main()
