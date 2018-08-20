#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Wuzhibin"
# Email: wuzhibin05@163.com
# Date: 2018/8/20

user_dict = {
             "alex":{"passwd": "1q2w3e","lockTimes":0},
             "wuzhibin":{"passwd": "1q2w3e","lockTimes":0},
             "zhangsan":{"passwd": "1q2w3e","lockTimes":0}
                                                        }

lock_time = 0

while True:
    user_name = input("Please input username:")
    if user_name in user_dict:
        if user_dict[user_name]["lockTimes"] <= 2:
            user_passwd = input("Please input your password:")

            if user_passwd == user_dict[user_name]["passwd"]:
                lock_time = 0
                user_dict[user_name]["lockTime"] = lock_time
                print("Welcome to login on our system!")
            else:
                lock_time += 1
                user_dict[user_name]["lockTime"] = lock_time
                print("Your password is not correct,please check!")
        else:
            exit("You account is locked,Bye bye!")
    else:
        print("Invalid username")
