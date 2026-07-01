def FactorsOf(No):
    x=[]
    for i in range(1,No,1):
        if No%i==0:
            x.append(i)
        else:
            pass
    return x

def main():
    Value=int(input("Enter a number"))
    Factors= FactorsOf(Value)
    print("The Factors of the given number are:", Factors)

if __name__=="__main__":
    main()