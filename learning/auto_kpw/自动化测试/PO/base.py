from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 公共方法的封装
class base_Element:
    # 等待元素出现，并执行点击操作
    def common_click(self, by, el):
        element = WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located((by, el)))
        element.click()
        return element

    # 等待元素出现，并执行输入操作
    def common_send_keys(self, by, el, val):
        element = WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located((by, el)))
        element.send_keys(val)
        return element

    # 等待元素出现，并获取元素的文字
    def common_text(self, by, el):
        element = WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located((by, el)))
        return element.text
