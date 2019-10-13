from random import randint

class CreateWeapon:
    def __init__(self):
        self.name = "empty hand"
        self.attack = 1
        self.list = (("Sword", 2), ("Axe", 3))
        self.condition = 100

    def setattack(self, integer):
        self.attack = integer

    def getattack(self):
        return self.attack

    def getcondition(self):
        return self.condition

    def setcondition(self, integer):
        self.condition = integer

    def setname(self, string):
        self.name = string

    def getname(self):
        return self.name

    def zerbrechen(self):
        random = randint(0,100)
        if self.condition <=40 and random <= 25 or self.condition<= 0:
            print("zerbrochen")
            self.setname("Leere Hand")
            self.setattack(1)

    def aufsteigen(self):
        wpnlist = ["huntingbow", "combat knife", "Sword", "Axe"]
        wpndmglist = [2, 3, 4, 5]
        random = randint(0, len(wpnlist)-1)
        print("You collected enough damage to upgrade your weapon.")

        self.name = wpnlist[random]
        self.attack = wpndmglist[random]

        print(f"You got yourself a {self.getname()}. Have fun.")
