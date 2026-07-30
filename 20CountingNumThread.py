import threading

def Counting():
    for i in range(1,51,1):
        print(i)

def ReverseCount():
    i=50
    while i!=0:
        print(i)
        i=i-1

def main():

    Thread1=threading.Thread(target=Counting, name="Counting Thread")
    Thread2=threading.Thread(target=ReverseCount, name="ReverseCounting Thread")

    Thread1.start()
    Thread1.join()
    
    Thread2.start()
    Thread2.join()

if __name__=="__main__":
    main()
