
MiniNumber= lambda No1,No2: No1<No2

def main():
    No1= int(input("Enter first number: "))
    No2= int(input("Enter second number: "))

    Result= MiniNumber(No1,No2)
    if Result==True:
        print("The smaller number is: ", No1)
    else:
        print("The smaller number is: ", No2)

if __name__=="__main__":
    main()
