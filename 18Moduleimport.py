from PrimeNUmModule import CheckPrime

def AddPrime(No):
    List=[]
    for i in range(No):
        Li=int(input("Enter the element: "))
        List.append(Li)
    print("The elements are : ",List)
    Primesum=0
    for i in List:
        Num= CheckPrime(i)
        if Num==True:
            Primesum=Primesum+i

    return Primesum

def main():

    No=int(input(" Enter the number of elements you want in your list: "))
    print("The number of elemetns are ",No)

    result= AddPrime(No)
    print("The addition of prime number is: ", result)

if __name__=="__main__":
    main()
