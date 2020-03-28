from selenium import webdriver
import unittest
from pages.pagesyitong import Yitong

class Yitong1(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Firefox()
        self.yt=Yitong(self.driver)
        self.driver.get(self.yt.url)
        print("---------------开始测试-----------------")

    """正确账号，正确秘密"""
    def test_01(self):
        self.yt.inputuser("117895")
        self.yt.inputpsw("xjl1314520")
        self.yt.submit()
        r=self.yt.isElementpresent(self.yt.loc_et)
        print(r)
        self.assertFalse(r,msg=["测试失败"])

    """正确的账号，空的秘密"""
    def test_02(self):
        self.yt.inputuser("117895")
        self.yt.inputpsw("")
        self.yt.submit()
        r=self.yt.isElementpresent(self.yt.loc_et)
        print(r)
        self.assertTrue(r,msg=["测试失败"])
    #
    """空的账号，正确的秘密"""
    def test_03(self):
        self.yt.inputuser("")
        self.yt.inputpsw("xjl1314520")
        self.yt.submit()
        r=self.yt.isElementpresent(self.yt.loc_et)
        print(r)
        self.assertTrue(r,msg=["测试失败"])

    # def test_04(self):
    #     self.yt.selectlanguage()


    def tearDown(self):
        self.driver.quit()
        print("------------测试结束--------------")







if __name__=="__main__":
    unittest.main()
