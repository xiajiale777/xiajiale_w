from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


"""Example:
            from selenium.webdriver.support.ui import WebDriverWait \n
            element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("someId")) \n
            is_disappeared = WebDriverWait(driver, 30, 1, (ElementNotVisibleException)).\ \n
                        until_not(lambda x: x.find_element_by_id("someId").is_displayed())"""
class Base():
    def __init__(self,driver):
        self.driver=driver
        self.t=0.5
        self.timeout=10
    def findelement(self,locator):
        ele=WebDriverWait(self.driver,self.t).until(lambda x:x.find_element(*locator))
        return ele

    def sendkeys(self,locator,text):
        ele=self.findelement(locator)
        ele.send_keys(text)

    def click(self,locator):
        ele=self.findelement(locator)
        ele.click()

    """鼠标移动事件"""
    def shubiaoyidong(self,locator):
        mouse=self.findelement(locator)
        ele=ActionChains(self.driver).move_to_element(mouse).perform()
        return ele

    """弹框事件"""
    def alertevent(self):
        a=self.driver.switch_to.alert
        a.accept()
    """切换ifame"""
    def switchtoframe(self,locator):
        element=self.findelement(locator)
        self.driver.switch_to.frame(element)
    """回到主界面"""
    def defaultcontent(self):
        self.driver.switch_to.default_content()

     # def selectevent(self,locator):
     #    el=self.findelement(locator)
     #    select(el).




    """判断title是否相等"""
    def titleis(self,text):
        a=EC.title_is(text)(self.driver)
        return a






    """判断title包含"""
    def titlecontains(self,text):
        a=EC.title_contains(text)(self.driver)
        return a

    def alertispresent(self):
        a=EC.alert_is_present()(self.driver)
        return a.text

    def isElementpresent(self,locator):
        """用来判断元素标签是否存在"""
        try:
            self.findelement(locator)
            return True
        except:
            return False





if __name__=="__main__":
    loc_user=("id","login_username")
    loc_psw=("id","login_password")
    loc_submit=("id","login_button")
    loc_errortext=("id","error_text")


    from selenium import webdriver
    driver=webdriver.Firefox()
    driver.get("http://36.7.154.105:81/seeyon/main.do")
    baidu=Base(driver)
    baidu.sendkeys(loc_user,"117895")
    baidu.sendkeys(loc_psw,"xjl1314521")
    baidu.click(loc_submit)
    a=baidu.isElementpresent(loc_errortext)
    print(a)
    # loc3=("link text","设置")
    # loc4=("link text","搜索设置")
    # loc5=("link text","保存设置")
    # loc1=("id","kw")
    # loc2=("id","su")
    # # baidu.findelement(loc1).send_keys("sss")
    # # baidu.findelement(loc2).click()
    # baidu.sendkeys(loc1,"sss")
    # baidu.click(loc2)
    # driver.find_element_by_link_text()
    # mouse=driver.find_element_by_link_text("设置")
    # ActionChains(driver).move_to_element(mouse).perform()
    # baidu.shubiaoyidong(loc3)
    # baidu.click(loc4)
    # baidu.click(loc5)
    # b=baidu.alertispresent()
    # print(b)
    # baidu.alertevent()
    # a=baidu.titleis("百度一下，你就知道")
    # print(a)



