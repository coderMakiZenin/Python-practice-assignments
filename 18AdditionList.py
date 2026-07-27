def AddList(No):
    List=0
    for i in range(No):

        Li=int(input("Enter the element: "))

        List=List+Li

    return List

def main():

    No=int(input(" Enter the number of elements you want in your list: "))
    print("The number of elemetns are ",No)

    result= AddList(No)
    print("The Addition is: ", result)

if __name__=="__main__":
    main()
