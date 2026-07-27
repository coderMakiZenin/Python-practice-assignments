Power=lambda x: 2**x

def main():
    x = int(input("Enter number: "))
    Result=Power(x)
    print("The Power is: ", Result)

if __name__=="__main__":
    main()