#!/usr/bin/emv python
# -*- coding:utf-8 -*-
# small ten
china_map = {
    "华南": {
        "广东": ["广州市", "佛山市", "深圳市", "东莞市"],

        "广西": ["南宁市", "柳州市", "桂林市", "北海市"],

        "海南": ["海口市", "三亚市", "三沙市", "儋州市"]

    },
    "华东": {
        "上海": ["黄浦区", "卢湾区", "徐汇区", "长宁区", "普陀区"],

        "安徽": ["合肥市", "芜湖市", "淮南市", "马鞍山市"],

        "江苏": ["南京市", "无锡市", "徐州市", "常州市", "苏州市"]

    },
    "华北": {
        "北京": ["东城区", "西城区", "朝阳区", "丰台区", "石景山区", "海淀区"],

        "山西": ["太原市", "大同市", "阳泉市", "长治市"],

        "河北": ["石家庄市", "唐山市", "秦皇岛市", "邢台市"]

    },
    "华中": {
        "湖北": ["武汉市", "黄石市", "十堰市", "十堰市"],

        "河南": ["郑州市", "开封市", "洛阳市", "平顶山市"],

        "湖南": ["长沙市", "株洲市", "衡阳市", "邵阳市"]

    },
    "西南": {
        "重庆": ["万州区", "涪陵区", "渝中区", "大渡口区"],
        "四川": ["成都市", "自贡市", "攀枝花市", "德阳市"],
        "贵州": ["贵阳市", "六盘水市", "遵义市", "安顺市"],

    },
    "特别行政区": {
        "香港": ["屯门", "弯仔", "北角", "西贡"],
        "澳门": ["花地玛堂区", "圣安多尼堂区", "大堂区", "望德堂区"],

    },

}

print("-------------------------------------------------")
print("+            +")
print("+            +")
print("+   欢迎来到大中华地区查询系统地   +")
print("+            +")
print("+            +")
print("-------------------------------------------------")
print("大中华地区一级划分:")
for i in china_map:  # 遍历字典的key，列出大中华地区的名字

    print(i)
print("-------------------------------------------------")
jump_flag = False  # 用于跳出外循环
for i in range(3):  # 外循环，指定循环3次，3次外循环完了，就退出程序
    greater_china_name = input("请输入你要查看的大中华地区名字:")
    if greater_china_name in china_map:  # 检查输入的地区是否在地图中，如果地区名字3次输入错误，程序退出
        gc_name = china_map[greater_china_name]
        province_name = gc_name.keys()  # 使用输入的信息作为key，取出省信息，存在字典中
        while True:  # 内循环，死循环，不指定循环次数，通过break或者flag跳出
            print("------------------包含的省名字二级:-----------------")  # 分隔线
            for i in province_name:  # 遍历列表，取出省名字，打印出来
                print(i)
            print("-------------------------------------------------")  # 分隔线
            sheng_name_input = input("请输入你要查看的省名字:")

            if sheng_name_input in province_name:  # 判断输入的省名字是否在地区列表中
                shi_name = china_map[greater_china_name][sheng_name_input]  # 取出省中有哪些市，存在列表中
                print("--------------包含的城市名三级:-------------------")  # 分隔线
                for i in shi_name:  # 遍历列表，取出地区市名字，打印出来
                    print(i)
                print("------------------------------------------------")  # 分隔线

            if sheng_name_input not in province_name:  # 如果输入的省名字不在在地区列表中
                print("输入的省名字不对，请重新输入")
                continue  # 跳出当次迭代，开始下一次迭代循环，直到地市名字输入正确为止(不停的要求输入)
            back_or_quit = input("请问是否退出？按b:Back是返回上一级菜单;按q:Exit是退出整个程序")
            # 显示完地区市后，就要退出程序了，一个是全部退出，一个是返回上一级菜单
            if back_or_quit == "q":
                jump_flag = True  # 用于跳出外循环
                break  # 跳出while内循环
            if back_or_quit == "b":
                continue  # 跳出当次迭代，开始下一次迭代循环,重新输入省处，返回上一步
            print("你输入的信息有误，请重新输入")
        if jump_flag:  # 跳出外循环的条件满足
            break  # 跳出外循环
else:  # 上面的3次for循环正常执行完毕，else才会执行，如果是不正常退出（break），else不会执行
    print("3次输入错误，程序退出")