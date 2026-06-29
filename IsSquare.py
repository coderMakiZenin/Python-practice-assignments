def SquareOf(No):

    result= No*No
    return result

def main():

    Val= int(input("Enter the number"))
    result= SquareOf(Val)
    print("The Square of",Val,"is",result)

if __name__=="__main__":
    main()
    