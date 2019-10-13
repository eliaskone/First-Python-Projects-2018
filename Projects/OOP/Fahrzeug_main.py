from Fahrzeug import Fahrzeug
from PKW import PKW
from LKW import LKW

if __name__ == "__main__":
    fahrzeug1 = PKW()
    fahrzeug1.beschleunigung()
    fahrzeug1.beschleunigung()
    print("Geschwindigkeit", fahrzeug1.getGeschwindigkeit(), "kmh", "\n")
    fahrzeug1.bremsen()
    print("Geschwindigkeit", fahrzeug1.getGeschwindigkeit(), "kmh", "\n")
    fahrzeug1.lenkenLinks()
    print("Richtung", fahrzeug1.getRichtung())
    fahrzeug1.lenkenRechts()
    fahrzeug1.lenkenRechts()
    print("Richtung", fahrzeug1.getRichtung())
    print("Hersteller", Fahrzeug.getHersteller())

    fahrzeug2 = LKW()
    fahrzeug2.beschleunigung()
    fahrzeug2.beschleunigung()
    print("Geschwindigkeit", fahrzeug2.getGeschwindigkeit(), "kmh", "\n")
    fahrzeug2.bremsen()
    print("Geschwindigkeit", fahrzeug2.getGeschwindigkeit(), "kmh", "\n")
    fahrzeug2.lenkenLinks()
    print("Richtung", fahrzeug2.getRichtung())
    fahrzeug2.lenkenRechts()
    fahrzeug2.lenkenRechts()
    print("Richtung", fahrzeug2.getRichtung())
    print("Hersteller", Fahrzeug.getHersteller())
