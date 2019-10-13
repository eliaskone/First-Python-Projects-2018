from random import randint
from time import sleep
from RPG_Weapon import CreateWeapon
from RPG_Herogroup import HeroGroup
from RPG_Hero import Hero

class Acrobat(Hero):

    def __init__(self):
        Hero.__init__(self)
        # if win: random gegner = tod + xp= xp+2, else: can fight = false
        # bei kampf: bodystrengh + agilitywert
        self.special = randint(1000000000000000000000000000000,10000000000000000000000000000000000000000000000)

