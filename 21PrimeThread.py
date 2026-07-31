import threading
from PrimeNumModule import CheckPrime

def Prime(Data):
    List=[]
    for i in Data:
        if CheckPrime(i):
            List.append(i)

    print("The prime numbers are: ",List)

def NonPrime(Data):
    List = []
    for i in Data:
        if not CheckPrime(i):
            List.append(i)

    print("Non-prime numbers:", List)

def main():
    Num=int(input("Enter the number of elements you want: "))

    Data=[]
    for x in range(Num):
        No=int(input("Enter the element: "))
        Data.append(No)

    Thread1=threading.Thread(target=Prime, args=(Data,))
    Thread2=threading.Thread(target=NonPrime, args=(Data,))

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()

if __name__=="__main__":
    main()