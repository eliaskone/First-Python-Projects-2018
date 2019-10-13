# Körperkraft, Intuition und Charisma
from random import randint
from time import sleep
from RPG_Weapon import CreateWeapon
from RPG_Herogroup import HeroGroup
from RPG_Monster import Monster

class Hero:
    Heroes = []
    def __init__(self):
        self.name = ""
        self.health = 30
        self.attack = randint(8, 16)
        self.intelligence = randint(8, 16)
        self.prestidigitation = randint(8, 16)
        self.agility = randint(8 ,16)
        self.monster = Monster()
        self.weapon = CreateWeapon()
        self.dmgcollection = 0
        Hero.Heroes.append(self)
        self.bodystrengh = randint(8 ,16)
        self.intuition = randint(8 ,16)
        self.charisma = randint(8 ,16)
        self.special = 0
        self.specialbool = True

    def getraetselnwin(self):
        return self.getintelligence()*2

    def gettaschendiebstahlwin(self):
        return 10

    def getbalancierenwin(self):
        return 2

    def getdmgcollection(self):
        return self.dmgcollection

    def setdmgcollection(self, integer):
        self.dmgcollection = integer

    def setname(self, string):
        self.name = string

    def getname(self):
        return self.name

    def sethealth(self, integer):
        self.health = integer

    def gethealth(self):
        return self.health

    def setattack(self, integer):
        self.attack = integer

    def getattack(self):
        return self.attack

    def setintelligence(self, integer):
        self.intelligence = integer

    def getintelligence(self):
        return self.intelligence

    def setprestidigitation(self, integer):
        self.prestidigitation = integer

    def getprestidigitation(self):
        return self.prestidigitation

    def setagility(self, integer):
        self.agility = integer

    def getagility(self):
        return self.agility

    def getbodystrengh(self):
        return self.bodystrengh

    def setbodystrengh(self, integer):
        self.bodystrengh = integer

    def getintuition(self):
        return self.intuition

    def setinuition(self, integer):
        self.intuition = integer

    def getcharisma(self):
        return self.charisma

    def setcharisma(self, integer):
        self.charisma = integer

    def taschendiebstahl(self):
        print("Do you want to be a thief?", self.getname())
        sleep(0.5)
        print("It is not recommended to rob")
        sleep(0.5)
        if self.monster.getfight() <= self.getprestidigitation() and self.monster.getfight() <= self.intuition:
            print("You managed to steal from your opponent")
            sleep(0.5)
            print("You are a thief now", self.getname())
            print("(︶︹︺)")
            sleep(0.5)
            print("EXP + 10", HeroGroup.herogroupInstance[0].incxp(10))
            print("Current XP:", HeroGroup.herogroupInstance[0].getxp())
            return True
        else:
            print("You are no thief", self.getname())
            print("(＾▽＾)")
            return False


    def raetseln(self):
        print("Are you intelligent enough?", self.getname())
        if self.monster.getfight() <= self.getintelligence() and self.monster.getfight() <= self.charisma:
            print("You are intelligent")
            print(HeroGroup.herogroupInstance[0].incxp(self.getintelligence()*2))
            print(f"EXP + {self.getintelligence()} * 2 = {self.getintelligence()*2}")
            print("Current XP:", HeroGroup.herogroupInstance[0].getxp())
            return True
        else:
            print("You are dumb as Stroh", self.getname())
            return False

    def balancieren(self):
        print("Are you a cyber Ninja?", self.getname())
        sleep(1)
        if self.monster.getfight() <= self.getagility() and self.monster.getfight() <= self.bodystrengh:
            print("You can balance")
            sleep(2.5)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                  "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                  "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                  "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                  "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

            print("Nice ( ͡° ͜ʖ ͡°)")
            print("You get 2 exp points", HeroGroup.herogroupInstance[0].incxp(2))
            print("Current XP:", HeroGroup.herogroupInstance[0].getxp())
            return True
        else:
            sleep(0.5)
            print("You failed to balance?", self.getname())
            sleep(1)
            print("You had only one job")
            print("(」°ロ°)」")
            sleep(1)
            print("Wow you even lost 10 hp (￢_￢;)")
            self.sethealth(self.gethealth()-10)
            print(f"HP {self.gethealth()}")
            return False