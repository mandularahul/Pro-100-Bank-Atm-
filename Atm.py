class ATM:
    def __init__ (self,Card,Pin,Name):
        self.Card = Card
        self.Pin = Pin
        self.Name = Name

    def CheckBalance(self):
        print("Your Bank balance is 500000")

    def Withdrawl(self,amount):
        Savings = 500000
        New_Amount = Savings - amount
        if New_Amount < Savings :
            print("You have withdrawn "+ str(amount) +" and your balance on account " + str(New_Amount))


def main():
    print("Hello, Welcome to Developer's Bank!!!")

    cardNum = int(input("Please enter the card number Sir/Madam (only 16 digits) : "))
    pinNum = int(input("Please enter the pin number Sir/Madam (only 4 digits) : "))
    name = input("Please enter your good name Sir/Madam (only alphabetical characters) : ")

    newUser = ATM(cardNum, pinNum, name)

    print("Hello Our Dear customer "+ str(name) +", Sir/Madam What do you want to do?")
    print("1 = Balance and 2 = Withdrawl")
    activity = input("Enter the activity no : ")

    if activity == "1" :
        newUser.CheckBalance()

    elif activity == "2" :
        amount = int(input("What is the amount of Withdrawl Sir/Madam? : "))
        newUser.Withdrawl(amount)
    
    else :
        print("Oops!! Wrong number Sir/Madam")

if __name__ == "__main__":
    main()