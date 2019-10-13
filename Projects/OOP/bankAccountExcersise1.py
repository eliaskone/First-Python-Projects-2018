#OjeketOrientierung
class BankAccountOwnerClass:

    def __init__(self):
        self.__surname = ""
        self.__forename = ""
        self.__address = ""
        self.__job = ""
        self.__day_of_birth = ""
        self.test = ""
    def account_owner_def(self):
        done = False
        while not done:
            try:
                print("Create your own bank account: ")
                self.__surname = input("Surname:")
                self.__forename = input("Forename:")
                self.__address = input("Address:")
                self.__job = input("Job:")
                self.__day_of_birth = input("Day of birth:")
            except(ValueError):
                print("Value Error")
                print("Try again")
            except:
                print("Invalid input")
            print("Surname:", self.__surname, "\nForename:", self.__forename, "\nAddress:", self.__address, "\nJob:", self.__job, "\nDay of birth:", self.__day_of_birth, "\n")
            done = True
    def placeOfResidence(self):
        try:
            newlivingplace= input("Did you change your place of living?")
            if newlivingplace == "Yes" or newlivingplace == "yes" or newlivingplace == "Y".lower():
                self.__address = newlivingplace
            elif newlivingplace == "No" or newlivingplace == "no" or newlivingplace == "N".lower():
                pass #Go back to menue
        except:
            print("Invalid input")

    def jobdef(self):
        try:
            newjob = input("Did you change your job?")
            if newjob == "Yes" or newjob == "yes" or newjob == "Y".lower():
                self.__job = newjob
            elif newjob == "No" or newjob == "no" or newjob == "N".lower():
                pass #Go back to menue
        except:
            print("Invalid input")


class BankAccount(BankAccountOwnerClass):

    def __init__(self):
        self.__account_owner = BankAccountOwnerClass
        self.__account_number = 0
        self.__credit_limit = 0
        self.__account_balance = 0
        self.__authorized_owner = ""

    def kontodefs(self):
        self.__account_owner = BankAccountOwnerClass
        self.__account_number = 485188848485356
        self.__credit_limit = 0
        self.__account_balance = 3677
        self.__authorized_owner = "Mister Hai"

    def returnAccountInfo(self):
        return BankAccountOwnerClass.account_owner_def(self)

    def depositdef(self): #einzahlung
        done = False
        while not done:
            try:
                deposit = input("Do you want to make a despoit?")
                if deposit == "Yes" or deposit == "yes":
                    despoit_confirmation = int(input("How much money do you want to despoit?"))
                    self.__account_balance= self.__account_balance + despoit_confirmation
                    print("Account balance: ",self.__account_balance)
                elif deposit == "No" or deposit == "no":
                    done = True
            except(ValueError):
                print("Value Error")
            except:
                print("Invalid input")



    def payingoutdef(self): #auszahlung
        global done
        global done2
        done = False
        done2 = False
        while not done:
            try:
                payingout = input("Do you want to make a payout?")
                if payingout == "Yes" or payingout == "yes":
                    payout_confirmation = int(input("How much money do you want to payout"))
                    if self.__account_balance - payout_confirmation < 0:
                        print("You do not have enough money on your bank account!")
                        print(self.__account_balance)
                        continuee = input("Do you want to do something else?")
                        if continuee == "Yes" or continuee == "yes":
                            self.menue()
                        elif continuee == "No" or continuee == "no":
                            print("Have a good day")
                            exit()
                        else:
                            print("Invalid input")
                        #self.payout_something_else()
                    else:
                        self.__account_balance = self.__account_balance - payout_confirmation
                        print("Account balance: ",self.__account_balance)
                elif payingout == "No" or payingout == "no":
                    while not done2:
                        continuee = input("Do you want to do something else?")
                        if continuee == "Yes" or continuee == "yes":
                            self.menue()
                        elif continuee == "No" or continuee == "no":
                            print("Have a good day")
                            exit()
                        else:
                            print("Invalid input")
                        #self.payout_something_else()
                else:
                    print("Invalid Input")

            except(ValueError):
                print("Value Error")

            except:
                print("Invalid input")

    #def payout_something_else(self):
        continuee = input("Do you want to do something else?")
        if continuee == "Yes" or continuee == "yes":
            self.menue()
        elif continuee == "No" or continuee == "no":
            print("Have a good day")
            exit()
        else:
            print("Invalid input")
            print(done2)
            #done2 = False


    def transferdef(self): #überweisung
        try:
            transfer = input("Do you want to transfer money?")
            if transfer == "Yes" or transfer == "yes" or transfer == "Y".lower():
                transfer_which_account = int(input("Type in the bank account number of the other bank account owner."))
                while True:
                    ueberweisungbetaetigen = int(input("How much money do you want to payout?"))
                    if self.__account_balance - ueberweisungbetaetigen < 0:
                        print("You do not have enough money on your bank account!")
                        print(self.__account_balance)

                    else:
                        self.__account_balance = self.__account_balance - ueberweisungbetaetigen
                        break
        except:
            print("Invalid input")

    def standingOrderdef(self): #dauerauftrag
        try:
            standingorder = input("Do you want to make a standing order?")
            if standingorder == "Yes" or standingorder == "yes" or standingorder == "Y".lower() :
                standing_order_which_account = int(input("Type in the bank account number of the other bank account owner."))
                while True:
                    standing_order_which_account = int(input("How much money do you want to payout?"))
                    if self.__account_balance - standing_order_which_account < 0:
                        print("You do not have enough money on your bank account!")
                        print(self.__account_balance)

                    else:
                        self.__account_balance = self.__account_balance - standing_order_which_account
                        break
        except:
            print("Invalid input")

    def menue(self):
        select_menue = input("What do you want to do?"
                             "\nDespoit(1)\tPayout(2)"
                             "\nTransfer(3)\tStanding order(4)")
        if select_menue == "1" or select_menue == "Despoit" or select_menue == "despoit":
            self.depositdef()
            done = False
            while not done:
                continuee = input("Do you want to do something else?")
                if continuee == "Yes" or continuee == "yes": #or "Y".lower():
                    #print("test")
                    #done = True
                    self.menue()

                elif continuee == "No" or continuee == "no":# or "N".lower():
                    print("Have a good day")
                    #done = True
                    exit()

                else:
                    print("Invalid input")


        elif select_menue == "2" or select_menue == "Payout" or select_menue == "payout":
            self.payingoutdef()

        elif select_menue == "3" or select_menue == "Transfer" or select_menue == "transfer":
            self.transferdef()
        elif select_menue == "4" or select_menue == "Standing order" or select_menue == "standing order":
            self.standingOrderdef()

        elif select_menue == "5" or select_menue == "show account balance" or select_menue == "Show account balance":
            pass#method that showes account balance

        elif select_menue == "6" or select_menue == "show account owner settings" or select_menue == "Show account owner settings":
            pass#method that showes account owner settings

        elif select_menue == "7" or select_menue == " change account owner settings" or select_menue == " change account owner settings":
            pass#method that changes account owner settings


my_account_owner = BankAccountOwnerClass()
myAccount = BankAccount()

#print(myAccount.returnAccountInfo())
#print(myAccount.depositdef())
#print(my_account_owner.account_owner_def()) #before menue create account
print(myAccount.menue())
#print(myAccount.returnAccountInfo())
#nochnichtvollendet
