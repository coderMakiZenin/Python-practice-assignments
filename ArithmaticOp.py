def ArithmaticOp(No1,No2):
    a= No1+No2
    s= No1-No2
    m= No1*No2
    d= No1/No2

    return a,s,m,d


def main():
    Val1=int(input("Enter a first number"))
    Val2=int(input("Enter a second number"))

    a,s,m,d= ArithmaticOp(Val1,Val2)

    print("The addition is:",a)
    print("The substraction is:",s)
    print("The multiplication is:",m)
    print("The division is:",d)

if __name__=="__main__":
    main()