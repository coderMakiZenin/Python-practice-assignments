def Show(x):
    if x>0:
        print("It is a positive number")
    elif x<0:
        print("It is a negative number")
    else:
        print("The number is zero")

def main ():
    x=int(input("Enter a number: "))
    Show(x)

if __name__=='__main__':
    main()