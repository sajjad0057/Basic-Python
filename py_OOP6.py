'''
method overwriting/ovrloading!
'''
class phone:
    def __init__(self):
        print("Now days Phn is very nescesary");
class sumsang(phone):
    def __init__(self):
        super().__init__()
        print("Sumsang is the popular brand of phone");
s=sumsang();
