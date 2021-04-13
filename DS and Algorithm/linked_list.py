class Node:
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.val = value
        # print(self.val)

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, x):
        node = Node(x)
        print('1--------->',self.tail)
        #print('xxx--------->', node)

        if self.tail is None:
            #print('2--------->', self.tail)
            self.head = node
            self.tail = node
            self.size += 1
            print('1st value node:', node, 'and self.tail.next= ', self.tail.next)
        else:
            # print('before node:',node ,'and self.tail.next= ',self.tail.next)
            self.tail.next = node
            print('after node:',node ,'and self.tail.next= ',self.tail.next)
            node.prev = self.tail
            #print('check tail---->',self.tail)
            self.tail = node
            print('check tail---->', self.tail)
            self.size += 1

    def __remove_node(self, node):
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next
        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev
        self.size -= 1

    def remove(self, value):
        node = self.head

        while node is not None:
            if node.val == value:
                # print('remove node is :' , node)
                self.__remove_node(node)
                # break
            node = node.next
            # print('test  ____>',node)

    def remove_last(self):
        if self.tail is not None:
            self.__remove_node(self.tail)

    def remove_first(self):
        if self.head is not None:
            self.__remove_node(self.head)

    def front(self):
        return self.head.val

    def back(self):
        return self.tail.val

    def search(self,value):
        node=self.tail
        while node is not None:
            if node.val==value:
                return print(value,'- exist in my list')
            node=node.prev
        return print(value,'does not exist in my list')


    def __str__(self):
        vals = []
        node = self.head
        while node is not None:
            vals.append(node.val)
            node = node.next
        return f"[{', '.join(str(val) for val in vals)}]"

my_list=DoubleLinkedList()
my_list.add(1)
my_list.add(2)
my_list.add(3)
my_list.add(4)
my_list.add(5)
my_list.search(100)

my_list.remove(1)

print(my_list)
