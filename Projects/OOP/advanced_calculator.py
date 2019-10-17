class calculator: #Klasse "calculator"(Taschenrechner)


    def resistancecalculator(self): #Berechnung von einem elektrischen Widerstand
        try:
            print("Berechnung des Widerstandes")
            self.voltage_ur = float(input("Spannung U in V>""Spannung U in V>"))
            self.electricity_ir = float(input("Stromstärke I in A>"))
            self.ergebnisA = self.voltage_ur / self.electricity_ir
            print("Ergebnis: R =", self.ergebnisA," Ohm")
        except:
            print("falsche eingabe")


    def conductance(self): #Leitwert berechnung
        try:
            print("Berechnung des Leitwerts")
            self.electricity_iG = float(input("Stromstärke I in A>"))
            self.voltage_uG = float(input("Spannung U in V>"))
            self.__ergebnisB = self.electricity_iG / self.voltage_uG
            print("Ergebnis: G=", self.__ergebnisB,"S")

        except:
            print("falsche Eingabe")


    def resistanceSeriesConnection(self): #Widerstands berechnung in einer Serien-(Reihenschaltung)
        try:
            print("Berechnung der Widerstände in einer Serienschaltung")
            self.resistance1_rS = float(input("Widerstand1 R in Ohm:"))
            self.resistance2_rS = float(input("Widerstand2 R in Ohm:"))
            self.ergebnisC = self.resistance1_rS + self.resistance2_rS
            print("Ergebnis: Rges=", self.ergebnisC, "Ohm")
        except:
            print("falsche Eingabe")


    def resistanceParallelConnection(self): #Widerstands berechnung Parallelschaltung
        try:
            print("Berechnung der Widerstände in einer Parallelschaltung")
            self.resistance1_rP = float(input("Widerstand1 R in Ohm:"))
            self.resistance2_rP = float(input("Widerstand2 R in Ohm:"))
            self.ergebnisD = self.resistance1_rP *self.resistance2_rP / (self.resistance1_rP + self.resistance2_rP)
            print("Ergebnis: Rges=", self.ergebnisD,"Ohm")

        except:
            print("falsche Eingabe")


    def frequenzcalculator(self): #Berechnung der Frequenz
        try:
            print("Berechnung der Frequenz f:")

            while True:
                self.period_T = float(input("Periodendauer T in s>0 "))

                if self.period_T <= 0:
                    continue

                else:
                    self.ergebnisE =  1 / self.period_T
                    print("Ergebnis:f=",self.ergebnisE, "Hz")
                    break

        except ValueError:
            print("falsche Eingabe")

        except:
            print("falsche Eingabe")


    def periodcalculator(self): #Berechnung der Periodendauer
        try:
            print("Berechnung der Periodendauer T:")

            while True:
                self.frequenz_f = float(input("Frequenz f in Hz>0 "))

                if self.frequenz_f <= 0:
                    continue

                else:
                    self.ergebnisF = 1 / self.frequenz_f
                    print("Ergebnis:T=", self.ergebnisF, "s")
                    break

        except ValueError:
            print("falsche Eingabe")

        except:
            print("falsche Eingabe")


    def close(self): #Programm beendung
        self.quite= "Ihre Eingabe>Q"
        print(self.quite)
        self.quiti= "--- Auf Wiedersehen-Ende ---"
        print(self.quiti)
        quit()


    def showmenu(self): #menü für den Zugriff
        calculatortxt = open("calculator.txt", "a")
        try:
            self.menue = str(input(
                "---E-Technik-Taschenrechner---\nMenü: Sie können berechnung:\nA) Widerstand R aus U und I""\nB) Leitwert G aus I und U \nC) Gesamntwiderstand einer Serienschaltung"
                "\nD) Gesamtwiderstand einer Parallelschaltung \nE) Frequenz aus der Periodendauer T"
                "\nF) Periodauer T aus der Frequenz f \nQ) beenden  "))
            if self.menue == "A" or self.menue == "a":
                self.resistancecalculator()
                calculatortxt.write("Berechnung des Widerstandes: "+"\n"+"Spannung U in V> "+
                                    str(self.voltage_ur)+"\n"+"Stromstärke I in A> "+
                                    str(self.electricity_ir)+"\n"+"Ergebnis: R = "+
                                    str(self.ergebnisA)+" Ohm"+"\n")

            if self.menue == "B" or self.menue == "b":
                self.conductance()
                calculatortxt.write("Berechnung des Leitwerts "+"\n""Stromstärke I in A>"+
                                    str(self.electricity_iG)+"\n"+"Spannung U in V>"+
                                    str(self.voltage_uG)+"\n"+"Ergebnis: G="+
                                    str(self.__ergebnisB)+"S")

            if self.menue == "C" or self.menue == "c":
                self.resistanceSeriesConnection()
                calculatortxt.write("Berechnung der Widerstände in einer Serienschaltung"+"\n"+"Widerstand1 R in Ohm:"+
                                    str(self.resistance1_rS)+"\n"+"Widerstand2 R in Ohm:"+
                                    str(self.resistance2_rS)+"\n"+"Ergebnis: Rges="+
                                    str(self.ergebnisC)+" Ohm")

            if self.menue == "D" or self.menue == "d":
                self.resistanceParallelConnection()
                calculatortxt.write("Berechnung der Widerstände in einer Parallelschaltung"+"\n"+"Widerstand1 R in Ohm:"+
                                    str(self.resistance1_rP)+"\n"+"Widerstand2 R in Ohm:"+
                                    str(self.resistance2_rP)+"\n"+"Ergebnis: Rges="+
                                    str(self.ergebnisD)+" Ohm")


            if self.menue == "E" or self.menue == "e":
                self.frequenzcalculator()  
                calculatortxt.write("Berechnung der Frequenz f:"+"\n"+"Periodendauer T in s>0 "+
                                    str(self.period_T)+"\n"+"Ergebnis: f="+
                                    str(self.ergebnisE)+ "Hz")

            if self.menue == "F" or self.menue == "f":
                self.periodcalculator()
                calculatortxt.write("Berechnung der Periodendauer T:"+"\n"+"Frequenz f in Hz>0 "+
                                    str(self.frequenz_f)+"\n"+"Ergebnis: T="+
                                    str(self.ergebnisF)+ "s")


            if self.menue == "Q" or self.menue == "q":
                self.close()
                calculatortxt.write(self.quite+"\n"+self.quiti)

        except ValueError:
            print("falsche Eingabe")


#Hauptprogramm
mycalculator = calculator()
print(mycalculator.showmenu())
