from multiprocessing import Pool

def SquareOF(No):
    x=0
    sq=0
    for i in range(1,No+1,1):
        sq=i*i
        x=x+sq
    return x

def main():
    Num=int(input("Enter the number of elements you need: "))
    Data=[]
    for i in range(Num):
        No=int(input("Enter the element: "))
        Data.append(No)

    Pmap=Pool()
    Result= Pmap.map(SquareOF,Data)

    Pmap.close()
    Pmap.join()

    print("The Squares are: ",Result)

if __name__=="__main__":
    main()