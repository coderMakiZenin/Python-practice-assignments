def Perfect(No):
    x=0
    for i in range(1,No,1):
        if No%i==0:
            x=x+i
    if x==No:
        return True
    
    return False

def main():
    Value=int(input("Enter a number"))
    Factors= Perfect(Value)
    if Factors==True:
        print("The number is a perfect number!")
    else:
        print("The number is not perfect number!")

if __name__=="__main__":
    main()