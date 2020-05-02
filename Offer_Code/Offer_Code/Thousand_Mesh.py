# -*- coding: utf-8 -*-
# @Time    : 2020/4/7 11:06
# @Author  : shajiu
# @FileName: Thousand_Mesh.py
# @Software: PyCharm
"""
https://www.cnblogs.com/TMesh/p/11731484.html
"""
class Mode:
    def __init__(self,data):
        self.data=data   #保存当前节点的值
        self.next=None   #保存当前节点中下一个节点的引用

        """获取node里面的数据"""
        def getData(self):
            return self.data

        """获取下一个节点的引用"""
        def getNext(self,newdata):
            return self.newdata

        """设置node里面的数据"""
        def setNext(self,newnext):
            self.next=newnext



"""
链表的定义
"""
class MySingleLinkList():
    def __init__(self):
        #定义链表的头结点
        self.head=None

def size(self):
    current=self.head    #将链表的头节点赋值给current，代表当前节点
    count=0
    while current!=None:
        count+=1
        current=current.getNext() #计算后，不断把下一个节点的引用赋值当前节点。
    return count

def add(self,val):
    temp=Node(val)
    temp.next=self.head  #将原来的开始节点设置为新开始节点的下一个节点
    self.head=temp       #将新加入节点设置为现在的第一个节点

"""
要实现查找算法，必然也是要遍历链表的，我们可以设置一个布尔变量作为是否查找到目标元素的标志
然后通过遍历链表中的每个元素，判断该元素的值是否等于要查找的值，如果是，则将布尔值设置为
True，最后返回该布尔值即可。代码如下
"""
def search(self,item):
    current=self.head
    found=False
    while current!=None and not found:
        if current.getData()==item:
            found=True
        else:
            current=current.getNext()
    return found

"""
移除指定节点remove()
"""
def remove(self,item):
    current=self.head
    previous=None
    found=False

    """判断指定是否存于链表中"""
    if not self.search(item):
        return
    while not found:
        if current.getData()==item:
            found=True
        else:
            previous=current
            current=current.getNext()
    if previous==None:
        self.head=current.getNext()
    else:
        previous.setNext(current.getNext())

"""
获取链表中所有节点的值getALLData()
"""
def getAllData(self):
    data=[]
    current=self.head
    while current:
        data.append(current.getData())
        current=current.getNext()
    return data


"""
具体的测试情况
"""
linkList=MySingleLinkList()
for i in range(10,50,5):
    linkList.add(i)

print(linkList.size())        #output:8
print(linkList.getAllData())  #output: [45, 40, 35, 30, 25, 20, 15, 10]
linkList.remove(25)
print(linkList.getAllData()) # output: [45, 40, 35, 30, 20, 15, 10]

linkList.search(25)  #output:False
linkList.isEmpyt()   #output:False
