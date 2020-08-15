class phone: #here Phone is parrent class!
    def call(self):
        print("Phn is mostly used for calling");
    def message(self):
        print("Phn is also used for transfering Text");
class Nokia(phone): #In nokia class inharited phone class method!
    def photo(self):   #SO Nokia is child class of phone class!
        print("By nokia phone you can take photo clearly");

N=Nokia(); # N is the object of Nokia Class!
N.call();
N.message();
N.photo();
print(issubclass(Nokia,phone));
