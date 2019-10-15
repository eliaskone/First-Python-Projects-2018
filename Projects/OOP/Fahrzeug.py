class Fahrzeug:
    __hersteller = ""

    def __init__(self):
        self._leistung = 0
        self._geschwindigkeit = 0.0
        self._richtung = 180
        self._farbe = ""
        self._anzahlTueren = 0
        self._bezeichnung = ""

    def beschleunigung(self):
        self._geschwindigkeit += 4

    def bremsen(self):
        self._geschwindigkeit -= 4

    def lenkenLinks(self):
        self._richtung = -20

    def lenkenRinks(self):
        self._richtung = 20

    def getRichtung(self):
        return self._richtung

    def getGeschwindigkeit(self):
        return self._geschwindigkeit

    @staticmethod
    def getHersteller():
        return Fahrzeug.__hersteller

    @staticmethod
    def setNewHersteller(new):
        Fahrzeug.__hersteller = new

class PKW(Fahrzeug):

    def __init__(self):
        Fahrzeug.__init__(self)
        self.anzahlPersonen += 1
        self.kofferraumVolumen = 0.0

    def beschleunigung(self):
        self._geschwindigkeit += 6

    def bremsen(self):
        self._geschwindigkeit -= 6

    def lenkenLinks(self):
        self._richtung += 30

    def lenkenRechts(self):
        self._richtung += 30

class LKW(Fahrzeug):

    def __init__(self):
        Fahrzeug.__init__(self)
        self._anzahlAnhaenger = 0
        self._ladeVolumen = 0.0

    def beschleunigung(self):
        self._geschwindigkeit += 4

    def bremsen(self):
        self._geschwindigkeit -= 4

    def lenkenLinks(self):
        self._richtung += 10

    def lenkenRechts(self):
        self._richtung += 10

if __name__ == "__main__":
    Fahrzeug1 = PKW()
    Fahrzeug1.lenkenRechts()
