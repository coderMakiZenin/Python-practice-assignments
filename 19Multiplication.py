Power=lambda x,y: x*y

def main():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    Result=Power(x,y)
    print("The multiplication is: ", Result)

if __name__=="__main__":
    main()