__author__ = "Alex Li"


name = "my \tname is {name} and i am {year} old"

print(name.capitalize()) #首字符大写
print(name.count("a")) # 统计a的个数
print(name.center(50,"-")) # 把name放在中间，总共打印50不够用-
print(name.endswith("ex")) # 以什么结尾，结果bool型
print(name.expandtabs(tabsize=30)) # 把tab键转成多少个空格
print(name[name.find("name"):]) # 查找查到的字符的索引，可以切片
print(name.format(name='alex',year=23)) # 格式化
print(name.format_map(  {'name':'alex','year':12}  )) # 格式化字符串
print('ab23'.isalnum()) # 是不是一个阿拉伯数字，bool型
print('abA'.isalpha()) # 是不是纯英文字符
print('1A'.isdecimal()) # 是不是一个十进制
print('1A'.isdigit()) # 是不是整数
print('a 1A'.isidentifier()) #判读是不是一个合法的标识符，是不是一个合法变量名
print('33A'.isnumeric())  # 是不是一个数字
print('My Name Is  '.istitle()) #
print('My Name Is  '.isprintable()) #tty file ,drive file，是否可打印
print('My Name Is  '.isupper())
print('+'.join( ['1','2','3'])  ) #把一个列表拼接成字符串
print( name.ljust(50,'*')  ) # 后面补全
print( name.rjust(50,'-')  ) # 前面补全
print( 'Alex'.lower()  ) # 大写转小写
print( 'Alex'.upper()  ) # 小写转大写
print( '\nAlex'.lstrip()  ) # 去掉左边空格回车
print( 'Alex\n'.rstrip()  ) # 去掉右边的空格和回车
print( '    Alex\n'.strip()  ) # 去掉所有空格和回车
p = str.maketrans("abcdefli",'123$@456') # 数据对应一样多
print("alex li".translate(p) ) # 对应修改

print('alex li'.replace('l','L',1)) # 替换第一个l换成大写
print('alex lil'.rfind('l'))  # 找到最后边的值得下标返回
print('1+2+3+4'.split('\n')) # 把字符串按照指定字符分成一个列表
print('1+2\n+3+4'.splitlines())
print('Alex Li'.swapcase())
print('lex li'.title()) # tille
print('lex li'.zfill(50)) # 自动使用0补位

print( '---')

