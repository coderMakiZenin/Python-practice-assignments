class Circle:

    PI=3.14

    def __init__(self):

        self.R=0.0
        self.A=0.0
        self.C=0.0

    def Accept(self):
        self.R=float(input("Enter the radius of the circle: "))

    def Area(self):
        
        self.A=self.PI*(self.R**2)

    def Circumference(self):

        self.C=2*self.PI*self.R
    
    def Display(self):

        print("The Radius is: ",self.R)
        print("The Area is: ",self.A)
        print("The Circumference is: ",self.C)

def main():
    Obj= Circle()
    Obj.Accept()
    Obj.Area()
    Obj.Circumference()
    Obj.Display()

    CObj= Circle()
    CObj.Accept()
    CObj.Area()
    CObj.Circumference()
    CObj.Display()



if __name__=="__main__":
    main()
