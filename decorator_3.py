def num(func):
    print("practice decorator")
    print("learn about decorator !")
    def wrp(*args,**kwargs):
        print(kwargs)
        print(f'{kwargs.get("y")} x 5 : {kwargs.get("y") * 5} ')
        return func(*args,**kwargs)
    return wrp

@num
def something(x=3,**kwargs):
    print("previous value : ",x)

something(y=5)