from functools import reduce
from PrimeNUmModule import CheckPrime

def MaxNum(x, y):
    if x > y:
        return x
    else:
        return y

def main():
    No=int(input("Enter the number of elements in the list: "))
    Data=[]
    for i in range(No):
        Num= int(input("Enter the element: "))
        Data.append(Num)

    fobj=list(filter(CheckPrime, Data))
    print("The filtered list is: ",fobj)

    mobj=list(map(lambda x:x*2, fobj))
    print("The modified list is: ",mobj)

    robj=reduce(MaxNum, mobj) 
    print("The Maximum number is: ",robj)  

if __name__=="__main__":
    main()