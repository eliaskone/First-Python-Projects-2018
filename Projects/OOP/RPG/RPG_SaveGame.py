def saveGame(gf):
    gf = str(gf) + "\n"
    with open("gamesave.txt", "a") as file:
        file.write(gf)

def readGame():
    dic = []
    with open("gamesave.txt", "r") as file:
        for x in file.readlines():
            dic.append(x)
    return dic
