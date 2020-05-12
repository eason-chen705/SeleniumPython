#coding=utf-8
import sys
sys.path.append('D:\\www\\SeleniumPython')
from Util.excel_util import ExcelUtil
from KeywordSelenium.actionMethod import ActionMethod

class KeywordCase:
    def run_main(self):
        self.action_method = ActionMethod()
        handle_excel = ExcelUtil('D:\\www\\SeleniumPython\\Config\\keyword.xls')
        case_lines = handle_excel.get_lines()
        if case_lines:
            for i in range(1,case_lines):
                is_run = handle_excel.get_col_value(i,3)
                #print(is_run)
                if is_run == 'yes':
                    method = handle_excel.get_col_value(i,4)
                    send_value = handle_excel.get_col_value(i,5)
                    handle_value = handle_excel.get_col_value(i,6)
                    expect_result_method = handle_excel.get_col_value(i,7)
                    expect_result = handle_excel.get_col_value(i,8)
                    #print(expect_result_method,expect_result)
                    self.run_method(method,send_value,handle_value)
                    if expect_result !='':
                        expect_value = self.get_expect_result_value(expect_result)
                        if expect_value[0] == 'text':
                            result = self.run_method(expect_result_method)
                            print(result)
                            if expect_value[1] in result:
                                handle_excel.write_value(i,'pass')
                            else:
                                handle_excel.write_value(i,'fail')
                        elif expect_value[0] == 'element':
                            print(expect_result_method,expect_value[1])
                            result = self.run_method(expect_result_method,expect_value[1])
                            print(result)
                            if result:
                                handle_excel.write_value(i,'pass')
                            else:
                                handle_excel.write_value(i,'fail')
                        else:
                            print("no else")
                    else:
                        print("expected result is blank")

    #get the value of expect_result
    def get_expect_result_value(self,data):
        return data.split('=')



    def run_method(self,method,send_value='',handle_value=''):
        #get the value of col "ExecuteMethod" from excel file, and find the related function from Class "action_method"
        method_value = getattr(self.action_method,method)
        if send_value == "" and handle_value != "":
            result = method_value(handle_value)
        elif send_value == "" and handle_value == "":
            result = method_value()
        elif send_value != "" and handle_value == "":
            result = method_value(send_value)
        else:
            result = method_value(send_value,handle_value)
        return result

if __name__ == "__main__":
    test = KeywordCase()
    test.run_main()
