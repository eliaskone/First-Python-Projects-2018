from random import randint
from time import sleep
from RPG_Weapon import CreateWeapon
from RPG_Herogroup import HeroGroup
from RPG_Hero import Hero

class Knight(Hero):

    def __init__(self):
        Hero.__init__(self)
        self.special = randint(6,12)
        #if win: damage= 6-12 + weaponstrengh, else: health = health -5
        #bei kampf: kampf + balancieren

    def getspecial(self):
        return self.special

