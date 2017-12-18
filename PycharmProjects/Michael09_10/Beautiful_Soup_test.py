from urllib import request

import bs4

html = """

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<HTML><HEAD><TITLE>“数据结构与算法（Python 语言）”::裘宗燕</TITLE>

<META http-equiv=content-type content="text/html; charset=gb2312">
<META http-equiv=author content="裘宗燕">
<link rel="stylesheet" href="../basic.css" type="text/css">

<BODY>
<TABLE class=c_table cellSpacing=1 align=center>
  <TBODY>
  <TR>
    <TD class=c_subhead>“数据结构与算法（Python 语言）”教学材料</TD></TR>
</TBODY></TABLE>

<TABLE class=c_table cellSpacing=1 align=center>
<colgroup align=middle width=20>
<colgroup align=left width=260>
<colgroup align=middle width=80>
<colgroup align=left>
  <TBODY>
  <TR class="c_subtitle"><th colspan=4>本页提供课程的幻灯片、演示代码和其他材料。<p>
  <FONT SIZE="4">相关教科书已出版：<A HREF="http://product.china-pub.com/4909472">《数据结构与算法：Python语言描述》</A><p>
    裘宗燕著，机械工业出版社，2016年1月</FONT></th></TR>
  <TR class="c_content">
    <TD align=middle> </TD>
    <TD align=middle>幻灯片和材料目录</TD>
    <TD align=middle>发布日期</TD>
    <TD align=middle>附注</TD></TR>
<TR class="c_content">
    <TD align=middle>1</TD>
    <TD align=left>引言：<A HREF="DS1-intro.pdf">幻灯片</A>，
    <A HREF="DS1-rational.py">rational 类的实现（基本部分）</A></TD>
    <TD>两次课 2014-09-25</TD>
    <TD align=left>问题求解过程，交叉路口通行问题，算法，算法复杂性及其估计，Python程序的时间估计，问题复杂性，P-NP问题，数据与数据结构，抽象数据类型，Python的类（class）定义</TD></TR>
  <TR class="c_content">
    <TD align=middle>2</TD>
    <TD align=left>线性表(1)，连续表：<A HREF="DS2-list-1.pdf">幻灯片</A></TD>
    <TD align=middle>2014-10-09</TD>
    <TD align=left>计算机存储结构，对象和表示，线性表的概念和操作，顺序表实现，Python list, 复杂性分析</TD></TR>
  <TR class="c_content">
    <TD align=middle>3</TD>
    <TD align=left>线性表(2)，链接表：<A HREF="DS2-list-2.pdf">幻灯片</A>，<A HREF="LNode.py">结点类模块</A>，<A HREF="LList.py">简单单链表模块</A>，<A HREF="LList1.py">带尾结点引用的单链表模块</A></TD>
    <TD align=middle>2014-10-16</TD>
    <TD align=left>
链接表结构，基本技术，基本操作，加入和删除元素，操作的复杂性，Python 实现，结点类，单链表类，继承/基类/派生类，带尾结点引用的单链表</TD></TR>
  <TR class="c_content">
    <TD align=middle>4</TD>
    <TD align=left>线性表(3)，链接表的变形和应用：<A HREF="DS2-list-3.pdf">幻灯片</A>，<A HREF="LCList.py">循环单链表类模块</A>，<A HREF="LDList.py">双链表类模块</A>，<A HREF="LList+.py">带反转和排序函数的单链表类模块</A>，<A HREF="LJosephus.py">Josephus 问题的几个实现</A></TD>
    <TD align=middle>2014-10-21</TD>
    <TD align=left>循环单链表的概念和实现，双链表的概念和一个实现，单链表元素反转算法，元素排序，单链接表元素排序的两个算法（分别采用移动元素和修改链接的方法），Josephus 问题的三种解法。</TD></TR>
  <TR class="c_content">
    <TD align=middle>5</TD>
    <TD align=left>字符串(1)，概念和串匹配算法：<A HREF="DS3-string-1.pdf">幻灯片</A>，匹配函数的<A HREF="SStrings.py">代码文件</A></TD>
    <TD align=middle>2014-10-23</TD>
    <TD align=left>字符串，概念，操作，实现，Python 的 str，字符串匹配，朴素匹配算法，KMP 算法</TD></TR>
  <TR class="c_content">
    <TD align=middle>6</TD>
    <TD align=left>字符串(2)，串匹配与正则表达式：<A HREF="DS3-string-2.pdf">幻灯片</A></TD>
    <TD align=middle>2014-10-26</TD>
    <TD align=left>串匹配问题，字符串集合的描述，正则表达式，Python 的正则表达式</TD></TR>
  <TR class="c_content">
    <TD align=middle>7</TD>
    <TD align=left>栈和队列(1)，概念，栈和应用：<A HREF="DS4-stack-queue-1.pdf">幻灯片</A>，连续栈实现<A HREF="SStack.py">代码文件</A>，链接栈实现<A HREF="LStack.py">代码文件</A>，栈的应用<A HREF="StackApp1.py">代码文件</A>（括号匹配，后缀表达式求值，中缀表达式到后缀表达式的转换）</TD>
    <TD align=middle>2014-10-30</TD>
    <TD align=left>容器，缓存，数据生成和使用的顺序，栈（后进先出），队列（先进先出），栈的实现（连续表实现，链接表实现），两种 Python 实现，栈的应用：括号匹配，后缀表达式求值，中缀表达式到后缀表达式的转换</TD></TR>
  <TR class="c_content">
    <TD align=middle>8</TD>
    <TD align=left>栈和队列(2)，栈和递归，队列实现和应用：<A HREF="DS4-stack-queue-2.pdf">幻灯片</A>，队列的连续表实现<A HREF="SQueue.py">代码文件</A></TD>
    <TD align=middle>2014-11-4</TD>
    <TD align=left>栈与递归，运行栈，递归的与普通的函数调用，递归与非递归算法，队列的链接表实现，队列的连续表实现，用 list 实现队列，队列的实际应用</TD></TR>
  <TR class="c_content">
    <TD align=middle>9</TD>
    <TD align=left>栈和队列(3)，迷宫和搜索：<A HREF="DS4-stack-queue-3.pdf">幻灯片</A>，迷宫搜索问题<A HREF="StackApp2.py">代码文件</A></TD>
    <TD align=middle>2014-11-6</TD>
    <TD align=left>迷宫问题，递归求解，回溯法求解和栈，搜索问题，迷宫问题的队列缓存求解，深度和宽度优先搜索，不同搜索方法的性质，栈和队列的变形结构，Python 的 deque 类</TD></TR>
  <TR class="c_content">
    <TD align=middle>10</TD>
    <TD align=left>树和二叉树(1)，概念，性质，实现和应用：<A HREF="DS5-tree-1.pdf">幻灯片</A>，二叉树的 list 实现和表达式树的<A HREF="BiTree.py">代码文件</A></TD>
    <TD align=middle>2014-11-13</TD>
    <TD align=left>树形结构及其图示，树和树林的相关概念，二叉树的概念和性质，二叉树的 list 实现，表达式树和表达式计算</TD></TR>
  <TR class="c_content">
    <TD align=middle>11</TD>
    <TD align=left>树和二叉树(2)，优先队列，离散事件模拟，二叉树的链接实现，遍历：<A HREF="DS5-tree-2.pdf">幻灯片</A>，优先队列的两种实现<A HREF="PrioQueue.py">代码文件</A>，海关检查站模拟<A HREF="simulation-customs.py">代码文件</A></TD>
    <TD align=middle>2014-11-18</TD>
    <TD align=left>优先队列的概念，连续表实现和堆实现，离散事件模拟的概念和基本技术，通用模拟框架类，事件类，海关检查站模拟系统，二叉树的链接表示，二叉树结点类，深度优先遍历（先根，中根和后根序），宽度优先遍历</TD></TR>
  <TR class="c_content">
    <TD align=middle>12</TD>
    <TD align=left>树和二叉树(3)，二叉树的遍历，递归和非递归实现，二叉树类，哈夫曼树和哈夫曼算法，树与树林，树的实现，树与二叉树的关系：<A HREF="DS5-tree-3.pdf">幻灯片</A>，二叉树遍历和二叉树类等的<A HREF="BiTree1.py">代码文件</A>，哈夫曼算法<A HREF="Huffman.py">代码文件</A></TD>
    <TD align=middle>2014-11-20</TD>
    <TD align=left>二叉树的遍历算法，非递归先根序和后根序遍历，链接表和二叉树迭代器，二叉树类，哈夫曼树和哈夫曼算法，哈夫曼编码，树的遍历，树林的遍历，树的表示，树（树林）和二叉树之间的转换，树的 Python 实现，本章总结</TD></TR>
  <TR class="c_content">
    <TD align=middle>13</TD>
    <TD align=left>图(1)，图的概念和性质，实现，Python 实现，遍历，生成树：<A HREF="DS6-graph-1.pdf">幻灯片</A>，两个图类的定义<A HREF="Graph.py">代码文件</A>，图遍历和生成树<A HREF="GBasic.py">代码文件</A><br>（<FONT SIZE="3" COLOR="#FF0000">项目1问题<A HREF="proj-1-summary.pdf">总结</A>，供参考</FONT>）</TD>
    <TD align=middle>2014-11-27</TD>
    <TD align=left>图的概念，顶点和边，有向图和无向图，子图，路径，连通性，带权图，图的操作，图的表示，邻接矩阵，邻接表，在 Python 里的实现图，图的遍历，生成树，基于遍历构造生成树</TD></TR>
  <TR class="c_content">
    <TD align=middle>14</TD>
    <TD align=left>图(2)，最小生成树，单源点最短路径：<A HREF="DS6-graph-2.pdf">幻灯片</A>，最小生成树算法的<A HREF="GSpanTree.py">代码文件</A>，最短路径算法的<A HREF="GShortestPath.py">代码文件</A></TD>
    <TD align=middle>2014-12-2</TD>
    <TD align=left>最小生成树，Kruskal 算法，Prim 算法，最短路径，单源点最短路径，Dijkstra 算法</TD></TR>
  <TR class="c_content">
    <TD align=middle>15</TD>
    <TD align=left>图(3)，所有顶点间的最短路径，拓扑排序，关键路径：<A HREF="DS6-graph-3.pdf">幻灯片</A>，拓扑排序和关键路径的<A HREF="GToposort.py">代码文件</A>，顶点间最短路径算法也在<A HREF="GShortestPath.py">代码文件</A></TD>
    <TD align=middle>2014-12-4</TD>
    <TD align=left>所有顶点间的最短路径，Floyd-Warshal 算法，AOV 网，拓扑序列，拓扑排序和算法，AOE 网，关键路径和算法</TD></TR>
  <TR class="c_content">
    <TD align=middle>16</TD>
    <TD align=left>字典和集合(1)，字典，线性表实现，散列表实现：<A HREF="DS7-dict-1.pdf">幻灯片</A>，关联类<A HREF="Assoc.py">代码文件</A>，二分检索等的<A HREF="Dict-1.py">代码文件</A></TD>
    <TD align=middle>2014-12-11</TD>
    <TD align=left>字典的概念，关键码，检索，关联，基于线性表实现字典，基于排序表实现字典，散列，散列函数，散列表字典，冲突和冲突消解技术</TD></TR>
  <TR class="c_content">
    <TD align=middle>17</TD>
    <TD align=left>字典和集合(2)，集合，Python字典和集合，二叉排序树：<A HREF="DS7-dict-2.pdf">幻灯片</A>，二叉排序树字典类<A HREF="DictBTree.py">代码文件</A></TD>
    <TD align=middle>2014-12-16</TD>
    <TD align=left>集合，集合的线性表和排序表实现，集合的位向量实现，二叉排序树，最佳二叉排序树的概念</TD></TR>
  <TR class="c_content">
    <TD align=middle>18</TD>
    <TD align=left>字典和集合(3)，最佳二叉排序树，平衡二叉排序树：<A HREF="DS7-dict-3.pdf">幻灯片</A>，最佳二叉排序树<A HREF="DictOptBTree.py">代码文件</A>，平衡二叉排序树<A HREF="AVLTree.py">代码文件</A></TD>
    <TD align=middle>2014-12-18</TD>
    <TD align=left>最佳二叉排序树的构造，等概率和不等概率情况下的构造算法；平衡二叉排序树（AVL树），概念，性质，插入和平衡调整，插入算法</TD></TR>
  <TR class="c_content">
    <TD align=middle>19</TD>
    <TD align=left>字典和集合(4)，多分支排序树，B 树和 B+ 树：<A HREF="DS7-dict-4.pdf">幻灯片</A>。排序(1)，排序的概念，排序算法<A HREF="DS8-sort-1.pdf">幻灯片</A></TD>
    <TD align=middle>2014-12-25</TD>
    <TD align=left>插入、选择、起泡、快速等排序算法</TD></TR>
  <TR class="c_content">
    <TD align=middle>20</TD>
    <TD align=left>排序(2)，归并排序算法等<A HREF="DS8-sort-2.pdf">幻灯片</A>, <BR><A HREF="summary.pdf">课程总结</A></TD>
    <TD align=middle>2014-12-30</TD>
    <TD align=left>归并，归并排序，Timsort（Python 使用的排序算法，<A HREF="timsort.pdf">参考材料</A>），各种排序算法的比较</TD></TR>
</TBODY></TABLE>

<TABLE style="MARGIN-TOP: 5px" align=center>
  <TBODY>
  <TR>
    <TD style="HEIGHT: 13px"><HR width=660px></TD></TR>
  <TR>
    <TD 
    style="BACKGROUND: url(img/footer_01.gif); FONT: 11px Verdana; VERTICAL-ALIGN: top; COLOR: black; PADDING-TOP: 0px; HEIGHT: 14px; TEXT-ALIGN: center">本页及相关页面（除另声明者外）由<A HREF="mailto:qzy@math.pku.edu.cn">裘宗燕</A>创建维护，可自由用于各种学习活动。其他使用需得到作者许可。</TD></TR>
</TBODY></TABLE>
</BODY>
</HTML>

"""
    # 首先传入一个 html 文档，soup 是获得文档的对象。然后,文档被转换成 Unicode ,并且 HTML 的实例都被转换成 Unicode 编码
soup = bs4.BeautifulSoup("<TABLE class=c_table cellSpacing=1 align=center><TBODY>" +
  "<TR><TD class=c_subhead>“数据结构与算法（Python 语言）”教学材料</TD></TR></TBODY></TABLE>", 'lxml')
# print(soup.prettify()) # print : 格式化打印soup内容

    # Beautiful Soup 将复杂HTML文档转换成一个复杂的树形结构,每个节点都是 Python 对象,所有对象可以归纳为4种:
    # Tag
    # NavigableString
    # BeautifulSoup
    # Comment

    #tag  HTML 标签加上里面包括的内容就是 Tag
# print(soup.tr)  # 不过有一点是，它查找的是在所有内容中的第一个符合要求的标签，如果要查询所有的标签，我们在后面进行介绍
# print(type(soup.tr)) # print : <class 'bs4.element.Tag'>
    # 对于 Tag，它有两个重要的属性，是 name 和 attrs
# print(soup.name)  # print : [document]
# print(soup.tr.name) # print : tr
# print(soup.table.attrs) # print : {'class': ['c_table'], 'cellspacing': '1', 'align': 'center'}
# print(soup.table['class']) # print : ['c_table']
# soup.table['class'] = 'new'
# print(soup.table['class']) # print : new
# del soup.table['class']
# print(soup.table)

    # NavigableString  获取标签内部的文字
# print(soup.tr.string) # print : “数据结构与算法（Python 语言）”教学材料
# print(type(soup.tr.string)) # print : <class 'bs4.element.NavigableString'>
    # BeautifulSoup 对象表示的是一个文档的全部内容.大部分时候,可以把它当作 Tag 对象，是一个特殊的 Tag
# print(soup.name) # print : [document]
# print(type(soup.name)) # print : <class 'str'>
# print(soup.attrs) # print : {}
    # Comment
# soup1 = bs4.BeautifulSoup("<a class=sister href=http://example.com/elsie id=link1><!-- Elsie --></a>", 'lxml')
# print(soup1.a.string) # print : Elsie
# if type(soup1.a.string)== bs4.element.Comment:
#     print(soup1.a.string) # print : Elsie
print('-'*20 + "遍历文档树" + '-' * 20)
southtml = bs4.BeautifulSoup(html, 'lxml')
    # 遍历文档树 .contents / children  仅包含tag的直接子节点
# print(southtml.table.contents)
# print([child for child in southtml.table.children])
    # 所有子孙节点 .descendants 属性可以对所有tag的子孙节点进行递归循环
# print([child for child in southtml.table.descendants])
    # 节点内容 如果一个标签里面没有标签了，那么 .string 就会返回标签里面的内容。如果标签里面只有唯一的一个标签了，那么 .string 也会返回最里面的内容
# print(southtml.table.string)  # print : None
# print(southtml.td.string) # print : “数据结构与算法（Python 语言）”教学材料
    # 多个内容 - 灰常nice  stripped_strings/strings
# print([repr(content) for content in southtml.stripped_strings])  #页面上面肉眼看到的文字， 都找到了
    # 父节点/全部父节点  .parent/.parents
# print(southtml.table.parent.name) # print ： body
# print([child.name for child in southtml.head.title.string.parents])
    # 兄弟节点 .next_sibling .previous_sibling
# print(southtml.table.next_sibling.next_sibling)
# print(southtml.table.previous_sibling.previous_sibling) # print : None
    # 全部兄弟节点 .next_siblings .previous_siblings
# print([nextbro for nextbro in southtml.table.next_siblings])
# print([prevbro for prevbro in southtml.table.previous_siblings]) # print : ['\n']
    # 前后节点 .next_element .previous_element 它并不是针对于兄弟节点，而是在所有节点，不分层次
# s1 = bs4.BeautifulSoup("<head><title>The Dormouse's story</title></head>", 'lxml')
# print(s1.title.next_element) # The Dormouse's story
# print(s1.title.previous_element) # <head><title>The Dormouse's story</title></head>
    # 所有前后节点  .next_elements .previous_elements 迭代器就可以向前或向后访问文档的解析内容,就好像文档正在被解析一样, 连color 都解析出来了
# print([child for child in southtml.table.next_elements])
# print([child for child in southtml.table.previous_elements])

print('-'*20 + "搜索文档树" + '-' * 20)
# find_all( name , attrs , recursive , text , **kwargs )
# name 参数可以查找所有名字为 name 的 tag,字符串对象会被自动忽略掉
    # 传字符串 print soup.find_all('a')
    # 传正则表达式 print([tage for tag in soup.find_all(re.compile("^b")])
    # 传列表 soup.find_all(["a", "b"])
    # 传 True print([tage for tag in soup.find_all(True])
    # 传方法
    #     def has_class_but_no_id(tag):
    #         return tag.has_attr('class') and not tag.has_attr('id')
    #     soup.find_all(has_class_but_no_id)
# keyword 参数  （如果一个指定名字的参数不是搜索内置的参数名,搜索时会把该参数当作指定名字 tag 的属性来搜索）
    # tag 的 ”id” 属性  soup.find_all(id='link2')
    # 传入 href 参数 soup.find_all(href=re.compile("elsie"))
    # 使用多个指定名字的参数可以同时过滤 tag 的多个属性 soup.find_all(href=re.compile("elsie"), id='link1')
    # 用 class 过滤 soup.find_all("a", class_="sister")
    # 用HTML5 中的 data-* 属性过滤  data_soup.find_all(attrs={"data-foo": "value"})
# text 参数可以搜搜文档中的字符串内容
    # soup.find_all(text="Elsie")
    # soup.find_all(text=["Tillie", "Elsie", "Lacie"])
    # soup.find_all(text=re.compile("Dormouse"))
# limit 参数 当搜索到的结果数量达到 limit 的限制时,就停止搜索返回结果
    # soup.find_all("a", limit=2)
# recursive 参数 如果只想搜索 tag 的直接子节点,可以使用参数 recursive=False .
#     <html\>
#      <head\>
#       <title\>
#        The Dormouse's story
#       </title\>
#      </head\>
#     ...
#     soup.html.find_all("title")
#     \# [<title>The Dormouse's story</title>]
#
#     soup.html.find_all("title", recursive=False)
#     \# []

# find( name , attrs , recursive , text , **kwargs )
    # find_all() 方法的返回结果是值包含一个元素的列表,而 find() 方法直接返回结果
# find_parents() fin_parent()
    # find_all() 和 find() 只搜索当前节点的所有子节点,孙子节点等.
    # find_parents() 和 find_parent() 用来搜索当前节点的父辈节点,搜索方法与普通 tag 的搜索方法相同,
    #搜索文档搜索文档包含的内容
#find_next_siblings() find_next_sibling()
    # 这2个方法通过 .next_siblings 属性对当 tag 的所有后面解析的兄弟 tag 节点进行迭代,
    # find_next_siblings() 方法返回所有符合条件的后面的兄弟节点,
    # find_next_sibling() 只返回符合条件的后面的第一个 tag 节点
# find_previous_siblings() find_previous_sibling()
    #这2个方法通过 .previous_siblings 属性对当前 tag 的前面解析的兄弟 tag 节点进行迭代,
    # find_previous_siblings() 方法返回所有符合条件的前面的兄弟节点,
    # find_previous_sibling() 方法返回第一个符合条件的前面的兄弟节点
# find_all_next() find_next()
    #这2个方法通过 .next_elements 属性对当前 tag 的之后的 tag 和字符串进行迭代,
    # find_all_next() 方法返回所有符合条件的节点, find_next() 方法返回第一个符合条件的节点
# find_all_previous() 和 find_previous()
    #这2个方法通过 .previous_elements 属性对当前节点前面的 tag 和字符串进行迭代,
    # find_all_previous() 方法返回所有符合条件的节点,
    # find_previous()方法返回第一个符合条件的节点

print('-'*20 + "CSS选择器" + '-' * 20)
    # 通过标签名查找
# print(southtml.select('title')) # [<title>“数据结构与算法（Python 语言）”::裘宗燕</title>]
# print(southtml.select('a'))
    # 通过类名查找
# print(southtml.select('.c_subtitle'))
    # 通过 id 名查找
# print(soup.select('#link1')) # 网页里面对应的   <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
    # 组合查找 例如查找 p 标签中，id 等于 link1 的内容，二者需要用空格分开
# print(soup.select('p #link1'))
    # 直接子标签查找
# print(southtml.select("head > title")) # [<title>“数据结构与算法（Python 语言）”::裘宗燕</title>]
    # 属性查找 查找时还可以加入属性元素，属性需要用中括号括起来，注意属性和标签属于同一节点，所以中间不能加空格，否则会无法匹配到
# print(southtml.select('table[class="c_table"]')) # 所有table class 是叫c_table 的全部列出来
    # 同样，属性仍然可以与上述查找方式组合，不在同一节点的空格隔开，同一节点的不加空格
# print soup.select('p a[href="http://example.com/elsie"]')

