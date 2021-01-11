# OOP Inheritance :

class Robot:
    def __init__(self,name,version):
        self.name=name
        self.version= version

    def __repr__(self):
        return  self.name

    def move_forward(self):
        print(f'{self.name} is moving forward !')

    def move_backward(self):
        print(f'{self.name} is moving backward !')

    def move_right(self):
        print(f'{self.name} is moving right !')

    def move_left(self):
        print(f'{self.name} is moving left !')



class HouseBot(Robot):
    def __init__(self,name,version,area_covered):
        Robot.__init__(self,name,version)   #also we can write super().__init__(name,version)
        self.area_covered=area_covered


    def clean(self):
        if self.area_covered>0:
            print(self.area_covered)
            print(f'{self.name} is cleaning the house !')
            self.area_covered -=30
            if self.area_covered<0:
                self.area_covered=0

        else:
            print(f'Can\'t clean ,PLEASE RESET AREA COVERED!')

    def set_cover_area(self,area):
        if self.area_covered==0:
            self.area_covered=area
        else:
            print('I can still clean more area')

    @staticmethod
    def halt():
        print('I am halting now!')

    #overidding & polymorphism
    def move_forward(self):
        super().move_forward()
        print('This is in house bot class ')


class maidbot(HouseBot):
    def __init__(self,name,version,area_covered,cooking):
        super().__init__(name,version,area_covered)
        self.cooking=cooking






H=maidbot('alex',3.05,50,'rice')
print(H)





# hBot=HouseBot('power',1.0,40)
# robo=Robot('stan li',2.0)
# print(help(Robot))
# print(help(list))
# print(help(HouseBot))

# print(hBot)
# hBot.move_forward()
# hBot.clean()
# hBot.clean()
# hBot.clean()
# hBot.set_cover_area(70)
# hBot.clean()
# hBot.clean()
# hBot.clean()
#
# hBot.halt()


