def CheckPrime(No):
    if No<2:
        return False
    for i in range(2,No,1):
        if No%i==0:
            return False
    return True
                
def main():
    Value=int(input("Enter a number:"))
    Result=CheckPrime(Value)
    if Result==True:
        print("The number is not prime!")
    else:
        print("The number is prime!")
        
if __name__=="__main__":
    main()