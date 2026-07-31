import threading
Lock=threading.Lock()

def Maximum(Data):
    x=Data[0]
    for i in Data:
        if i>x:
            x=i
    Lock.acquire()
    print("Maximum element from list is: ",x)
    Lock.release()

def Minimum(Data):
    x=Data[0]
    for i in Data:
        if i<x:
            x=i
    Lock.acquire()
    print("Minimum element from list is: ",x)
    Lock.release()

def main():
    Num=int(input("Enter the number of elements you want: "))

    Data=[]
    for x in range(Num):
        No=int(input("Enter the element: "))
        Data.append(No)

    Thread1=threading.Thread(target=Maximum, args=(Data,))
    Thread2=threading.Thread(target=Minimum, args=(Data,))

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()

if __name__=="__main__":
    main()