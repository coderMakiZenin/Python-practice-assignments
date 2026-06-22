def Multiplication(No1,No2):

    Ans=No1*No2

    return Ans

def main():

    Value1=int(input("Enter First Number"))
    Value2=int(input("Enter Second Number"))

    Ret= Multiplication(Value1,Value2)

    print("The Multiplication is:",Ret)
    
if __name__=="__main__":
    main()