#操作excel
import xlrd
#文件地址直接选择绝对路径就好，copy path
#data = xlrd.open_workbook('C:/Users/Administrator/PycharmProjects/imock_interface/data_config/operation_excel.xlsx')
'''tables = data.sheets()[0]
print(tables.nrows)
print(tables.cell_value(1,3))  #x表示列，y表示行，索引从0开始'''
class OperateExcel():
    def __init__(self,filename=None,sheet_id=None):
        if filename:
            self.filename = filename
            self.sheet_id = sheet_id

        else:
            self.filename = 'C:/Users/Administrator/PycharmProjects/imock_interface/data_config/operation_excel.xlsx'
            self.sheet_id = 0
        self.data = self.get_data()
    #获取sheet的内容

    def get_data(self):
        data = xlrd.open_workbook(self.filename)
        tables = data.sheets()[self.sheet_id]
        return tables
    #获取单元格的行数
    def get_lines(self):
        tables = self.data
        return tables.nrows

    def get_cell_value(self,row,col):
        return self.data.cell_value(row,col)


if __name__ =='__main__':
    opers = OperateExcel()
    #filename = 'C:/Users/Administrator/PycharmProjects/imock_interface/data_config/operation_excel.xlsx'
    print(opers.get_data().nrows)
