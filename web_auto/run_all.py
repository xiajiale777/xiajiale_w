import unittest
from common import HTMLTestRunner_cn
#用例路径
casepath=("E:\\web_auto\\test_case")
rule=("test*.py")
discover=unittest.defaultTestLoader.discover(start_dir=casepath,pattern=rule)
reportpath=("E:\\web_auto\\report\\"+"report.html")
fp=open(reportpath,"wb")
runner=HTMLTestRunner_cn.HTMLTestRunner(stream=fp,title="超级完美无敌美丽的测试报告",description="主要是用来测"
                                                                               "试百度搜索和上海屹通的登录界面")
runner.run(discover)

if __name__=="__main__":
    unittest.main()

