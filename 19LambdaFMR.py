from functools import reduce

def main():
    No=int(input("Enter the number of elements in the list"))
    Data=[]
    for i in range(No):
        Num= int(input("Enter the element: "))
        Data.append(Num)

    fobj=list(filter(lambda x:x%2==0, Data))
    print("The filtered list is: ",fobj)

    mobj=list(map(lambda x:x**2, fobj))
    print("The modified list is: ",mobj)

    robj=reduce(lambda x,y:x+y, mobj) 
    print("The sum is: ",robj)  

if __name__=="__main__":
    main()