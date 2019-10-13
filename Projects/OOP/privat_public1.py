class Schiff:
    def __init__ (self):
        self.__geschwindigkeit = 0 #Knoten
        self.__besatzung = 0 #Anzahl an Personen
        self.__leange = 27 #inMeter
        self.__material = "Kunststoff"
        self.__farbe = "weiß"
        self.__richtung = 0 #0-359 Grad
    def groeße(self, leangeNeu):
        if leangeNeu <100 and leangeNeu >1:
            self.__leange = leangeNeu

    def beschleunigen(self, faster):
        if faster <100 and faster >1:
            self.__geschwindigkeit += faster
        elif faster > 100 or faster < 1:
            print("Zu langsam oder zu Schnell")


    def abbremsen(self):
        self.__geschwindigkeit -= 1.0

    def nachBackboard(self): # links
        self.__richtung -=10 #-10 Grad
        if self.__richtung < 0:
            self.__richtung = self.__richtung +360

    def nachSteuerboard(self): #rechts
        self.__richtung +=10 #+10
        if self.__richtung > 359: #Korrektur des Kurses
            self.__richtung = self.__richtung -360

    def showSchiff(self):
        return "Geschwindigkeit: {} \nRichtung: {} \nFarbe: {}".format(
            self.__geschwindigkeit, self.__richtung, self.__farbe)

    #Hauptprogramm
if __name__ == "__main__":
    print("Anfang")
    meinSchiff = Schiff()
    meinSchiff.__geschwindigkeit = 0
    print(meinSchiff.showSchiff())
    meinSchiff.nachBackboard()
    meinSchiff.beschleunigen(12)
    meinSchiff.beschleunigen(3)
    print(meinSchiff.showSchiff())



