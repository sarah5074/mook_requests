import unittest
from base.demo import RunMain
from base.mock_demo import *
#创建一个类继承unittest
class TestMethod(unittest.TestCase):

    def setUp(self):#，每个case执行之前都要执行setup
        self.run = RunMain()
        #self.user_id = self.test_001()

    def test_001(self):
        url = 'http://127.0.0.1:8000/login/'
        data = {'username':'sarah',
        'password':'fdfd'}

        #res = self.run.run_main(url,"POST",data)
        #print(res)
        res = mock_test(self.run.run_main,data,'POST',url,data)

        #self.assertEqual(res['user'],'sarah')
        #globals()['userid'] = 10034   #定义全局变量
        #return self.user_id
        print(res)

    @unittest.skip('test_002')    #跳过test_002的方法
    def test_002(self):
        url = 'http://127.0.0.1:8000/login/'
        data = {'username':'sarah',
        'password':'fssgsgsgsg'}
        res = self.run.run_main(url,"POST",data)
        print(res)
        print(userid)

    def tearDown(self):
        pass

if __name__ =='__main__':
    suite = unittest.TestSuite()#创建测试集
    suite.addTest(TestMethod('test_001'))
    unittest.run(suite)