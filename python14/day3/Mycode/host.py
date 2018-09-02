#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Wuzhibin"
# Email: wuzhibin05@163.com
# Date: 2018/8/26

# 数据库中原有
old_dict = {
    "#1": {'hostname': 'c1', 'cpu_count': 2, 'mem_capicity': 80},
    "#2": {'hostname': 'c1', 'cpu_count': 2, 'mem_capicity': 80},
    "#3": {'hostname': 'c1', 'cpu_count': 2, 'mem_capicity': 80}
}

# cmdb 新汇报的数据
new_dict = {
    "#1": {'hostname': 'c1', 'cpu_count': 2, 'mem_capicity': 800},
    "#3": {'hostname': 'c1', 'cpu_count': 2, 'mem_capicity': 80},
    "#4": {'hostname': 'c2', 'cpu_count': 2, 'mem_capicity': 80}
}

# 1，需要删除主机：？
# 2，需要新建主机：？
# 3，需要更新主机：？ 注意：无需考虑内部元素是否改变，只要原来存在，新汇报也存在，就是需要更新
old_set = set(old_dict.keys())
update_list = list(old_set.intersection(new_dict.keys()))

new_list = []
del_list = []

for i in new_dict.keys():
    if i not in update_list:
        new_list.append(i)

for i in old_dict.keys():
    if i not in update_list:
        del_list.append(i)

print(update_list, new_list, del_list)
