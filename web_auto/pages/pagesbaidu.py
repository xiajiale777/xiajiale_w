from common.base import Base
url=("http://www.baidu.com")
class Baidu(Base):
    """百度进行搜索"""

    loc_search=("id","kw")
    loc_submit=("id","su")

    """百度点击设置"""
    loc_set=("link text","设置")
    loc_searchset=("link text","搜索设置")
    loc_saveset=("link text","保存设置")


    def baidu_search(self,text):
        self.sendkeys(self.loc_search,text)
        self.click(self.loc_submit)


    def baidu_set(self):
        self.shubiaoyidong(self.loc_set)
        self.click(self.loc_searchset)
        self.click(self.loc_saveset)




if __name__=="__main__":
    from selenium import webdriver
    driver=webdriver.Firefox()
    driver.get(url)
    baidu=Baidu(driver)
    # baidu.baidu_search("自动化测试")
    baidu.baidu_search("xiajile")
    title=baidu.titlecontains("百度搜索")(driver)
    print(title)



