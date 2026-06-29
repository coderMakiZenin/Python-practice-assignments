def CArea(R):

    Area= 3.14*R*R

    return Area

def main():

    Radius= int(input("Enter the radius of the circle: "))

    result= CArea(Radius)
    print("The Area of Circle is:", result)

if __name__=="__main__":
    main()