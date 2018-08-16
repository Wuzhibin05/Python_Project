#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Wuzhibin"
# Email: wuzhibin05@163.com
# Date: 2018/8/16
product_list = [("Iphone8",5800),
                ("Thinkpad480",6000),
                ("Bike",1600),
                ("mate20",5000),
                ("Python基础",80)]
for item in product_list:

    print(product_list.index(item),item)