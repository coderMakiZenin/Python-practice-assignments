
IsSquare= lambda No: (No*No)

def main():
    No= int(input("Enter a number: "))
    Result= IsSquare(No)
    print("The Square is: ", Result)

if __name__=="__main__":
    main()
