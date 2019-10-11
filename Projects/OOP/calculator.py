class Calculator:

    def __init__(self):
        self.num1 = 0.0
        self.num2 = 0.0
        self.result = 0.0
        self.bolean = True
        self.signCount = 0

    def add(self):
        self.result = self.num1 + self.num2

    def sub(self):
        self.result = self.num1 - self.num2

    def mult(self):
        self.result = self.num1 * self.num2

    def div(self):
        self.result = self.num1 / self.num2

    def setNum1(self):
        self.num1 = float(input("Number1: "))

    def setNum2(self):
        self.num2 = float(input("Number2: "))

    def calc(self):
        self.bolean = True
        while self.bolean:
            try:
                self.setNum1()
                self.setNum2()
                if self.signCount == 1:
                    self.add()

                elif self.signCount == 2:
                    self.sub()

                elif self.signCount == 3:
                    self.mult()

                elif self.signCount == 4:
                    self.div()

                print("Result: ",self.result)
                self.bolean = False
                return self.menu()

            except(ValueError):
                print("Value error")

    def menu(self):
        self.bolean = True
        while self.bolean:
            try:
                chose = int(input("Functions:\n"+
                "1)add\t2)substract\n3)multiply\t4)divide\n5)exit"))

                if chose >0 and chose < 5:
                    self.signCount = chose
                    return self.calc()

                elif chose == 5:
                    exit("Good Bye")

                else:
                    print("Invalid input")

            except(ValueError):
                print("Value Error")

myCalc = Calculator()
myCalc.menu()
