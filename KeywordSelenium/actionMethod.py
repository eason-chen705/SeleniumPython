#coding=utf-8
from selenium import webdriver
from Base.find_element import FindElement
import time

class ActionMethod:
    def __init__(self):
        pass
    #open browser
    def open_browser(self,browser):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Edge()
    
    #input URL
    def get_url(self,url):
        self.driver.get(url)
    #locate element
    def get_element(self,key):
        find_element = FindElement(self.driver)
        element = find_element.get_element(key)
        return element
    #input data
    def element_send_keys(self,value,key):
        element = self.get_element(key)
        element.send_keys(value)
    #click element
    def click_element(self,key):
        self.get_element(key).click()
    #wait
    def sleep_time(self):
        time.sleep(3)
    #close browser
    def close_browser(self):
        self.driver.close()
    #get title
    def get_title(self):
        return self.driver.title

