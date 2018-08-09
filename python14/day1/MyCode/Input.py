#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Wuzhibin"
# Email: wuzhibin05@163.com
# Date: 2018/8/10

name = input("name:")
# 强制类型转换
age = int(input("age:"))
print(type(age))
job = input("job:")
salary = input("salary:")

# -------第一种格式化------------

# ------第二种格式化--------------
info = '''
-------- info of  %s  -----
Name:%s
Age:%d
Job:%s
Salary:%s
'''%(name,name,age,job,salary)
print(info)

# ------第三种格式化（官方推荐）--------------
info2 = '''
-------- info of {_name}  -----
Name:{_name}
Age:{_age}
Job:{_job}
Salary:{_salary}
'''.format(_name=name,
           _age=age,
           _job=job,
           _salary=salary)
print(info2)

# ------第三种格式化--------------
info3 = '''
-------- info of {0}  -----
Name: {0}
Age: {1}
Job: {2}
Salary:{3}
'''.format(name,
           age,
           job,
           salary)
print(info3)


