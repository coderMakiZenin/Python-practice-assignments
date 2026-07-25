def DigitAdd(No):
    i=0
    while No!=0:
        x=No%10
        i=i+x
        No=No//10
        
    return i

def main():

    Value= int(input("Enter the number: "))
    Digits= DigitAdd(Value)
    print("The addition of digits are:", Digits)

if __name__=="__main__":
    main()