#### xpath模块使用

`pip install lxml`

```python
# encoding = utf-8
from lxml import etree

text = '''
        <li class='item-01'><a href='link1.html'>test1</li>
        <li class='item-02'><a href='link2.html'>test2</li>
        <li class='item-03'><a href='link3.html'>test3</li>
        <li class='item-04'><a href='link4.html'>test4</li>
        <li class='item-05'><a href='link5.html'>test5</li>
        '''
html = etree.HTML(text)

print(html)
print(etree.tostring(html).decode())

ret1 = html.xpath("//li[@class='item-04']/a/text()")
print(ret1)

ret2 = html.xpath("//li[@class='item-04']/a/@href")
print(ret2)
```
