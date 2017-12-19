import unittest
from base.demo import RunMain
#创建一个类继承unittest
class TestMethod(unittest.TestCase):

    def setUp(self):
        self.run = RunMain()

    def test_001(self):
        url = 'http://127.0.0.1:8000/login/'
        data = {'username':'sarah',
        'password':'fdfd'}
        #res = self.run.run_main(url,"POST",data)
        #print(res)
        res = self.run.run_main(url,"POST",data)
        self.assertEqual(res['user'],'sarah')
        #print(res)

    def test_002(self):
        url = 'http://127.0.0.1:8000/login/'
        data = {'username':'sarah',
        'password':'fssgsgsgsg'}
        res = self.run.run_main(url,"POST",data)
        print(res)

    def tearDown(self):
        pass

if __name__ =='__main__':
    unittest.main()