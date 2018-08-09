#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Wuzhibin

import os
if os.path.exists('user.json'):  # 判断user.json是否存在，存在打印相关信息。
    print("The file is exist.")
else:
    print("Please check your file.")  # 不存在则退出程序。
    exit()

import json
file = 'user.json'
fp = open(file, 'r')
user_dict = json.load(fp)  # 打开将json中内容读取到字典user_dict中来，使用完毕关闭文件。
fp.close()

try_flag = 1

while try_flag:
    print("--------------------------------------------------")
    print("Welcome to login system ! ".center(50, "*"))
    print("--------------------------------------------------")
    username = input("please input  your name:")
    password = input("please input your password:")

    if username in user_dict:
        user_detail = user_dict[username]  # 如果字典里有该用户，则将该用户对应的value值给字典user_detail。

        if user_detail["locked"] == 3:  # 判断该用户的锁定标识是否为3,。如果为3，则认为该用户已锁定。
            print("The user is locked")
            try_flag = 0  # 将循环标识置为0，退出整个循环。

        elif user_detail["Password"] == password:  # 如果用户在此字典且用户密码正确，欢迎用户登录。
            print("--------------------------------------------------")
            print("Welcome to login in our system %s!".center(50,"*")%(username))
            print("--------------------------------------------------")
            user_detail["locked"] = 0  # 将该用户的locked标识置为0，用户下次的尝试次数还是3次。
            try_flag = 0   # 将循环标识置为0，退出整个循环。

        else:

            user_detail["locked"] += 1  # 如果用户输错一次密码，则将locked标识自增1，用户需要重新输入用户名密码。

            if user_detail["locked"] == 3:
                file = 'user.json'
                json.dump(user_dict, open('user.json', 'w'))
                fp.close()
                print("The user is locked,please ask administrator for help!")
                try_flag = 0
                '''
                如果用户输错三次密码(只要是在本次程序中输错三次密码。可以不是连续的三次，中途可以输入其他用户的密码)，将
                该用户的锁定标志locked改为3，并写入文件。下次用户登录则提示锁定。并将循环标识try_flag的标识改为0，从而
                退出整个循环。
                '''
            else:
                print("The password is mistake,please try again!")  # 锁定标识不等于3的时候提示用户再次输入。

    else:
        print("The user does not exist,please check your username!")
        '''
        用户不在用户字典中的时候提示用户检查自己的用户名
        '''

