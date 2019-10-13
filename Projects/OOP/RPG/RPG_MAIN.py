from random import randint
from RPG_Hero import Hero
from RPG_Herogroup import HeroGroup
from time import sleep
import RPG_Monster
from RPG_Knight import Knight
from RPG_Archer import Archer
from RPG_Acrobat import Acrobat
from RPG_Thief import Thief

if __name__ == '__main__':
    boolean = False
    group = HeroGroup()

    print("Welcome")
    print("(￣▽￣)ノ")


    hero1 = Knight()
    name1 = input("Please put in a name for your Knight:")
    hero1.setname(name1)
    group.group.append(hero1)

    hero2 = Archer()
    name2 = input("Please put in a name for your Archer:")
    hero2.setname(name2)
    group.group.append(hero2)

    hero3 = Thief()
    name3 = input("Please put in a name for your Thief:")
    hero3.setname(name3)
    group.group.append(hero3)

    hero4 = Acrobat()
    name4 = input("Please put in a name for your Acrobat:")
    hero4.setname(name4)
    group.group.append(hero4)
    #menü
    dones = False
    while not dones:
        menue = int(input("Start Game[1] \nExit[2]\nLoad[3]"))

        if menue == 1:

            gameover = False
            while not gameover:
                aliveplayer = []
                try:
                    for i in range(0, len(group.group)-1):
                        if group.group[i].health >= 0:
                            aliveplayer.append(group.group[i])
                except ValueError:
                    if group.group[0].health >= 0:
                        aliveplayer.append(group.group[0])
                    else:
                        print("You died")
                        sleep(1)
                        print("¯\_(ツ)_/¯")
                        sleep(3)
                        gameover = True

                check = 0
                for i in Hero.Heroes:
                    if i.gethealth() <= 0:
                        check+=1
                if check == 4:
                    print("You died")
                    sleep(1)
                    print("¯\_(ツ)_/¯")
                    sleep(3)
                    gameover = True


                pickcharacter = randint(0, len(aliveplayer)-1)
                pickactivity = randint(1, 4)
                if not gameover:
                    if pickactivity == 1:
                        group.angreifen()
                        sleep(4)
                        print("\n\n\n")
                        print("Don´t worry")
                        sleep(0.5)
                        print("The game isn´t over yet")
                        print("(=^･ω･^=)")
                        sleep(0.5)
                        print("Your next adventure is starting")
                        print("(^_~)")
                        sleep(2)
                        menue2 = int(input("Event[1]\nRast[2]\nSave[3]\nEnd Game[4]"))
                        if menue2 == 4:
                            print("Thanks for playing")

                        if menue2 == 3:
                            print("Save game")
                            with open("Hero.txt", "a") as x:
                                for i in group.group:
                                    x.write(str(i.name)+"\n")
                                    x.write(str(i.health) + "\n")
                                    x.write(str(i.attack) + "\n")
                                    x.write(str(i.intelligence) + "\n")
                                    x.write(str(i.prestidigitation) + "\n")
                                    x.write(str(i.agility) + "\n")
                                    x.write(str(i.weapon.name) + "\n")
                                    x.write(str(i.weapon.attack) + "\n")
                                    x.write(str(i.weapon.list) + "\n")
                                    x.write(str(i.weapon.condition) + "\n")
                                    x.write(str(i.dmgcollection) + "\n")
                                    x.write(str(i.bodystrengh) + "\n")
                                    x.write(str(i.intuition) + "\n")
                                    x.write(str(i.charisma) + "\n")
                                    x.write(str(i.special) + "\n")
                                    x.write(str(i.specialbool) + "\n")
                                    x.write(str(i.name) + "\n")
                                    x.write(str(group.group))
                                    x.write(str(group.name))
                                    x.write(str(group.xp))
                                    x.write(str(group.weapon))
                                    x.write(str(group.monster))
                                    x.close()
                            sleep(3)
                            print("Your game is saved")
                            quit()

                        if menue2 == 2:
                            group.rest()

                        group.aufsteigen()
                        group.used = False

                    elif pickactivity == 2:
                        boolean = aliveplayer[pickcharacter].taschendiebstahl()
                        sleep(4)
                        print("\n\n\n")
                        print("Don´t worry")
                        sleep(0.5)
                        print("The game isn´t over yet")
                        print("(=^･ω･^=)")
                        sleep(0.5)
                        print("Your next adventure is starting")
                        print("(^_~)")
                        sleep(2)
                        menue2 = int(input("Event[1]\nRast[2]\nSave[3]\nEnd Game[4]"))
                        if menue2 == 4:
                            print("Thanks for playing")

                        if menue2 == 3:
                            print("Save game")
                            with open("Hero.txt", "a") as x:
                                for i in group.group:
                                    x.write(str(i.name)+"\n")
                                    x.write(str(i.health) + "\n")
                                    x.write(str(i.attack) + "\n")
                                    x.write(str(i.intelligence) + "\n")
                                    x.write(str(i.prestidigitation) + "\n")
                                    x.write(str(i.agility) + "\n")
                                    x.write(str(i.weapon.name) + "\n")
                                    x.write(str(i.weapon.attack) + "\n")
                                    x.write(str(i.weapon.list) + "\n")
                                    x.write(str(i.weapon.condition) + "\n")
                                    x.write(str(i.dmgcollection) + "\n")
                                    x.write(str(i.bodystrengh) + "\n")
                                    x.write(str(i.intuition) + "\n")
                                    x.write(str(i.charisma) + "\n")
                                    x.write(str(i.special) + "\n")
                                    x.write(str(i.specialbool) + "\n")
                                    x.write(str(i.name) + "\n")
                                    x.write(str(group.group))
                                    x.write(str(group.name))
                                    x.write(str(group.xp))
                                    x.write(str(group.weapon))
                                    x.write(str(group.monster))
                                    x.close()

                            sleep(3)
                            print("Your game is saved")
                            quit()

                        if menue2 == 2:
                            group.rest()

                        group.aufsteigen()
                        group.used = False

                    elif pickactivity == 3:
                        boolean = aliveplayer[pickcharacter].raetseln()
                        sleep(4)
                        print("\n\n\n")
                        print("Don´t worry")
                        sleep(0.5)
                        print("The game isn´t over yet")
                        print("(=^･ω･^=)")
                        sleep(0.5)
                        print("Your next adventure is starting")
                        print("(^_~)")
                        sleep(2)
                        menue2 = int(input("Event[1]\nRast[2]\nSave[3]\nEnd Game[4]"))
                        if menue2 == 4:
                            print("Thanks for playing")

                        if menue2 == 3:
                            print("Save game")
                            sleep(3)
                            print("Your game is saved")
                            quit()

                        if menue2 == 2:
                            group.rest()
                        group.aufsteigen()
                        group.used = False

                    elif pickactivity == 4:
                        boolean = aliveplayer[pickcharacter].balancieren()
                        sleep(4)
                        print("\n\n\n")
                        print("Don´t worry")
                        sleep(0.5)
                        print("The game isn´t over yet")
                        print("(=^･ω･^=)")
                        sleep(0.5)
                        print("Your next adventure is starting")
                        print("(^_~)")
                        sleep(2)
                        menue2 = int(input("Event[1]\nRast[2]\nSave[3]\nEnd Game[4]"))
                        if menue2 == 4:
                            print("Thanks for playing")

                        if menue2 == 3:
                            print("Save game")
                            sleep(3)
                            print("Your game is saved")
                            quit()

                        if menue2 == 2:
                            group.rest()

                        group.aufsteigen()
                        group.used = False

                    if boolean is True:
                        if pickactivity == 2:
                            print(f"You receive {hero1.gettaschendiebstahlwin()}")
                            group.setxp(group.getxp()+group.group[pickcharacter].gettaschendiebstahlwin())
                        elif pickactivity == 3:
                            print(f"You receive {hero1.getraetselnwin()}")
                            group.setxp(group.getxp()+group.group[pickcharacter].getraetselnwin())
                        elif pickactivity == 4:
                            print(f"You receive {hero1.getbalancierenwin()}")
                            group.setxp(group.getxp()+group.group[pickcharacter].getbalancierenwin())

                    if boolean is False:
                        if pickactivity == 4:
                            group.group[pickcharacter].sethealth(group.group[pickcharacter].gethealth()-10)

            if menue == 2:
                print("Thanks for playing")
                exit()

            if menue == 3:
                with open("Hero.txt","r") as y:
                    loading = []
                    for xx in y.readlines():
                        loading.append(str(xx))


                hero1.name(loading[0])
                hero1.health(loading[1])
                hero1.attack(loading[2])
                hero1.intelligence(loading[3])
                hero1.prestidigitation(loading[4])
                hero1.agility(loading[5])
                hero1.weapon.name(loading[6])
                hero1.weapon.attack(loading[7])
                hero1.weapon.list(loading[8])
                hero1.weapon.condition(loading[9])
                hero1.dmgcollection(loading[10])
                hero1.bodystrengh(loading[11])
                hero1.intuition(loading[12])
                hero1.charisma(loading[13])
                hero1.special(loading[14])
                hero1.specialbool(loading[15])
                hero1.name(loading[16])

                hero2.name(loading[17])
                hero2.health(loading[18])
                hero2.attack(loading[19])
                hero2.intelligence(loading[20])
                hero2.prestidigitation(loading[21])
                hero2.agility(loading[22])
                hero2.weapon.name(loading[23])
                hero2.weapon.attack(loading[24])
                hero2.weapon.list(loading[25])
                hero2.weapon.condition(loading[26])
                hero2.dmgcollection(loading[27])
                hero2.bodystrengh(loading[28])
                hero2.intuition(loading[29])
                hero2.charisma(loading[30])
                hero2.special(loading[31])
                hero2.specialbool(loading[32])
                hero2.name(loading[33])

                hero3.name(loading[34])
                hero3.health(loading[35])
                hero3.attack(loading[36])
                hero3.intelligence(loading[37])
                hero3.prestidigitation(loading[38])
                hero3.agility(loading[39])
                hero3.weapon.name(loading[40])
                hero3.weapon.attack(loading[41])
                hero3.weapon.list(loading[42])
                hero3.weapon.condition(loading[43])
                hero3.dmgcollection(loading[44])
                hero3.bodystrengh(loading[45])
                hero3.intuition(loading[46])
                hero3.charisma(loading[47])
                hero3.special(loading[48])
                hero3.specialbool(loading[49])
                hero3.name(loading[50])

                hero4.name(loading[51])
                hero4.health(loading[52])
                hero4.attack(loading[53])
                hero4.intelligence(loading[54])
                hero4.prestidigitation(loading[55])
                hero4.agility(loading[56])
                hero4.weapon.name(loading[57])
                hero4.weapon.attack(loading[58])
                hero4.weapon.list(loading[59])
                hero4.weapon.condition(loading[60])
                hero4.dmgcollection(loading[61])
                hero4.bodystrengh(loading[62])
                hero4.intuition(loading[63])
                hero4.charisma(loading[64])
                hero4.special(loading[65])
                hero4.specialbool(loading[66])
                hero4.name(loading[67])

                group.group(loading[68])
                group.name(loading[69])
                group.xp(loading[70])
                group.weapon(loading[71])

        print("Game is loading")
        sleep(2)
        print("Game is loaded, press 1 to continue")
        continue


"""
x.write(str(x.group.group))
                        x.write(str(x.name))
                        x.write(str(x.xp))
                        x.write(str(x.weapon))
                        x.write(str(x.monster))"""


