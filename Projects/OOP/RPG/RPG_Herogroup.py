from RPG_Weapon import CreateWeapon
from time import sleep
from random import randint
from RPG_Monster import Monster

class HeroGroup:
    herogroupInstance = []

    def __init__(self):
        self.group = []
        self.name = ""
        HeroGroup.herogroupInstance.append(self)
        self.xp = 0
        self.weapon = CreateWeapon()
        self.monster = Monster()
        used = False

    def getxp(self):
        return self.xp

    def setxp(self, integer: object) -> object:
        self.xp = integer

    def incxp(self, inc):
        self.xp += inc

    def setgroup(self, lst):
        self.group = lst

    def getgroup(self):
        return self.group

    def setname(self, string):
        self.name = string

    def getname(self):
        return self.name

    def rest(self):
        restt = int(input("Do you want to repair your weapon[1], "
                          "or do you want to regenerate your health?[2]"))
        used = False
        while not used:
            for hero in self.group:
                restt=int(input("Do you want to repair your weapon[1], "
                      "or do you want to regenerate your health?[2]"))

                if restt == 1:
                    hero.weapon.setcondition(hero.weapon.getcondition()+10)
                    print(hero.weapon.getcondition())

                if restt == 2 and used == False:
                    hero.sethealth(hero.gethealth()+10)
                    print("hero new helth:",hero.gethealth())
                    used = True


    def aufsteigen(self):
        if self.getxp() >= 100:
            print("Vegeta what does the scouter say about his Power Level?!")
            sleep(3)
            print("IT´S OVER 9000!!!")
            self.setxp(self.getxp()-100)
            for x in self.group:
                choice = int(input("Impossible!!!You´re Power Level is Over 9000. You can upgrade one of your attribute, which such "
                                   "a Power Level. Which attribute would you like to upgrade?[attack(1), agility(2), "
                               "inteligence(3), prestidigitaion(4), itiution(5), charisma(6), bodystrengh(7)"
                               "]"))
                if choice == 1:
                    for i in self.group:
                        i.setattack(i.getattack()+1)
                        print(f"ATTACK = {i.getattack}")

                elif choice == 2:
                    for i in self.group:
                        i.setagility(i.getafility()+1)
                        print(f"AGILITY = {i.getagility}")

                elif choice == 3:
                    for i in self.group:
                        i.setintelligence(i.getintelligence()+1)
                        print(f"INTELLIGENCE = {i.getintelligence}")

                elif choice == 4:
                    for i in self.group:
                        i.setprestidigitation(i.getprestidigitation()+1)
                        print(f"PRESTIDIGITATION = {i.getprestidigitation}")

                elif choice == 5:
                    for i in self.group:
                        i.setprestidigitation(i.getintuition()+1)
                        print(f"INTUITION = {i.getintuition}")

                elif choice == 6:
                    for i in self.group:
                        i.setprestidigitation(i.getcharisma()+1)
                        print(f"CHARISMA = {i.getcharisma}")

                elif choice == 7:
                    for i in self.group:
                        i.setprestidigitation(i.getintuition() + 1)
                        print(f"BODYSTRENGH = {i.getintuition}")


    def angreifen(self):
        weaponcrack = self.weapon.zerbrechen()
        dmgdice = randint(1, 6)
        dmg = dmgdice + self.weapon.getattack()
        print("A wild monster appears")
        sleep(0.5)
        print("/╲/\╭(ఠఠ益ఠఠ)╮/\╱`")
        self.monsters = [0 , 0, 0, 0]
        for i in range(4):
            self.monster = Monster()
            self.monsters[i-1] = (self.monster)
        self.group[0].specialbool = True
        done = False
        acrobatfail = False
        while not done:
            self.checkherodeath() #Knight attack
            self.allherodead()
            self.checkmonsterdeath()
            self.allmonsterdead()
            wattack = int(input(f"Which Monster do you want to attack, Knight?{self.monsters[0].getname()}, {self.monsters[1].getname()}, " 
                                f"{self.monsters[2].getname()}, {self.monsters[3].getname()}"))
            if self.monsters[wattack-1].getfight() <= self.group[0].getattack() and self.monsters[wattack-1].getfight() <= self.group[0].agility:
                special = int(input("Do you want to use your special? 1 = Yes, 2 = No"))

                if special == 1 and self.group[0].specialbool:
                    self.monsters[wattack-1].sethealth(self.monsters[wattack-1].gethealth() - self.group[0].getattack() + self.group[0].special)
                    print("You hit", self.monsters[wattack-1].getname())
                    sleep(0.5)
                    print(self.monsters[wattack-1].getname(), "Health:", self.monsters[wattack-1].gethealth())
                    self.checkmonsterdeath()
                    self.allmonsterdead()
                    sleep(1)
                    self.weapon.aufsteigen()
                    print(self.weapon.name, "makes", self.weapon.attack, "damage")
                    self.group[0].specialbool = False
                    self.weapon.setcondition(self.weapon.getcondition() - randint(1,5))
                    self.weapon.zerbrechen()

                else:
                    self.monsters[wattack - 1].sethealth(
                        self.monsters[wattack - 1].gethealth() - self.group[0].getattack() + dmgdice)
                    print("You hit", self.monsters[wattack - 1].getname())
                    sleep(0.5)
                    print(self.monsters[wattack - 1].getname(), "Health:", self.monsters[wattack - 1].gethealth())
                    self.checkmonsterdeath()
                    self.allmonsterdead()
                    sleep(1)
                    self.weapon.aufsteigen()
                    print(self.weapon.name, "makes", self.weapon.attack, "damage")
                    self.group[0].specialbool = True
                    self.weapon.setcondition(self.weapon.getcondition() - randint(1, 5))
                    self.weapon.zerbrechen()
            else:
                print("How could you miss that punch?", self.group[0].getname())
                sleep(2)
                print("┐('～`;)┌")
                sleep(2)
                print("Really you got hit?(↼_↼)")
                print("You lose 5 healthpoints")
                self.group[0].sethealth(self.group[0].gethealth() - 5)
                print(self.group[0].getname(),"current health:", self.group[0].gethealth())
                self.checkherodeath()
                self.allherodead()

            if self.monsters[0].getfight() >= self.group[0].getattack():
                self.group[0].sethealth(self.group[0].gethealth()-self.monsters[0].getdamage() + dmgdice)
                print(self.group[0].getname(),"Health:",self.group[0].gethealth())

            self.checkherodeath() #Archer Attack
            self.allherodead()
            self.checkmonsterdeath()
            self.allmonsterdead()
            wattack = int(input(
                f"Which Monster do you want to attack, Archer?{self.monsters[0].getname()}, {self.monsters[1].getname()}, "
                f"{self.monsters[2].getname()}, {self.monsters[3].getname()}"))

            if self.monsters[wattack-1].getfight() <= self.group[1].getattack() and self.monsters[wattack-1].getfight() <= self.group[1].getintelligence():
                special = int(input("Do you want to use your special? 1 = Yes, 2 = No"))

                if special == 1 and self.group[1].specialbool:
                    self.monsters[wattack-1].sethealth(self.monsters[wattack-1].gethealth() - self.group[1].getspecial())
                    print("You hit", self.monsters[wattack-1].getname())
                    sleep(0.5)
                    print(self.monsters[wattack-1].getname(), "Health:", self.monsters[wattack-1].gethealth())
                    self.checkmonsterdeath()
                    self.allmonsterdead()
                    sleep(1)
                    self.weapon.aufsteigen()
                    print(self.weapon.name, "makes", self.weapon.attack, "damage")
                    self.group[1].specialbool = False
                    self.weapon.setcondition(self.weapon.getcondition() - randint(1, 5))
                    self.weapon.zerbrechen()

                else:
                    self.monsters[wattack - 1].sethealth(
                        self.monsters[wattack - 1].gethealth() - self.group[1].getattack() + dmgdice)
                    print("You hit", self.monsters[wattack - 1].getname())
                    sleep(0.5)
                    print(self.monsters[wattack - 1].getname(), "Health:", self.monsters[wattack - 1].gethealth())
                    self.checkmonsterdeath()
                    self.allmonsterdead()
                    sleep(1)
                    self.weapon.aufsteigen()
                    print(self.weapon.name, "makes", self.weapon.attack, "damage")
                    self.group[1].specialbool = True
                    self.weapon.setcondition(self.weapon.getcondition() - randint(1, 5))
                    self.weapon.zerbrechen()

            else:
                print("How could you miss that punch?", self.group[1].getname())
                sleep(2)
                print("┐('～`;)┌")
                sleep(2)
                print("Really you got hit?(↼_↼)")
                print("You lose healthpoints")
                self.group[1].sethealth(self.group[1].gethealth() - self.group[1].getintelligence())
                print(self.group[1].getname(),"current health:", self.group[1].gethealth())
                self.checkherodeath()
                self.allherodead()

            if self.monsters[1].getfight() >= self.group[1].getattack():
                self.group[1].sethealth(self.monsters[1].getdamage() + dmgdice)
                print(self.group[1].getname(), "Health:", self.group[1].gethealth())

            self.checkherodeath()  # Thief Attack
            self.allherodead()
            self.checkmonsterdeath()
            self.allmonsterdead()

            wattack = int(input(
                f"Which Monster do you want to attack, Thief?{self.monsters[0].getname()}, {self.monsters[1].getname()}, "
                f"{self.monsters[2].getname()}, {self.monsters[3].getname()}"))

            if self.monsters[wattack - 1].getfight() <= self.group[2].getagility() and self.monsters[
                wattack - 1].getfight() <= self.group[2].getintuition():
                special = int(input("Do you want to use your special? 1 = Yes, 2 = No"))

                if special == 1 and self.group[2].specialbool:
                    self.monsters[wattack - 1].sethealth(
                        self.monsters[wattack - 1].gethealth() - self.group[2].getspecial())
                    print("You hit", self.monsters[wattack - 1].getname())
                    sleep(0.5)
                    print(self.monsters[wattack - 1].getname(), "Health:", self.monsters[wattack - 1].gethealth())
                    self.checkmonsterdeath()
                    self.allmonsterdead()
                    sleep(1)
                    self.weapon.aufsteigen()
                    print(self.weapon.name, "makes", self.weapon.attack, "damage")
                    self.group[2].specialbool = False
                    self.weapon.setcondition(self.weapon.getcondition() - randint(1, 5))
                    self.weapon.zerbrechen()

                else:
                    self.monsters[wattack - 1].sethealth(
                        self.monsters[wattack - 1].gethealth() - self.group[2].getattack() + dmgdice)
                    print("You hit", self.monsters[wattack - 1].getname())
                    sleep(0.5)
                    print(self.monsters[wattack - 1].getname(), "Health:", self.monsters[wattack - 1].gethealth())
                    self.checkmonsterdeath()
                    self.allmonsterdead()
                    sleep(1)
                    self.weapon.aufsteigen()
                    print(self.weapon.name, "makes", self.weapon.attack, "damage")
                    self.group[2].specialbool = True
                    self.weapon.setcondition(self.weapon.getcondition() - randint(1, 5))
                    self.weapon.zerbrechen()

            else:
                print("How could you miss that punch?", self.group[0].getname())
                sleep(2)
                print("┐('～`;)┌")
                sleep(2)
                print("Really you got hit?(↼_↼)")
                print("You lose healthpoints")
                self.group[2].sethealth(self.group[2].gethealth() - 5)
                print(self.group[0].getname(), "current health:", self.group[2].gethealth())
                self.checkherodeath()
                self.allherodead()

            if self.monsters[2].getfight() >= self.group[2].getattack():
                self.group[2].sethealth(self.group[2].gethealth() - self.monsters[2].getdamage()+dmgdice)
                print(self.group[2].getname(), "Health:", self.group[2].gethealth())

            self.checkherodeath()  # Acrobat Attack
            self.allherodead()
            self.checkmonsterdeath()
            self.allmonsterdead()

            wattack = int(input(
                f"Which Monster do you want to attack, Thief?{self.monsters[0].getname()}, {self.monsters[1].getname()}, "
                f"{self.monsters[2].getname()}, {self.monsters[3].getname()}"))
            randommonster = randint(0, len(self.monsters) - 1)

            if self.monsters[wattack - 1].getfight() <= self.group[3].getbodystrengh() and self.monsters[
                wattack - 1].getintuition() <= self.group[3].getagility() and acrobatfail == False:
                special = int(input("Do you want to use your special? 1 = Yes, 2 = No"))

                if special == 1 and self.group[2].specialbool:
                    self.monsters[randommonster].sethealth(
                        self.monsters[randommonster].gethealth() - self.group[2].getspecial())
                    print("You hit", self.monsters[randommonster].getname())
                    sleep(0.5)
                    print(self.monsters[randommonster].getname(), "Health:", self.monsters[randommonster].gethealth())
                    self.checkmonsterdeath()
                    self.allmonsterdead()
                    sleep(1)
                    self.weapon.aufsteigen()
                    print(self.weapon.name, "makes", self.weapon.attack, "damage")
                    self.group[2].specialbool = False
                    self.weapon.setcondition(self.weapon.getcondition() - randint(1, 5))
                    self.weapon.zerbrechen()

                else:
                    self.monsters[wattack - 1].sethealth(
                        self.monsters[wattack - 1].gethealth() - self.group[2].getattack() + dmgdice)
                    print("You hit", self.monsters[wattack - 1].getname())
                    sleep(0.5)
                    print(self.monsters[wattack - 1].getname(), "Health:", self.monsters[wattack - 1].gethealth())
                    self.checkmonsterdeath()
                    self.allmonsterdead()
                    sleep(1)
                    self.weapon.aufsteigen()
                    print(self.weapon.name, "makes", self.weapon.attack, "damage")
                    self.group[2].specialbool = True
                    self.weapon.setcondition(self.weapon.getcondition() - randint(1, 5))
                    self.weapon.zerbrechen()

            else:
                acrobatfail = True
                print("How could you miss that punch?", self.group[0].getname())
                sleep(2)
                print("┐('～`;)┌")
                sleep(2)
                print("Really you got hit?(↼_↼)")
                print("You lose healthpoints")
                self.group[2].sethealth(self.group[2].gethealth() - 5)
                print(self.group[0].getname(), "current health:", self.group[2].gethealth())
                self.checkherodeath()
                self.allherodead()

            if self.monsters[3].getfight() >= self.group[3].getattack():
                self.group[3].sethealth(self.monsters[3].getdamage()+dmgdice)
                print(self.group[3].getname(), "Health:", self.group[3].gethealth())

            monsterdeadcheck = self.checkmonsterdeath()
            if monsterdeadcheck == True:
                done = True

    def checkmonsterdeath(self):
        done = False
        deathcounter = 0
        monsterxp = self.monster.health / 10

        for x in self.monsters:
            if x.gethealth() <= 0:

                self.setxp(self.getxp() + monsterxp)
                del x
                deathcounter += 1
            else:
                ret = False

        if deathcounter == 4:
            ret = True
            done = True
        return ret

    def allmonsterdead(self):
        done = False
        monsterdead = len(self.monsters)
        if monsterdead == 0:
            print("All monsters died")
            done = True

    def checkherodeath(self):
        herodead = 0

        for i in self.group:
            if i.gethealth() <= 0:
                herodead +=1
            if herodead == 4:
                print("All heroes died")
                exit()

    def allherodead(self):
        herodead = len(self.group)
        if herodead == 0:
            print("All heroes are dead")
            exit()












