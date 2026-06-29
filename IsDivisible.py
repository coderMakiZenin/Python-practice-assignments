def IsDivisible(No):
    if No%5 and No%3==0:
        return True
    else:
        return False


def main():

    Val= int(input("Enter the number"))

    result= IsDivisible(Val)
    if result==True:
        print("The number is divisible by 3 and 5")
    else:
        print("The number is not divisble by 3 and 5")

if __name__=="__main__":
    main()
    