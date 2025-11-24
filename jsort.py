class node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)
    def __lt__(self,rhs):
        if self.data<rhs.data:
            return self
        else:
            return rhs

class linkedList:
    head, tail, size = 0,0,0
    def __init__(self,head=None):
        if head != None:
            self.head=node(head)
            self.tail=self.head
            while self.tail != None:
                self.size+=1
                self.tail=self.tail.next
        else:
            self.head=None
            self.tail=None
            self.size = 0

    def __str__(self):
        result=""
        temp=self.head
        while temp!=None:
            result+=str(temp.data)
            temp = temp.next
        # print()
        # print("Head:",self.head,"\tTail:",self.tail)
        return result

    def add(self,item):
        temp=node(item)
        temp.next=self.head
        self.head=temp
        if self.size==0:
            self.tail=self.head
        self.size+= 1

    def append(self,item):
        if self.size==0:
            self.add(item)
        else:
            temp=node(item)
            self.tail.next=temp
            self.tail=temp
            self.size+=1

    def remove(self):
        if self.size>0:
            temp=self.head
            self.head=self.head.next
            self.size -= 1
            return temp
        else:
            self.tail=self.head
            return None

def listmerge(a,b):
    left,right=None,None
    a=linkedList(a)
    b=linkedList(b)
    c=linkedList()
    while a.size+b.size>0:
        if a.head==None:
            c.append(b.remove())
        elif b.head==None:
            c.append(a.remove())
        else:
            nexta=a.remove()
            nextb=b.remove()
            if nexta>nextb:
                c.add(nexta)
                mexta=a.remove()
            else:
                c.add(nextb)
                nextb=b.remove()
    return c

spine=[]
myList=linkedList()
data = int(input("Enter a number:"))
while data>0:

    if myList.size==0:
        myList.add(data)
    elif myList.head.data>data:
        myList.add(data)
    elif myList.tail.data<data:
        myList.append(data)
    else:
        spine.append(myList)
        print("Spine size:", len(spine))
        myList=linkedList()
        myList.add(data)

    data = int(input("Enter a number:"))

spine.append(myList)

for l in spine:
    print((linkedList(l)))

while len(spine)>1:
    listmerge(spine[0],spine[-1])
    spine.pop()