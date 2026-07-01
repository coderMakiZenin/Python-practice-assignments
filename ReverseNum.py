def ReverseNum(No):
    x=0
    i=0
    while No!=0:
        i=No%10
        x=x*10+i
        No=No//10
    return x

def main():

    Value= int(input("Enter the number: "))
    Reverse= ReverseNum(Value)
    print("The reverse of the number is:", Reverse)

if __name__=="__main__":
    main()