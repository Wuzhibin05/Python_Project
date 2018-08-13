#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Wuzhibin"
# Email: wuzhibin05@163.com
# Date: 2018/8/10

age_of_oldboy = 56
count = 0
while count < 3:
    guess_age = int(input("guess age:"))
    if guess_age == age_of_oldboy:
        print("yes, you got it !")
        break
    elif guess_age > age_of_oldboy:
        print("Think smaller!")
    else:
        print("Think bigger!")
    count += 1
else:
   print("You have tried too manay times!")


