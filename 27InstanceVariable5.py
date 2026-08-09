class BankAccount:
    ROI=10.5 #(Rate of Interest)

    def __init__(self,Name,Amount):
        self.Name=Name
        self.Amount=Amount

    def Deposit(self):

        AddAmount=int(input(" Enter the amount you wanna add to the balance: "))
        self.Amount=self.Amount+AddAmount

        return self.Amount

    def AmtWithdrawn(self):

        Withdraw=int(input(" Enter the amount you want to withdraw:  "))

        if self.Amount>=Withdraw:
            self.Amount=self.Amount-Withdraw
            print("The amount withdrawn is:  ",Withdraw)
            return self.Amount  
        else:
            print(" You don't have sufficient balance in your bank account!")

    def CalculateInterest(self):

        Interest=(self.Amount* BankAccount.ROI)/100
        return Interest
    
    def Display(self):

        print(f"Account holder: {self.Name} \n Balance Amount: {self.Amount}")


def main():
    Obj1=BankAccount("Pissed off Gremlin",40000)
    
    print(" The amount deposited is:  ", Obj1.Deposit())
    print("The amount after withdrawl is:  ", Obj1.AmtWithdrawn())
    print("The rate of interest calculated is:  ",Obj1.CalculateInterest())
    Obj1.Display()

    Obj2=BankAccount("Ambitious Gremlin", 50000)
    
    print(" The amount deposited is:  ",Obj2.Deposit())
    print("The amount after withdrawl is:  ",Obj2.AmtWithdrawn())
    print("The rate of interest calculated is:  ",Obj2.CalculateInterest())
    Obj2.Display()

if __name__=="__main__":
    main()
