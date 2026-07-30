import threading

def Even():
    Data=[]
    for i in range(1,21,1):
        if i%2==0:
            Data.append(i)
        
    print("The even numbers are: ", Data)


def Odd():
    Data=[]
    for i in range(1,21,1):
        if i%2!=0:
            Data.append(i)

    print("The odd numbers are: ", Data)

def main():

    Thread1=threading.Thread(target=Even)
    Thread2=threading.Thread(target=Odd)

    Thread1.start()
    Thread1.join()

    Thread2.start()
    Thread2.join()

if __name__=="__main__":
    main()
