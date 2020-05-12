#coding=utf-8
import logging
import os
import datetime
class Userlog(object):
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        #创建流对象，控制台输出日志
        #consle = logging.StreamHandler()
        #logger.addHandler(consle)
        #logger.debug("info")
        #file name
        base_dir = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(base_dir,"logs")
        log_file = datetime.datetime.now().strftime("%Y-%m-%d")+".log"
        log_name = log_dir+"/"+log_file
        #print(log_name)
        #文件输出日志
        self.file_handle = logging.FileHandler(log_name,'a',encoding='utf-8')
        #only log info of logging
        self.file_handle.setLevel(logging.INFO)
        #set file format
        formatter = logging.Formatter('%(asctime)s %(filename)s---> %(funcName)s %(lineno)d %(levelname)s --->%(message)s')
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)
        #logger.debug("test12344")

    def get_log(self):
        return self.logger

    def close_handle(self):
        #关闭流对象和logger
        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()

if __name__ == "__main__":
    user = Userlog()
    log = user.get_log()
    log.debug('test')
    user.close_handle()