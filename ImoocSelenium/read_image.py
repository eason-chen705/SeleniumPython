#coding=utf-8
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
from PIL import Image
from ShowapiRequest import ShowapiRequest
'''
image = Image.open("D:/www/SeleniumPython/ImoocSelenium/imooc1.png")
text = pytesseract.image_to_string(image)
print(text)
'''

r = ShowapiRequest("http://route.showapi.com/184-4","62626","d61950be50dc4dbd9969f741b8e730f5" )
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addFilePara("image", r"D:/www/ImoocSelenium/imooc1.png") #文件上传时设置
res = r.post()
text = res.json()['showapi_res_body']['Result']
print(text) # 返回信息
