#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Wu zhi bin"
# Email: wuzhibin05@163.com
# Date: 2018/8/15


'''
# 程序：购物车程序
# 需求:
#  启动程序后，让用户输入工资，然后打印商品列表
#  允许用户根据商品编号购买商品
#  用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
#  可随时退出，退出时，打印已购买商品和余额
'''

product_list = [("Iphone8", 5800),
                ("Think110", 6000),
                ("Bike", 1600),
                ("mate20", 5000),
                ("Python基础", 80),
                ("pen", 10)]

shopping_car = []
salary = input("Please input your salary:")
if salary.isdigit():
    salary = int(salary)
    while True:
        for index, item in enumerate(product_list):
            print(index, item)
        # for item in product_list:
        #     print(product_list.index(item), item)
        user_choice = input("Please input you choice:")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if (user_choice >= 0) and (user_choice <= len(product_list)):
                if salary >= product_list[user_choice][1]:
                    shopping_car.append(product_list[user_choice])
                    salary -= product_list[user_choice][1]
                    print("Trade successfully")
                else:
                    print("you can't afford it!")
            else:
                print("You choice is not exist,please try again!")
        elif user_choice == "b":
            for item in shopping_car:
                print(item)
            exit("your balance is %s!" % salary)
        else:
            print("Invalid input, please try again!")
else:
    print("Invalid input bye bye!")

