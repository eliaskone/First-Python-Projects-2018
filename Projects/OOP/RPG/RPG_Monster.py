from random import randint
class Monster():

    def __init__(self):
        self.randomname = randint(1,5)
        self.name = ""
        self.fight = 0
        self.health = 0
        self.damage = randint(1,6)
        self.monsterlist = []
        self.createmonster()
        self.attmakedamage = 0


    def createmonster(self):
        self.randomname = randint(1,5)
        if self.randomname == 1:
            self.name = "Dragon"
            self.fight = randint(12, 25)
            self.health = randint(30,80)
            self.monsterlist.append((self.name, self.fight, self.health, self.gethealth(), self.getfight(), self.getname()))

        elif self.randomname == 2:
            self.name = "Wolf"
            self.fight = randint(8,20)
            self.health = randint(25,50)
            self.monsterlist.append((self.name, self.fight, self.health))

        elif self.randomname == 3:
            self.name = "Snake"
            self.fight = randint(4,16)
            self.health = randint(20,40)
            self.monsterlist.append((self.name, self.fight, self.health))

        elif self.randomname == 4:
            self.name = "Spider"
            self.fight = randint(2,12)
            self.health = randint(15,35)
            self.monsterlist.append((self.name, self.fight, self.health))

        elif self.randomname == 5:
            self.name = "Bat"
            self.fight = randint(1,8)
            self.health = randint(10,30)
            self.monsterlist.append((self.name, self.fight, self.health))



    def getname(self):
        return self.name

    def getfight(self):
        return self.fight

    def sethealth(self, integer):
        self.health = integer

    def gethealth(self):
        return self.health

    def getdamage(self):
        return self.damage

    def makedamage(self):
        self.attmakedamage = self.getdamage() + self.getfight()

    def getmakedamage(self):
        return self.attmakedamage

