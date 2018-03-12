#encoding=utf-8
'''
minidom.Document()
该方法用于创建一个空白的xml文档对象，并返回这个doc对象
每个xml文档都是一个Document对象，代表着内存中的DOM树
'''
import xml.dom.minidom
#在内存中创建一个空的文档
doc=xml.dom.minidom.Document()
print doc

print "------------创建xml文档根节点--------------"
'''
doc.createElement(tagName)
生成xml文档节点，参数表示要生成节点的名称
'''
#创建一个根节点Managers对象
root=doc.createElement("Managers")
print u"添加的xml标签为：",root.tagName

print "================添加节点属性================="
'''
node.setAttribute(attname,value)
该方法表示给节点添加属性值对
参数说明：
attname：属性的名称
value：属性的值
'''
root.setAttribute("company","xx科技")
value=root.getAttribute("company")
print u"root元素的'company'属性值为：",value

print "-------------------添加文本节点------------------"
'''
doc.createTextNode(data)
给叶子节点添加文本节点
'''
ceo=doc.createElement("CEO")
#给叶子节点name设置一个文本节点，用于显示文本内容
ceo.appendChild(doc.createTextNode("吴总"))
print ceo.tagName
print u"给叶子节点添加文本节点成功"

print "================添加子节点========================"
'''
doc/parentNode.appendChild(node)
将节点node添加到文档对象doc作为文档树的根节点或者添加到父节点parentNode下作为子节点
'''
#给根节点添加一个叶子节点
company=doc.createElement("gloryroad")
#叶子节点下再嵌套叶子节点
name=doc.createElement("Name")
#给节点添加文本节点
name.appendChild(doc.createTextNode("光荣之路科技有限公司"))
ceo=doc.createElement("CEO")
ceo.appendChild(doc.createTextNode(u"王总"))
#将各叶子节点添加到父节点company中，然后将company添加到根节点company中
company.appendChild(name)
company.appendChild(ceo)
root.appendChild(company)
print doc.toxml()



