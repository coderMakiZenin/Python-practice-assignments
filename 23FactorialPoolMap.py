from multiprocessing import Pool
import os

def Factorial(No):
    print("Process ID:", os.getpid())
    print("Input Number :", No)
    Fact=1
    for x in range(1,(No+1),1): 
        Fact=Fact*x

    print("The factorials is: ",Fact)
    return Fact

def main():
    Num=int(input("Enter the number of elements you need: "))
    Data=[]
    for i in range(Num):
        No=int(input("Enter the element: "))
        Data.append(No)

    print("The elements are: ",Data)

    Pmap=Pool()
    Result= Pmap.map(Factorial,Data)

    Pmap.close()
    Pmap.join()

    print("The list of factorials is: ",Result)

if __name__=="__main__":
    main()