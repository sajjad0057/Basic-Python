# COMPOSITION
class StoryBook:
    # class Variable
    no_of_books = 0
    discount = 0.5  # its called class variable

    def __init__(self, name, price, author_name, author_born, no_of_page):
        self.name = name
        self.price = price
        self.author_name = author_name
        self.author_born = author_born
        self.no_of_page = no_of_page
        StoryBook.no_of_books += 1

    #  regular_method
    def get_book_info(self):
        print(f'The Book name : {self.name}, price : {self.price}, pages: {self.no_of_page}')

    def get_author_info(self):
        print(f'Author name : {self.author_name} , Born : {self.author_born}')

    # applying discount to an instance

    def apply_discount(self):
        self.price = int(self.price - self.price * StoryBook.discount)


class Library:
    def __init__(self, book_list=None):
        self.book_list = []
        if book_list is not None:
            self.book_list.append(book_list)

    def get_all_books(self):

        for book in self.book_list:
            print(f'Title : {book.name}, Author : {book.author_name} , price : {book.price}')

    def add_book(self, book):
        self.book_list.append(book)

    def remove_book(self, book):
        self.book_list.remove(book)



# creating Instance
book_1 = StoryBook('xyz', 300, 'abc', 1999, 2985)
book_2 = StoryBook('mnv', 7567, 'uutu', 1995, 576)

# book_1.get_book_info()
# book_1.get_author_info()

public_library = Library(book_1)
public_library.add_book(book_1)
public_library.add_book(book_2)
public_library.get_all_books()
public_library.remove_book(book_1)
public_library.get_all_books()
