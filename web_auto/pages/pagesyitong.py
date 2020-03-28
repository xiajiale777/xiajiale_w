from common.base import Base
class Yitong(Base):
    url=("http://36.7.154.105:81/seeyon/main.do")
    loc_user=("id","login_username")
    loc_psw=("id","login_password")
    loc_submit=("id","login_button")
    loc_et=("id","error_text")
    loc_et=("id","error_text")
    loc_language=("id","login_locale_dropdown_text")
    loc_framelanguage=("xpath","[@id=login_locale_dropdown_title]/iframe")
    loc_languageenglish=("xpath","[@id=login_locale_dropdown_title]/iframe/a[2]")




    def inputuser(self,text):
        self.sendkeys(self.loc_user,text)

    def inputpsw(self,text):
        self.sendkeys(self.loc_psw,text)

    def submit(self):
        self.click(self.loc_submit)

    def selectlanguage(self):
        self.click(self.loc_language)

    def pa(self):
        self.isElementpresent(self.loc_et)

    def ylanguageswitchtoframe(self):
        self.click(self.loc_language)
        self.switchtoframe(self.loc_framelanguage)
        # self.click(self.loc_languageenglish)



if __name__=="__main__":

    from  selenium import webdriver
    driver=webdriver.Firefox()
    url=("http://36.7.154.105:81/seeyon/main.do")
    driver.get(url)
    yt=Yitong(driver)
    yt.ylanguageswitchtoframe()
    # yt.inputuser(+"117895")
    # yt.inputpsw("xjl1314521")
    # yt.submit()
    # a=yt.pa()
    # print(a)



