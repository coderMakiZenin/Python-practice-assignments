import threading

Lock=threading.Lock()
Var=0

def AdditionFun(Num):
    Lock.acquire()
    global Var
    Var=Var+Num
    print("AdditionFun Variable: ",Var)
    Lock.release()

def SubstractionFun(Num):
    Lock.acquire()
    global Var
    Var=Var-Num
    print("SubstractionFun Variable: ",Var)
    Lock.release()

def main():
    Num=int(input("Enter a number: "))

    Thread1=threading.Thread(target=AdditionFun, args=(Num,))
    Thread2=threading.Thread(target=SubstractionFun, args=(Num,))

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()

    print("Exit from Main")

if __name__=="__main__":
    main()