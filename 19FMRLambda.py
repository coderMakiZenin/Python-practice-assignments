from functools import reduce

def main():
    No=int(input("Enter the number of elements in the list"))
    Data=[]
    for i in range(No):
        Num= int(input("Enter the element: "))
        Data.append(Num)

    fobj=list(filter(lambda x: 70<=x<=90, Data))
    print("The filtered list is: ",fobj)

    mobj=list(map(lambda x:x+10, fobj))
    print("The modified list is: ",mobj)

    robj=reduce(lambda x,y:x*y, mobj) 
    print("The product is: ",robj)  

if __name__=="__main__":
    main()