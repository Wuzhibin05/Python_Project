#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Wuzhibin"
# Email: wuzhibin05@163.com
# Date: 2018/8/13

# import passwd_demo

import os
# # # 执行系统命令，不保存结果
# # cmd_res = os.system("dir")
# # print("--",cmd_res)
# #
# # # 执行系统命令，保存结果
# # cmd_res = os.popen("dir").read()
# # print(cmd_res)
# #
# # # 创建目录
# # os.mkdir("new_dir")

# 字符串和byte互相转换
msg = "我爱你"
print(msg.encode("utf-8"))
print(msg.encode("utf-8").decode("utf-8"))