from Fahrzeug import Fahrzeug

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