
ChkLargest= lambda No1,No2,No3:No1 if No1>No2 and No1>No3 else No2 if No2>No1 and No2>No3 else No3

def main():
    No1= int(input("Enter first number: "))
    No2= int(input("Enter second number: "))
    No3= int(input("Enter third number: "))

    Result= ChkLargest(No1,No2,No3)
    print(f"Amongst {No1},{No2} and {No3} the largest is: ", Result)

if __name__=="__main__":
    main()
