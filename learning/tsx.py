# !/usr/local/bin/python
# coding=utf-8
monthMoney = int(input("请输入月收入："))
ds = 3500 #扣除标准
threeInsurancesUp = 7662#三险一金上线
yangLao=monthMoney*0.08
yiLiao=monthMoney*0.02
shiYe=monthMoney*0.005
homeMoney=monthMoney*0.12
threeInsurances=yangLao+yiLiao+shiYe+homeMoney
if threeInsurances>threeInsurancesUp:
    threeInsurances=threeInsurancesUp
#应纳税所得额
payable=monthMoney-threeInsurances-ds
single=0
if payable<1500:
    single=payable*0.03-0
elif payable>=1500 and payable<4500:
     single=payable*0.1-105
elif payable>=4500 and payable<9000:
     single=payable*0.2-555
elif payable>=9000 and payable<35000:
     single=payable*0.25-1005
elif payable>=35000 and payable<55000:
     single=payable*0.3-2002
elif payable>=55000 and payable<80000:
     single=payable*0.35-5505
elif payable>=80000:
     single=payable*0.45-13505
if single<0:
    single=0
print ("应纳个人所得税税额为%.2f" %single)