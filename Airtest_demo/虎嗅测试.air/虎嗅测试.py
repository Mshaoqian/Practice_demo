# -*- encoding=utf8 -*-
__author__ = "和铭谦"

from airtest.core.api import *
import time



from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)
# snapshot(filename="1.jpg")
# swipe((517,1716),(517,193),duration=2)
# print(type(snapshot(filename="2.jpg" ,msg="请填写测试点.")))

# 在页面也截图的方法
# sign = 0
# while 1:
#     sign = sign+1
#     snapshot(filename="{}.jpg".format(sign)) 
#     swipe((517,1716),(517,193),duration=2)
#     if poco(name="内容棒棒哒，邀请好友免费读").exists():
#         break
# poco(name="com.huxiu:id/footer_back").click()

# 进页面的方法
one_height = 336# 适应更改
sum_height = 0
cl_height=0
flag = 0
cl_width=541
sign = 0
while True:
    cl_height = cl_height+one_height
    if cl_height>=2000:
        cl_height=336
        swipe((517,1716),(517,0),duration=2)
        if poco(text="没有更多内容了").exists():
            flag = flag+1
        sleep(5)
    if flag == 2:
        break
    touch((cl_width,cl_height))
    sleep(3)
    while 1:
        sign = sign +1 
        sleep(1)
        snapshot(filename="{}.jpg".format(sign)) 
        swipe((517,1716),(517,40),duration=2)
        if poco(name="内容棒棒哒，邀请好友免费读").exists() or poco(name="别打CALL，打钱") or poco(name="支持一下").exists() or poco(text="读过本文，TA们还读了").exists():
            sign = sign +1 
            snapshot(filename="{}.jpg".format(sign))
            break
    sleep(1)
    poco(name="com.huxiu:id/footer_back").click()
     
    
