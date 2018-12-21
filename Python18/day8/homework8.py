#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Bruce wu
# Date: 2018/12/20

# 题目1

## a
# f = open('./a1.txt',mode = 'r',encoding='utf-8')
# for line in f:
#     print(line)
# f.close()

## b

f = open('./a1.txt',mode = 'a',encoding='utf-8')
f.write("信不信由你，反正我信了。")
f.close()