# import subprocess
# url = 'http://cmbchina.huacai.cn/test/test_cmbchina_member.jsp'
# cmd = ["C:\Program Files\Internet Explorer\iexplore.exe", url]
# cmd = ["C:\Program Files (x86)\Mozilla Firefox\firefox.exe", url]
# subprocess.Popen(cmd)


import webbrowser
import time
webbrowser.open_new_tab('http://cmbchina.huacai.cn/test/test_cmbchina_login.jsp?account=cmb%23m10620')
time.sleep(5)
webbrowser.open_new_tab('http://cmbchina.huacai.cn/test/test_cmbchina_refund.jsp')
time.sleep(5)
webbrowser.open_new_tab('http://cmbchina.huacai.cn/touch/index.do')
