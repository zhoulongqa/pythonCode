#encoding=utf-8
'''
minidom.parse(parser=None,bufsize=None)
该函数的作用是使用parse解析器打开xml文档，并将其解析为DOM文档，也就是内存中
的一棵树，并得到这个DOM对象
'''
#从xml.dom.minidom模块引入解析器parse
from xml.dom.minidom import parse

#minidom解析器打开xml文档并将其解析为内存中的一棵树
DOMTree=parse(r"D:\python\book.xml")
print type(DOMTree)


'''
dom.documentElement
获取xml文档对象，就是拿到DOM树的根
'''
#获取xml文档对象，就是拿到树的根
booklist=DOMTree.documentElement
print booklist

#返回xml的文本内容
print u"DOM树的根对象：",booklist
print u"xml文档内容：\n%s"% DOMTree.toxml()
print "------------------------判断某属性是否存在------------------"
#判断是否包含属性
if booklist.hasAttribute("type"):
    print u"booklist元素存在type属性"
else:
    print u"booklist元素不存在type属性"

'''
hasAttribute(name)：判断某个节点node是否存在某个属性，存在则返回True，否则返回False
'''


print "---------------------获取属性---------------------"
'''
node.getAttribute(attname)
获取节点node的某个属性的值
'''
print "Root element is",booklist.getAttribute("type")


print "=======================获取节点元素================="
'''
node.getElementsByTagName
获取XML文档中某个节点下具有节点名的节点对象集合
在下面的XML程序中，getElementsByTagName()函数返回的是同一个节点下的同级节点中
相同标签的集合，这是一个list对象，所以可以使用列表中的所有操作。
这个时候，可以通过索引去拿相应的节点，也可以使用节点名拿相应的节点，也可以通过循环遍历整个返回的list
注意：
就算某个父节点下没有同名的节点，该方法返回的仍是一个list，只是此时的list是一个空list
'''
#获取booklist对象中所有book节点的list集合
books=booklist.getElementsByTagName("book")
print type(books)
print books

print "*********************获取节点元素************************"
'''
node.childNodes
返回节点node下所有子节点组成的list
'''
#获取booklist对象中所有book节点的list集合
books=booklist.getElementsByTagName("book")
print books[0].childNodes
print books[1].childNodes


print "---------------------获取节点文本值------------------------"
books=booklist.getElementsByTagName("book")
print u"book节点的个数：",books.length
for book in books:
    print "***book***"
    if book.hasAttribute("category"):
        print u"category is:",book.getAttribute("category")
    #根据节点名title拿到这个book节点下所有的title节点的集合list
    #[0]表示第一个title标签，因为一个<book> ... </book>之间可能会定义多个title标签
    title=book.getElementsByTagName('title')[0]
    print "Title is:",title.childNodes[0].data
    author=book.getElementsByTagName("author")[0]
    print "autor is:",author.childNodes[0].data
    pageNumber=book.getElementsByTagName("pageNumber")[0]
    print "pageNumber is:",pageNumber.childNodes[0].data

print "----------------------判断是否有子节点------------------"
'''
node.hasChildNodes()
判断节点node下是否有子节点，如果有返回True，否则返回False，但是需要注意的是，，
每个节点都默认有一个文本叶子节点，所以只要标签后有值，就返回True，只有当标签后没
值时并且也没有叶子节点时才会返回False
'''
#获取booklist对象中所有book节点的list集合
books=booklist.getElementsByTagName("book")
print u"book节点的个数：",books.length
print books[0]
if books[0].hasChildNodes():
    print u"存在叶子节点:\n",books[0].childNodes
else:
    print u"不存在叶子节点"


