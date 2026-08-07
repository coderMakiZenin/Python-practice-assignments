class Arithmatic:

    def __init__(self):

        self.Value1=0
        self.Value2=0

    def Accept(self):

        self.Value1=int(input("Enter first value: "))
        print("The first value is: ",self.Value1)
        
        self.Value2=int(input("Enter second value: "))
        print("The second value is: ",self.Value2)

    def Add(self):
        
        No= self.Value1+self.Value2
        return No

    def Substract(self):

        No= self.Value1-self.Value2
        return No

    def Multiply(self):

        No= self.Value1*self.Value2
        return No

    def Divide(self):

        try:
            No= self.Value1/self.Value2
            return No
        except ZeroDivisionError:
            print("Division with zero is not allowed!!")        

def main():
    Obj= Arithmatic()
    Obj.Accept()
    print(" The Addition is: ",Obj.Add())
    print("The Substraction is: ",Obj.Substract())
    print("The Multiplication is: ",Obj.Multiply())
    print("The Division is: ",Obj.Divide())


    AObj= Arithmatic()
    AObj.Accept()
    print(" The Addition is: ",AObj.Add())
    print("The Substraction is: ",AObj.Substract())
    print("The Multiplication is: ",AObj.Multiply())
    print("The Division is: ",AObj.Divide())

if __name__=="__main__":
    main()
