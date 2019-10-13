from Figur import Figur
from math import pi

class Kreis(Figur):

    def __init__(self):
        Figur.__init__(self)
        self.__radius = 0.0

    def getRadius(self):
        return self.__radius

    def zeichnen(self):
        print("Zeichne Kreis")

    def berechneFlaeche(self):
        return pi * self.__radius
        self.__radius