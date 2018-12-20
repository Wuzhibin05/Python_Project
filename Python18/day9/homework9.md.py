#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Wuzhibin"
# Email: wuzhibin05@163.com
# Date: 2018/12/20

# 2，写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
l1 = [1,2,'alex',[1,2,3],'wuzb']
def search(l1):
    l2 = []
    for i in range(len(l1)):
        if i % 2 != 0:
            l2.append(l1[i])
    return l2
print(search(l1))


# 3，写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
l3 = 'sga142141'
def len_test(*args):
    if len(args)>5:
        return True
    else:
        return False
print(len_test(*l3))


# 4，写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
l4 = [1,2,'alex',[1,2,3],'wuzb']
def len1(*args):
    l5 = []
    if len(args) > 2:
        l5.append(args[0])
        l5.append(args[1])
        return l5
print(len1(*l4))
# 5，写函数，计算传入函数的字符串中,[数字]、[字母]、[空格] 以及 [其他]的个数，并返回结果。
s = " sfs1 42ssf  ss 我爱你"
def count(*args):
    total = []
    str_num = 0
    num = 0
    others = 0
    space = 0
    space = args.count(" ")
    for i in args:
        if i.isdigit():
            num +=1
        elif i.isalpha():
            str_num += 1
    others = len(args)- space - num - str_num
    total.append(str_num)
    total.append(num)
    total.append(space)
    total.append(others)
    return total
print(count(*s))

# 6，写函数，接收两个数字参数，返回比较大的那个数字。




