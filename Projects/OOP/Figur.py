class Figur:

    def __init__(self):
        self.__laenge = 0.0
        self.__breite = 0.0
        self.__farbe = ""

    def getLaenge(self):
        return self.__laenge

    def getBreite(self):
        return self.__breite

    def getFarbe(self):
        return self.__farbe

    def zeichnen(self):
        print("Zeichne Figur")

    def berechneFlaeche(self):
        return self.__laenge * self.__breite