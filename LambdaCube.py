
IsCube= lambda No: (No*No*No)

def main():
    No= int(input("Enter a number: "))
    Result= IsCube(No)
    print("The Cube is: ", Result)

if __name__=="__main__":
    main()
