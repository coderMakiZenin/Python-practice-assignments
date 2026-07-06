
Multiplication= lambda No1,No2: No1*No2

def main():
    No1= int(input("Enter first number: "))
    No2= int(input("Enter second number: "))

    Result= Multiplication(No1,No2)
    print(f"The multiplication of {No1} and {No2} is: ", Result)

if __name__=="__main__":
    main()
