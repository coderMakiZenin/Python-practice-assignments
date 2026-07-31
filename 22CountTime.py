from multiprocessing import Pool
import time

def PowerOfFive(No):
    x=0
    for i in range(1,No+1,1):
        x=x+(i**5)
    return x

def main():
    Num=int(input("Enter the number of elements you need: "))
    Data=[]
    for i in range(Num):
        No=int(input("Enter the element: "))
        Data.append(No)

    StartTime=time.time()

    Pmap=Pool()
    Result= Pmap.map(PowerOfFive,Data)

    Pmap.close()
    Pmap.join()

    print("The sum is: ",Result)

    EndTime=time.time()
    print("Execution Time is: ",EndTime-StartTime)

if __name__=="__main__":
    main()