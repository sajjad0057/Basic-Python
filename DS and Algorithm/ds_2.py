from linked_list import DoubleLinkedList



class Stack:
    def __init__(self):
        self.__list=DoubleLinkedList()

    def push(self,val):
        self.__list.add(val)

    def pop(self):
        val = self.__list.back()
        self.__list.remove_last()
        return val

    def is_empty(self):
        return self.__list.size==0

    def peek(self):
        return self.__list.back()

    def __len__(self):
        return self.__list.size


class Queue:
    def __init__(self):
        self.__list = DoubleLinkedList()

    def enqueue(self,val):
        self.__list.add(val)

    def dequeue(self):
        val = self.__list.front()
        self.__list.remove_first()
        return val

    def is_empty(self):
        return self.__list.size==0

    def front(self):
        return self.__list.front()

    def __len__(self):
        return self.__list.size












# my_stack=Stack()
# my_stack.push(1)
# my_stack.push(2)
# my_stack.push(3)
# my_stack.push(5)
# print(my_stack.peek())
# print(len(my_stack))
# print(my_stack.pop())
# print(len(my_stack))
# print(my_stack.peek())