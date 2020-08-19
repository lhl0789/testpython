# 导包
# from common import HTMLTestRunnerNew
# import unittest
# import time
# # 设置一个容器
# testsuite = unittest.TestSuite()
#
# # 发现用例
# suite = unittest.defaultTestLoader.discover('./test_cases')
# testsuite.addTests(suite)
# # 用load取用例
# load=unittest.defaultTestLoader
# testcases = load.discover('test_cases',pattern='test*.py',top_level_dir=None)
# # 把用例放在容器中
# #suite.addTests(testcases)
# currenttime = time.strftime("%Y-%m-%d %H-%M-%S")
# filename = r'report/reporter'+currenttime+'.html'
# with open(filename,'wb+') as fp:
#     HTMLTestRunnerNew.HTMLTestRunner(stream=fp,title='学生管理系统接口测试报告',description='balalala,',tester='xml').run(testsuite)




import unittest
from common import HTMLTestRunnerNew
import time

testsuite = unittest.TestSuite()
suite = unittest.defaultTestLoader.discover('./test_cases')
testsuite.addTests(suite)
currenttime = time.strftime('%Y-%m-%d-%H-%M-%S')
filename = r'report/reporter'+currenttime+'.html'
with open(filename, 'wb+') as f:
    HTMLTestRunnerNew.HTMLTestRunner(stream=f,
                                     title='学生管理系统',
                                     description='balala',
                                     tester='xml').run(testsuite)







