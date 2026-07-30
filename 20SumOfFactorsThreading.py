import threading

Lock=threading.Lock()

def Even(No):
        
    Data=[]
    for i in range(1,No+1):
        if No%i==0:
            Data.append(i)

    EvenSum=0
    for x in Data:
        if x%2==0:
            EvenSum=EvenSum+x
    Lock.acquire()       
    print("The sum of even factors is: ", EvenSum)
    Lock.release()

def Odd(No):

    Data=[]
    for i in range(1,No+1):
        if No%i==0:
            Data.append(i)

    OddSum=0
    for x in Data:
        if x%2!=0:
            OddSum=OddSum+x

    Lock.acquire()        
    print("The sum of odd factors is: ", OddSum)
    Lock.release()

def main():

    No=int(input("Enter a number: "))

    Thread1=threading.Thread(target=Even, args=(No,))
    Thread2=threading.Thread(target=Odd, args=(No,))

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()

    print("Exit from Main")

if __name__=="__main__":
    main()
