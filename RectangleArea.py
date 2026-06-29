def RArea(Ln,Wd):

    Area= Ln*Wd

    return Area

def main():

    Ln= int(input("Enter the length of the rectangle: "))
    Wd= int(input("Enter the Width of the rectangle: "))

    result= RArea(Ln,Wd)
    print("The Area of Rectangle is:", result)

if __name__=="__main__":
    main()