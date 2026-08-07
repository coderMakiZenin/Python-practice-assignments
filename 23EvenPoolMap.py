from multiprocessing import Pool
import os

def Even(No):
    print("Process ID :", os.getpid())
    print("Input Number :", No)
    x=0
    for i in range(1,No+1,1):
        if i%2==0:
            x=x+i

    print("The sum of even numbers is: ",x)
    
    return x

def main():
    Num=int(input("Enter the number of elements you need: "))
    Data=[]
    for i in range(Num):
        No=int(input("Enter the element: "))
        Data.append(No)

    Pmap=Pool()
    Result= Pmap.map(Even,Data)

    Pmap.close()
    Pmap.join()

    print("The list of sum of Even numbers is: ",Result)

if __name__=="__main__":
    main()