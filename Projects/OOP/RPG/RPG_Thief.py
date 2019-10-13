from random import randint
from time import sleep
from RPG_Weapon import CreateWeapon
from RPG_Herogroup import HeroGroup
from RPG_Hero import Hero

class Thief(Hero):
    pass

    def __init__(self):
        Hero.__init__(self)
        #if win: damage = fingerfertigkeit *2, else: health = health -5
        #bei kampf: agility + ituition
        self.special = self.prestidigitation * 2

    def getspecial(self):
        return self.special