from random import randint
from time import sleep
from RPG_Weapon import CreateWeapon
from RPG_Herogroup import HeroGroup
from RPG_Hero import Hero

class Archer(Hero):

    def __init__(self):
        Hero.__init__(self)
        #if win: damage = intelligence *2, else: health = health - intelligence
        #bei kampf: intelligence + kampfwert
        self.special = self.intelligence * 2

    def getspecial(self):
        return self.special

