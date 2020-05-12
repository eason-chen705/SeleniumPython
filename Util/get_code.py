#coding=utf-8
from PIL import Image
from Util.ShowapiRequest import ShowapiRequest
import time

class GetCode:    
    def __init__(self,driver):
        self.driver = driver
    #get Captcha picture
    def get_code_image(self,file_name):
        self.file_name = "D:\\www\\SeleniumPython\\Report\\code.png"
        self.driver.save_screenshot(file_name)
        code_element = self.driver.find_element_by_id("getcode_num")
        #print(code_element.location) #{"x":123,"y":345}
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width']+left
        height = code_element.size['height']+top
        im = Image.open(file_name)
        #resize the screenshot
        img = im.crop((left,top,right,height)) 
        img.save(file_name)
        time.sleep(2)

    #Parsing Captcha picture via 3rd party API
    def code_online(self,file_name):
        self.get_code_image(file_name)
        '''
        r = ShowapiRequest("http://route.showapi.com/184-4","62626","d61950be50dc4dbd9969f741b8e730f5" )
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addFilePara("image", file_name) #文件上传时设置
        res = r.post()
        #print(res.text)
        text = res.json()['showapi_res_body']['Result']
        time.sleep(2)
        '''
        text = "code"
        return text