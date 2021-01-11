class StoryBook:
    no_of_books=0
    discount =0.5   # its called class variable
    def __init__(self,name,price,author,date):
        self.name=name
        self.price=price
        self.author=author
        self.p_date=date
        StoryBook.no_of_books += 1

    def applying_discount(self):
        self.price = int(self.price * StoryBook.discount)
        return self.price

    def __str__(self):
        return str(self.name) #,self.y,self.z,self.w


    #CLASS METHOD

    @classmethod    # its works like alternative constractor
    def set_discount(cls,new_discount):
        cls.discount=new_discount

    @classmethod
    def construct_from_string(cls,book_str):
        name, price, author, date = book_str.split(',')
        return cls(name, price, author, date)

    # STATIC_METHOD

    @staticmethod

    def check_price(price):
        if int(price)>100:
            print("Price is greather than 100")
        else:
            print("price is less than 100")





book_1=StoryBook('sajjad',30,'zahan','2-3-4')
book_2=StoryBook('sajjad',100,'zahan','2-3-4')
# print(book_2)
# book_2.discount=0.6
# print(book_2.applying_discount())
# print(book_2)
# print(StoryBook.no_of_books)

# print(book_1.price)
# print(book_1.discount)
# StoryBook.set_discount(0.7)
# print(book_2.applying_discount())

book_str = 'Harry Poter, 200, JK Rowling, 1970'

harry_poter=StoryBook.construct_from_string(book_str)
print(harry_poter)
StoryBook.check_price(harry_poter.price)
