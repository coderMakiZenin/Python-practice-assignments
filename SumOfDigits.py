def SumOfDigit(No):
    x=0
    while No!=0:
        i=No%10
        No=No//10
        x=x+i
    return x

def main():

    Value= int(input("Enter the number: "))
    Sum= SumOfDigit(Value)
    print("The sum of digits is:", Sum)

if __name__=="__main__":
    main()