class Schueler:
    #Anfangsclass Schueler:
    #!!!! statische Variable = Klassenvariable!!!
    __schulklasse = "---Keine---" #Name der Schulklasse, String, für alle gleich

    #Atribute und Methoden
    def __init__(self): #/#Konstruktor
        self.__name = "" #Nachname String
        self.__vorname ="" #Vorname String

    #Namen abrufen
    def getName(self):
        return (self.__name, self.__vorname)#Tupel!

    #Namen setzen
    def setName(self, nameNeu, vornameNeu):
        if nameNeu != "" and vornameNeu != "":
            self.__name = nameNeu
            self.__vorname = vornameNeu
    @staticmethod
    def setzeSchulklasse(schulklasseNeu):
        Schueler.__schulklasse = schulklasseNeu

    @staticmethod
    def begruessung():
        return  "Willkomen zur Schulklasse {}!".format(Schueler.__schulklasse)

    def zeigeSchuelerDaten(self):
        return """
            Schülerdaten:
            Name:{},{}
            Schule: {}""".format(
            self.__name, self.__vorname, Schueler.__schulklasse)

#Hauptprogramm
if __name__ == "__main__":

    #erstaml eine Begruessung!
    print( Schueler.begruessung())

    #Schulklasse schon festlegen, ohne Instanzen!
    Schueler.setzeSchulklasse("ITA17")

    #Instanzen von zwei Schuelern erstellen
    eins= Schueler()
    eins.setName("Elyas","Koné")
    zwei = Schueler()
    zwei.setName("Dennis","Mund")

    print(eins.zeigeSchuelerDaten())
    print(zwei.zeigeSchuelerDaten())

    #nochmals eine Begrüßung!
    print( Schueler.begruessung())

#Ende
