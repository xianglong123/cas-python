from bs4 import BeautifulSoup
import re

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html, 'lxml')

# print(soup.prettify())

# 获取第一个title标签
# print(soup.title)

# 获取所有p标签
# print(soup.findAll('p'))

# 输出第一个a标签的所有属性信息
# print(soup.a.attrs)

# 获取所有文字内容
# print(soup.get_text)

# 获取a 标签的所有href属性内容
# for link in soup.findAll('a'):
#     print(link.get('href'))

# 对soup.p的子节点进行循环输出
# for child in soup.findAll('p'):
#     print(child)

# 正则匹配，名字中带有b的标签
for tag in soup.findAll(re.compile("a")):
    print(type(tag.string))
    # print(tag.attrs)
