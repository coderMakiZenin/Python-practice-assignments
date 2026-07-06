
MaxNumber= lambda No1,No2: No1>No2

def main():
    No1= int(input("Enter first number: "))
    No2= int(input("Enter second number: "))

    Result= MaxNumber(No1,No2)
    if Result==True:
        print("The bigger number is: ", No1)
    else:
        print("The bigger number is: ", No2)

if __name__=="__main__":
    main()
