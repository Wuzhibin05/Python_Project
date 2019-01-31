#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Bruce wu
# Date: 2019/1/31

# 1，使用循环打印以下效果:
# 1:
# *
# **
# ***
# ****
# *****
# 2:
# *****
# ****
# ***
# **
# *
# 3:
# *
# ***
# *****
# *******
# *********
for i in range(1,6):
    print(i*"*")

for i in range(5,0,-1):
    print(i*"*")

for i in range(1,10,2):
    print(i*"*")

# 2, 输入一个广告标语. 判断这个广告是否合法. 根据最新的广告法来判断. 广告法内容过多.
# 我们就判断是否包含'最', '第一', '稀缺', '国家级'等字样. 如果包含.提示：广告不合法. 例如,
#
# (1)老男孩python世界第一. 不合法
# (2)今年过年不收礼啊. 收礼只收脑白金. 合法
# li = ["最","第一","稀缺","国家级"]
# tag = 0
# msg = input("请输入广告语>>").strip()
# for i in li:
#     if i in msg:
#         tag = 1
#         break
# if tag ==1:
#     print("此广告不合法")
# else:
#     print("此广告合法")

# 3,敲七游戏. 从1开始数数. 遇到7或者7的倍数（不包含17,27,这种数）要在桌上敲一下. 编程来完成敲七.
#
# 给出一个任意的数字n. 从1开始数. 数到n结束. 把每个数字都放在列表中, 在数的过程中出现7或者7的倍数
# （不包含17,27,这种数）.则向列表中添加一个'咣'
# 例如, 输入10. # lst = [1, 2, 3, 4, 5, 6, '咣', 8, 9, 10]
# li1 = []
# list_len = input("请输入列表长度").strip()
#
# if list_len.isdigit():
#     list_len=int(list_len)
#     if list_len >0:
#         for i in range(1,list_len+1):
#             li1.append(i)
#         for index,value in enumerate(li1):
#             if value%7 == 0:
#                 li1[index]="咣"
# print(li1)

# ### 4，电影投票. 程序先给出一个目前正在上映的电影列表. 由用户给每一个电影投票. 最终，将该用户投票信息公布出来 。（此题明天可以继续做）
# **要求：**
# -     1，用户输入序号，进行投票。比如输入序号 1，给黄金兄弟投票1。
# -     2，每次投票成功，显示给哪部电影投票成功。
# -     3，退出投票程序后，要显示最终每个电影的投票数。
# ```python
# lst = ['黄金兄弟', '解救吾先生', '美国往事', '西西里的美丽传说'] 结果: {'黄金兄弟': 99, '解救吴先生': 80, '美国往事': 6, '西西里的美丽传说': 23}
# ```
lst = ['黄金兄弟', '解救吾先生', '美国往事', '西西里的美丽传说']
vote_dict ={}
for i in lst:
    vote_dict[i] = 0
while True:
    for index,value in enumerate(lst):
        print(index,value)
    choice_num = input("请输入你选择的编号>>").strip()
    if choice_num.isdigit():
        choice_num = int(choice_num)
        if choice_num in range(len(lst)):
            vote_dict[lst[choice_num]] += 1
        else:
            print("选择不在范围内，请重新输入！".center(80, "*"))
    elif choice_num.upper() == "Q":
        for key,value in vote_dict.items():
            print("%s的投票数是：%d"%(key,value))
        break

    else:
        print("输入的选项有误，请重新输入！".center(80,"*"))





