# 执行测试套件
import unittest
from learning.auto_kpw.自动化测试.KPW_case_login import DemoTest

if __name__ == '__main__':
    suite = unittest.TestSuite()

    tests = [DemoTest('test_case_login')]
    # 使用TestSuite的addTest()方法,直接传入TestCase列表
    suite.addTests(tests)

    with open('/Users/henry/02_Study/01_Python/learning/auto_kpw/自动化测试/UnittestTextReport.txt', 'a') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)