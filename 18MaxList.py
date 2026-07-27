def MaxList(No):
    List=[]
    for i in range(No):
        Li=int(input("Enter the element: "))
        List.append(Li)
    print("The elements are : ",List)

    No1=List[0]
    for No2 in List:
        if No2>No1:   
            No1=No2

    return No1

def main():

    No=int(input(" Enter the number of elements you want in your list: "))
    print("The number of elemetns are ",No)

    result= MaxList(No)
    print("The maximum number is: ", result)

if __name__=="__main__":
    main()
