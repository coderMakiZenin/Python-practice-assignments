
IsDivisible= lambda No: No%5==0

def main():
    No= int(input("Enter a number: "))
    Result= IsDivisible(No)

    if Result==True:
       print(f"Is {No} divisible by 5: ", True)
    else:
        print(f"Is {No} divisible by 5: ", False)
if __name__=="__main__":
    main()
