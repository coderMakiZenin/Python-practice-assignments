from multiprocessing import Pool
from PrimeNumModule import CheckPrime

def CountPrime(No):
    Count=0
    for i in range(1,No+1,1):
        if CheckPrime(i):
            Count=Count+1

    return Count

def main():
    Data=[]
    num=int(input("Enter the number of elements you want: "))
    for i in range(num):
        No=int(input("Enter the element: "))
        Data.append(No)

    pobj=Pool()
    Result=pobj.map(CountPrime,Data)

    pobj.close()
    pobj.join()

    print("The prime count is: ",Result)

if __name__=="__main__":
    main()