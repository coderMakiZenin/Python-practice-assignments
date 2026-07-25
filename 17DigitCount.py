def DigitCount(No):
    x=0
    while No!=0:
        No=No//10
        x=x+1
    return x

def main():

    Value= int(input("Enter the number: "))
    Digits= DigitCount(Value)
    print("The number of digits are:", Digits)

if __name__=="__main__":
    main()