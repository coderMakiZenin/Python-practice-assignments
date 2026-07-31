import threading
Lock=threading.Lock()

def Add(Data):
    x=0
    for i in Data:
        x=x+i
    Lock.acquire()
    print("Sum of elements from the list is: ",x)
    Lock.release()

def Product(Data):
    x=1
    for i in Data:
        x=x*i
    Lock.acquire()
    print("Product of elements from the list is: ",x)
    Lock.release()

def main():
    Num=int(input("Enter the number of elements you want: "))

    Data=[]
    for x in range(Num):
        No=int(input("Enter the element: "))
        Data.append(No)

    Thread1=threading.Thread(target=Add, args=(Data,))
    Thread2=threading.Thread(target=Product, args=(Data,))

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()

    print("Exit from Main")

if __name__=="__main__":
    main()