import threading

Lock=threading.Lock()

def Even(Data):
    EvenSum=0
    for x in Data:
        if x%2==0:
            EvenSum=EvenSum+x
    Lock.acquire()       
    print("The sum of even elements is: ", EvenSum)
    Lock.release()

def Odd(Data):

    OddSum=0
    for x in Data:
        if x%2!=0:
            OddSum=OddSum+x

    Lock.acquire()        
    print("The sum of odd elements is: ", OddSum)
    Lock.release()

def main():
    No=int(input("Enter the number of elements you need: "))
    
    Data=[]
    for i in range(1,No+1):
        Num=int(input("Enter the element: "))
        Data.append(Num)

    Thread1=threading.Thread(target=Even, args=(Data,))
    Thread2=threading.Thread(target=Odd, args=(Data,))

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()

    print("Exit from Main")

if __name__=="__main__":
    main()
