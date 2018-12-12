#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Wu zhi bin"
# Email: wuzhibin05@163.com
# Date: 2018/11/11

# 实现a的中元素全部加1.
a = [1,3,4,6,7,7,8,9,11]
for index,i in enumerate(a):
    a[index] +=1
    print(a[index], index, i)
print(a)


# 使用lambda表达式实现列表b中元素加1.
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = map(lambda x: x + 1, b)
print(b)
for i in b: print(i)
