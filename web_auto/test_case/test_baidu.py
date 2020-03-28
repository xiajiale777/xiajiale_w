import unittest
from selenium import webdriver
from pages.pagesbaidu import Baidu
import time

class Baidu11(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.get("http://www.baidu.com")
        self.bd=Baidu(self.driver)

    """百度进行搜索"""
    def test_baidu_serch(self):
        self.bd.baidu_search("xiajiale")
        print(self.bd.titlecontains("百度"))
        self.assertTrue(self.bd.titlecontains("百度"),msg=["测试失败"])

    """百度设置保存"""
    def test_baidu_set(self):
        self.bd.baidu_set()
        a=self.bd.alertispresent()
        print(a)
        self.bd.alertevent()
        self.assertIsNotNone(a,msg=["测试失败"])

    def tearDown(self):
        self.driver.quit()

if __name__=="__main___":
    unittest.main()



