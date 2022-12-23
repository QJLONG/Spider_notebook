import re

# findall: Matches every regex-compliant content in the string.
target = "My phone is 10086. And my girlfriend's phone is 10010."
lst = re.findall(r"\d+", target)
print(lst)

'''
    ['10086', '10010']
'''


# finditer: Matches every regex-compliant content in the string.(The content returned is an iterator). We can get
#           contents by function group()
it = re.finditer(r"\d+", target)
print(it)
'''
    <callable_iterator object at 0x0000028922CD5340>
'''
for i in it:
    print(i.group())
'''
    10086
    10010
'''


# search: Matches the first regx-compliant content in the string.
#         It returns a match object(get contents by function group())
ser = re.search(r"\d+", target)
print(ser.group())
'''
    10086
'''


# match:  Matches the string from the very beginning. It returns match object,too.
mat = re.match(r"\d+", target)
print(mat.group())
'''
    AttributeError: 'NoneType' object has no attribute 'group'
'''


# preload regular expression.
obj = re.compile(r"\d+")

ret = obj.finditer(target)
for i in ret:
    print(i.group())
'''
    10086
    10010
'''


# Filtering from matches
s = '''
<div class='jar'><span id='1'>郭麒麟</span></div>
<div class='jj'><span id='2'>宋铁</span></div>
<div class='jay'><span id='3'>大聪明</span></div>
<div class='lisa'><span id='4'>胡说八道</span></div>
'''

comp = re.compile(r"<div class='.*?'><span id='(?P<id>\d)'>(?P<name>.*?)</span></div>")
ret = comp.finditer(s)
for i in ret:
    print(f"{i.group('id')}: {i.group('name')}")
'''
    1: 郭麒麟
    2: 宋铁
    3: 大聪明
    4: 胡说八道
'''


