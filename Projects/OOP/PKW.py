from Fahrzeug import Fahrzeug


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