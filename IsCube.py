def CubeOf(No):

    result= No*No*No
    return result

def main():

    Val= int(input("Enter the number"))
    result= CubeOf(Val)
    print("The Cube of",Val,"is",result)

if __name__=="__main__":
    main()