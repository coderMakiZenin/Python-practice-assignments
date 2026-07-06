
IsOdd= lambda No: No%2==0

def main():
    No= int(input("Enter a number: "))
    Result= IsOdd(No)

    if Result==False:
       print(f"Is {No} ODD?: ", True)
    else:
        print(f"Is {No} Odd?: ", False)

if __name__=="__main__":
    main()
