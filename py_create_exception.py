# Exception is built in class and inherit it here  ExceptionName :

class LessThanTen(Exception):
    def __init__(self,msg=""):
        self.msg = msg
    def print_exception(self):
        print("LessThanTen Error : ",self.msg)

x = int(input("Enter Number greater than ten : "))

try:
    if x<10:
        raise LessThanTen("Please Enter greater than Ten")
except LessThanTen as e:
    e.print_exception()
else:
    print("Congrats! You have successfully set  greater than ten ")
finally:
    print("Do some thing else !")
