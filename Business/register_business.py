#coding=utf-8
from Handle.register_handle import RegisterHandle
class RegisterBusiness:
    def __init__(self,driver):
        self.register_h = RegisterHandle(driver)
    #business业务层，执行操作,把handle层组装起来

    def user_base(self,email,name,password,file_name):
        self.register_h.send_user_email(email) 
        self.register_h.send_user_name(name)
        self.register_h.send_user_password(password)
        self.register_h.send_user_code(file_name)
        self.register_h.click_register_button()

    def register_success(self):
        if self.register_h.get_register_text() == None:
            return True
        else:
            return False

    def login_email_error(self,email,name,password,code):
        self.user_base(email,name,password,code)
        if self.register_h.get_user_text('email_error',"请输入有效的电子邮件地址") == None:
            print("---email verify failed!")
            return True
        else:
            return False

    def register_function(self,email,username,password,code,assertCode,assertText):
        file_name = "D:\\www\\SeleniumPython\\Report\\code.png"
        self.user_base(email,username,password,file_name)
        if self.register_h.get_user_text(assertCode,assertText) == None:
            print("---email verify failed!")
            return True
        else:
            return False        


    def login_name_error(self,email,name,password,code):
        self.user_base(email,name,password,code)
        if self.register_h.get_user_text('user_name_error',"字符长度必须大于等于4，一个中文字算2个字符") == None:
            print("---username verify failed!")
            return True
        else:
            return False

    def login_password_error(self,email,name,password,code):
        self.user_base(email,name,password,code)
        if self.register_h.get_user_text('password_error',"最少需要输入 5 个字符") == None:
            print("---password verify failed!")
            return True
        else:
            return False
    def login_code_error(self,email,name,password,code):
        self.user_base(email,name,password,code)
        if self.register_h.get_user_text('code_text_error',"验证码错误") == None:
            print("---code verify failed!")
            return True
        else:
            return False
