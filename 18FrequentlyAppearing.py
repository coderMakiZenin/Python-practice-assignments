def Frequency(No):
    List=[]
    for i in range(No):
        Li=int(input("Enter the element: "))
        List.append(Li)
    print("The elements are : ",List)

    Search= int(input(" Enter the number you want to find the frequency of: "))
    print(f"Let's find out frequency of the number {Search}")

    Count=0
    for x in List:
        if x==Search:
            Count=Count+1

    return Count

def main():

    No=int(input(" Enter the number of elements you want in your list: "))
    print("The number of elemetns are ",No)

    result= Frequency(No)
    print("The frequency of the number is: ", result)

if __name__=="__main__":
    main()
