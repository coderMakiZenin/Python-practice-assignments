def Prime(No):
    for i in range(2,No,1):
        if No%i==0:
            return True
    
    return False
                
def main():
    Value=int(input("Enter a number:"))
    Result=Prime(Value)
    if Result==True:
        print("The number is not prime!")
    else:
        print("The number is prime!")
        
if __name__=="__main__":
    main()
