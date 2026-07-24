def ChkNum(x):
    if (x%2==0):
        print("The number is even")
    else:
        print("The number is odd")

def main():
    no= int(input("Enter any number: "))
    ChkNum(no)
if __name__=='__main__':
    main()