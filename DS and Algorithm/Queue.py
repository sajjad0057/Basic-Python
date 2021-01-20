class Queue:
    def __init__(self,size):
        self.item = [None]*size
        self.max_size=size
        self.head=0
        self.tail=0
        self.size=0

    def __is_full(self):
        if self.size==self.max_size:

            return True
        return False


    def enqueue(self,item):
        if self.__is_full():
            self.tail = 0

            return print("queue full !!")

        self.item[self.tail]=item
        self.tail=(self.tail + 1)%self.max_size
        self.size +=1
        print('enqueue size',self.size)
    def dequeue(self):
        item=self.item[self.head]
        self.head=(self.head+1)%self.max_size
        self.size -=1

        print('dequeue size',self.size)
        return item
    def is_empty(self):
        if self.item==[]:
            return True
        return False
q_size=int(input("Plz enter Queue size: "))
q = Queue(q_size)


while True:
    x = input(f"If you want to Enqueue - Plz press 1, or want to Dequeue - Plz press 2: ")
    if x == '1':
        while True:
            print("Enqueue Plz,(If want to exit type exit): ")
            Entry = input()
            if Entry == "exit":
                break
            q.enqueue(Entry)
    elif x == '2':
        print(q.dequeue())

    # break

