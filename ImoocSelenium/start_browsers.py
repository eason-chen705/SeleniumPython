#coding=utf-8
from selenium import webdriver
import time
import random
from PIL import Image
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

'''
for i in range(5):
    user_email = ''.join(random.sample('1234567890abcdefghijklmnopqrstuvwxyz',8))+"@163.com"
    print(user_email)

'''
driver = webdriver.Chrome()
#driver = webdriver.Firefox()
driver.get("http://www.5itest.cn/register")
driver.maximize_window()
time.sleep(3)
print(EC.title_contains("注册"))
email_element = driver.find_element_by_id("register_email")
driver.save_screenshot("D:/www/SeleniumPython/ImoocSelenium/imooc.png")
code_element = driver.find_element_by_id("getcode_num")
print(code_element.location) #{"x":123,"y":345}
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width']+left
height = code_element.size['height']+top
im = Image.open("D:/www/SeleniumPython/ImoocSelenium/imooc.png")
#resize the screenshot
img = im.crop((left,top,right,height)) 
img.save("D:/www/SeleniumPython/ImoocSelenium/imooc1.png")
driver.close()

'''
#verify if the element is found
#element = driver.find_elements_by_class_name("controls")
locator = (By.CLASS_NAME,"controls")
WebDriverWait(driver,1).until(EC.visibility_of_element_located(locator))

print(email_element.get_attribute("placeholder"))
email_element.send_keys("cyj@163.com")
print(email_element.get_attribute("value"))
driver.close()

driver.find_element_by_id("register_email").send_keys("himo2020@163.com")
user_name_element_node = driver.find_elements_by_class_name("controls")[1]
user_element = user_name_element_node.find_element_by_class_name("form-control")
user_element.send_keys("himo2020")
driver.find_element_by_name("password").send_keys("222222")
driver.find_element_by_xpath("//*[@id='captcha_code']").send_keys("111111")
'''