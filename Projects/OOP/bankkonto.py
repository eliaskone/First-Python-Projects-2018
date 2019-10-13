class Bankkonto:
    def __init__(self):
        self._auszahlen = True
        self._ueberzeihungskredit = False
        self._vorname = "Elyas"
        self.__nachname = "Koné"
        self.__kontonumer = 473628383477447
        self.__kontostand = 4927.50


    def informationen(self):
        self._vorname = "Elyas"
        self.__nachname = "Koné"
        self.__kontonumer = 473628383477447
        self.__kontostand = 4927.50

    def aktionen(self):
        try:
            self.__einzahlen = float(input("Wie viel Geld wollen sie eizahlen")), self.__kontostand - self.__einzahlen
            self._auszahlen = float(input("Wie viel Geld wollen sie auzahlen"))
            if self.__kontostand == 0 and self._ueberzeihungskredit == False:
                self._auszahlen = False
            else:
                self.__auzahlen = True
                self.__kontostand - self._auszahlen


        except:
            print("Falsche Eingabe")


class Girokonto(Bankkonto):

    def __init__(self):
        Bankkonto.__init__(self)
        self.__ueberzeihungskredit = True

    def besondersGiro(self):
        self.__BLZGiro = 3748989
        self.__ueberweisung = float(input("Wie viel Geld wollen sie Überweisen?")), self.__ueberweisung - self.__einzahlen
        self.__IBANGiro = self.__BLZGiro + self.__kontonummer

class Sparbuchkonto(Bankkonto):

    def __init__(self):
        self.__ueberzeihungskredit = False

    def besondersSpar(self):
        self.__BLZSpar = 36363748
        self.__IBANSpar = self.__BLZSpar + self.__kontonummer
        self.__zinsberechung = 0
        self.__zinssatz = 0

class Kreditkartenkonto(Bankkonto):

    def __init__(self):
        self.__ueberzeihungskredit = False

    def besondersKredit(self):
        self.__kreditlimit = 0.0

#Hauptprogramm
if __name__ == "__main__":

    Giro = Girokonto()
    Giro._vorname
    print(Giro._vorname)






