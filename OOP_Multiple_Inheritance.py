# Multi-Inheritance
class Dancer:
    def __init__(self,style):
        self.style=style

    def dance(self):
        print(f'Dancing in {self.style}')

class Singer:
    def __init__(self,genre):
        self.genre=genre

    def sing(self):
        print(f'Singing {self.genre} music')

class Artist:
    def __init__(self,painting_material):
        self.painting_material=painting_material

class SuperHuman(Dancer,Singer,Artist):
    def __init__(self,style,genre,painting_material,sport):
        Dancer.__init__(self,style)
        Singer.__init__(self,genre)
        Artist.__init__(self,painting_material)
        self.sport=sport

    def play_sport(self):
        print(f'Playing {self.sport}')

    # Overiding thr Dance method from Dancer class

    def dance(self,competition):
        print(f'Dancing with my own {self.style} in the competition : {competition}')

nafiul=SuperHuman('Hip-Hop','classical','Acrylic','Dota-2')
print(nafiul.style)
nafiul.dance("Freshers-cup")
nafiul.play_sport()

print(help(SuperHuman))

