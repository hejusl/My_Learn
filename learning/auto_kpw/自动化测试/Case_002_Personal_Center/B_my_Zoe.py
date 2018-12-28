from selenium.webdriver.common.by import By
from 自动化测试.common import *


# 已登录状态进入首页,点击【个人中心】按钮,进入“个人中心”页面
def personal_Center_01(self):
    common_click(self, By.ID, 'com.kpwlottery.app:id/title_left')

# 返回---com.kpwlottery.app:id/iv_back
# 个人信息图标---com.kpwlottery.app:id/iv_info
# 设置---com.kpwlottery.app:id/iv_setting
# 用户名---com.kpwlottery.app:id/tv_name
# 头像---com.kpwlottery.app:id/iv_icon
# 余额---
# 余额￥---com.kpwlottery.app:id/tv_balance
# 彩金---
# 彩金￥---com.kpwlottery.app:id/tv_k_beans
# 充值---com.kpwlottery.app:id/tv_topup
# 提现---com.kpwlottery.app:id/tv_withdraw
# 资金流水---com.kpwlottery.app:id/tv_capital
# 转账---com.kpwlottery.app:id/tv_transfer
# 彩票记录---com.kpwlottery.app:id/tv_lottery_record
# 游戏记录---com.kpwlottery.app:id/tv_game_record
# FAQ---com.kpwlottery.app:id/tv_faq
# 分享---com.kpwlottery.app:id/tv_share
# 扫我---com.kpwlottery.app:id/tv_scan_me

