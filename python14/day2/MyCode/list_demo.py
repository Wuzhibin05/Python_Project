#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Wuzhibin"
# Email: wuzhibin05@163.com
# Date: 2018/8/14


# names = "ZhangYang Guyun Xiangpeng Xuliangchen"


# names = ["ZhangYang","ZhangYang",["Guyun","Xiangpeng"],"Xuliangchen"]

# # 增加值。
# names.append("Alex")
#
# # 插入值到指定位置
# names.insert(1,"Chenzhonghua")
#
# # 修改
# names[2] = "Xiedi"
# # 删除
# names.remove("Chenzhonghua")
# del names[0]
# del names
# names.pop()

# 取值，用位置取值
# print(names[0],names[2])
#
# # 切片取值
# print(names[1:3])
# print(names[-1])
# print(names[-3:-1])
# print(names[-3:])
#
# print(names)
# # 查询索引
# print(names.index("ZhangYang"))
# print(names[names.index("ZhangYang")])
# # 计数
# print(names.count("ZhangYang"))
# # 清空
# names.clear()
# 反转
# names.reverse()
# # 排序，按照ASCII排序
# names.sort()
# names2 = ["a","b","c"]
# # 扩展列表
# names.extend(names2)
# print(names,names2)
import copy

names = ["ZhangYang","ZhangYang",["Guyun","Xiangpeng"],"Xuliangchen"]
# names2 = names.copy()
names2 = copy.deepcopy(names)
names[2] = "小十"
names[0] = "Alex"
names[2][0] ="ALEXANDER"
print(names)
print(names2)

# 字符串和数字赋值
a = 1
b = a
a = 2
b = 1
print(a,b)

# 步长
print(names[::2])
print(names[0:-1:2])