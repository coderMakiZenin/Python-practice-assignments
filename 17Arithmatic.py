def Add(a,b):
    return a+b

def Sub(a,b):
    return a-b

def Div(a,b):
    return a/b

def Multi(a,b):
    return a*b

def main ():
    x= int(input("Enter the first number:  "))
    y= int(input("Enter the second number:  "))

    A=Add(x,y)
    print(" The Addition is: ",A)

    S=Sub(x,y)
    print(" The Substraction is: ",S)

    M=Multi(x,y)
    print(" The Multiplication is: ",M)
    
    D=Div(x,y)
    print(" The Division is: ",D)

if __name__=='__main__':
    main()