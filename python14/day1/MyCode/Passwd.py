#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Wuzhibin"
# Email: wuzhibin05@163.com
# Date: 2018/8/10

import getpass

_username = 'alex'
_password = '123'
username = input("username:")
# password = getpass.getpass("password:")
password = input("password:")


print(username,password)

if _username ==  username and _password == password:
    print("Welcome usr {name} login...".format(name=username))
else:
    print("Invalid username or password")
