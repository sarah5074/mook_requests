import xlrd
'''filename = 'C:/Users/Administrator/PycharmProjects/imock_interface/data_config/operation_excel.xlsx'
#打开表格
data = xlrd.open_workbook(filename)
#获取第一张表
tables = data.sheets()[0]
#获取行数
rows = tables.nrows
#获取每一个格的信息
cell = tables.cell_value(1,2)
print(cell)'''

class OperaExcel():
    #类在实例化的时候，调用一个函数
    def __init__(self,filename=None,sheetid=None):
        if filename:#如果filename存在

            self.sheetid = sheetidl
            self.filename = filename  #定义全局变量，后面的可以直接用，不用传参
        else:
            self.filename = 'C:/Users/Administrator/PycharmProjects/imock_interface/data_config/operation_excel.xlsx'
            self.sheetid = 0
        self.data = self.get_data()


    def get_data(self):#拿到数据
        data = xlrd.open_workbook(self.filename)
        tables = data.sheets()[self.sheetid]
        return tables

    def get_lines(self):
        line = self.data.nrows()
        return line





if __name__== '__main__':
    filename = 'C:/Users/Administrator/PycharmProjects/imock_interface/data_config/1.xlsx'
    sheetid = 0
    opers = OperaExcel()
    print(opers.get_lines())
