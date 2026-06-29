def chkGreater(No1,No2):
    if No1>No2:
        print(No1,"is Greater")
    else:
        print(No2, "is Greater")

def main():

    Val1= int(input("Enter the first number"))
    Val2= int(input("Enter the second number"))

    chkGreater(Val1,Val2)

if __name__=="__main__":
    main()
    
