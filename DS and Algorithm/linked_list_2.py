class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next


    def __repr__(self):
        return repr(self.data)

class LinkedList:
    def __init__(self):
        self.head=Node()
        self.size = 0
        #print('1 ------->',self.head)

    def __repr__(self):
        nodes=[]

        current_node = self.head.next
        #print('2 ------->', current_node)

        while current_node:
            #print('** ------->',repr(current_node))
            nodes.append(repr(current_node))
            current_node=current_node.next
            #print('*** ---------->',current_node)


        return ','.join(nodes)




    def preappend(self,data):
        node=Node(data,self.head.next)
        #print('3 ----->',node)
        self.head.next=node
        self.size +=1


    def append(self,data):
        node=Node(data)
        #print('4 ------>', node)
        if self.head.next is None:
            self.head.next=node
            return
        current_node=self.head.next

        #print('5 ------->', current_node)

        while current_node.next:
            current_node = current_node.next
            #print('6------->', current_node)

        current_node.next=node
        self.size += 1
        #print('7------->', current_node)

    def search(self,item):
        current_node=self.head.next
        while current_node:
            if current_node.data==item:
                return print(item,"-exist in the list")
            current_node=current_node.next
        return print(item,"-does not exist in the list")

    def remove(self, item):
        previous_node=self.head
        current_node=previous_node.next

        while current_node:
            if current_node.data==item:
                break
            previous_node=current_node
            current_node=current_node.next

        if current_node is None:
            return None
        if self.head==previous_node:
            self.head.next=current_node.next
        else:
            previous_node.next=current_node.next
        self.size -= 1



    def insert(self,data,new_data):
        current_node=self.head.next

        while current_node:
            if current_node.data==data:
                new_node=Node(new_data,current_node.next)
                current_node.next=new_node
                break
            current_node=current_node.next





my_list=LinkedList()

my_list.preappend(2)
my_list.append(4)
my_list.append(5)
my_list.search(7)
print(my_list.size)
print(my_list)
my_list.remove(5)
print(my_list)
my_list.insert(4,7)
print(my_list.size)
