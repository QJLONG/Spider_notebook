# xpath 是在XML文档中搜索内容的一门语言
# html 是XML的一个子集
'''
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <author>
        <nick>周大强</nick>
        <nick>周芷若</nick>
        <div>
            <nick>王宝强</nick>
        </div>
    </author>
</book>
'''
from lxml import etree

xml = '''
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <author>
        <nick href="zhou">周大强</nick>
        <nick href="ruo">周芷若</nick>
        <div>
            <nick>王宝强</nick>
            <span>
                <nick>周深</nick>
            </span>
        </div>
        <span>
                <nick>薛之谦</nick>
        </span>
    </author>
</book>
'''

tree = etree.XML(xml)
# result = tree.xpath("/book/name")     # /表示层级关系，第一个/表示根节点
# result = tree.xpath("/book/name/text()")     # /text()表示获取内容
# result = tree.xpath("/book/author//nick/text()")    # //表示查找所有符合条件的后代，即可以匹配任意数量的任意节点
# result = tree.xpath("/book/author/*/nick/text()")    # *表示任意节点，但只能匹配一层节点
# result = tree.xpath("/book/author/nick[1]/text()")       # 匹配所有当前层第一个符合条件的节点，【】只能用于同一层，即存在//匹配所有的时候不可用
result = tree.xpath("/book/author/nick[@href='zhou']/text()")       # 按照属性查找：[@name="value"]
attribute = tree.xpath("/book/author/nick/@href")       # 获取标签内的属性值

print(attribute)



