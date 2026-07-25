def AddFact(no):
    x=0
    for i in range(1,(no),1):
        if no%i==0:
            x=x+i

    return x

def main():
    val=int(input(" Enter any number: "))
    result=AddFact(val)
    print("The addition of factors is:", result)

if __name__=="__main__":
    main()