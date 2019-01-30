#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Bruce wu
# Date: 2019/1/30

### 1，写代码，有如下列表，按照要求实现每一个功能

# ```python
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# ```
# - 1)计算列表的长度并输出
# - 2)列表中追加元素"seven",并输出添加后的列表
# - 3)请在列表的第1个位置插入元素"Tony",并输出添加后的列表
# - 4)请修改列表第2个位置的元素为"Kelly",并输出修改后的列表
# - 5)请将列表l2=[1,"a",3,4,"heart"]的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
# - 6)请将字符串s = "qwert"的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
# - 7)请删除列表中的元素"eric",并输出添加后的列表
# - 8)请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表
# - 9)请删除列表中的第2至4个元素，并输出删除元素后的列表
# - 10)请将列表所有得元素反转，并输出反转后的列表
# - 11)请计算出"alex"元素在列表li中出现的次数，并输出该次数。
li = ["alex", "WuSir", "ritian", "barry", "wenzhou","eric"]
l2=[1,"a",3,4,"heart"]
s = "qwert"
print(len(li))
li.append("seven")
li.insert(1,"Tony")
li[2]="Kelly"
li.extend(l2)
li.extend(s)
li.remove("eric")
li.pop(1)
li.pop(2)
del li[1:4]
print(li)
print(li.reverse())
print(li)
print(li.count("alex"))



### 2，写代码，有如下列表，利用切片实现每一个功能

# ```python
# li = [1, 3, 2, "a", 4, "b", 5,"c"]
# ```
# - 1)通过对li列表的切片形成新的列表l1,l1 = [1,3,2]
# - 2)通过对li列表的切片形成新的列表l2,l2 = ["a",4,"b"]
# - 3)通过对li列表的切片形成新的列表l3,l3 = ["1,2,4,5]
# - 4)通过对li列表的切片形成新的列表l4,l4 = [3,"a","b"]
# - 5)通过对li列表的切片形成新的列表l5,l5 = ["c"]
# - 6)通过对li列表的切片形成新的列表l6,l6 = ["b","a",3]
li2 = [1, 3, 2, "a", 4, "b", 5,"c"]
print(li2[:3])
print(li2[3:6])
print(li2[::2])
print(li2[1:-2:2])
print(li2[-1:])
print(li2[-3::-2])

### 3,写代码，有如下列表，按照要求实现每一个功能。

# - lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# - 1)将列表lis中的"tt"变成大写（用两种方式）。
# - 2)将列表中的数字3变成字符串"100"（用两种方式）。
# - 3)将列表中的字符串"1"变成数字101（用两种方式）。
lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
lis[3][2][1][0]="TT"
lis[3][2][1][1]="100"
lis[3][2][1][2]="101"
print(lis)


### 4,请用代码实现：
#
# ```python
# li = ["alex", "eric", "rain"]
# ```
# 利用下划线将列表的每一个元素拼接成字符串"alex_eric_rain"
l3 = ["alex", "eric", "rain"]
s="_".join(l3)
print(s)

### 5，利用for循环和range打印出下面列表的索引。

# ```python
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# ```
li3 = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
for index,i in enumerate(li3):
    print(index,i)

### 6，利用for循环和range找出100以内所有的偶数并将这些偶数插入到一个新列表中。
li4 =[]
for i in range(101):
    if i%2 == 0:
        li4.append(i)
print(li4)

### 8，利用for循环和range从100~1，倒序打印。

for i in range(100,0,-1):
    print(i)

### 9，利用for循环和range从100~10，倒序将所有的偶数添加到一个新列表中，然后对列表的元素进行筛选，将能被4整除的数留下来。