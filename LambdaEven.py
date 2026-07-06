
IsEven= lambda No: No%2==0

def main():
    No= int(input("Enter a number: "))
    Result= IsEven(No)

    if Result==True:
       print(f"Is {No} EVEN?: ",Result)
    else:
        print(f"Is {No} EVEN?: ",Result)

if __name__=="__main__":
    main()
