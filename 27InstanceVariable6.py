class Numbers:

    def __init__(self,Value):
        self.Value=Value

    def ChkPrime(self):

        if self.Value <= 1:
            return False
        
        for i in range(2,self.Value):
            if self.Value%i==0:
                return False
          
        return True

    def ChkPerfect(self):

        Sum = 0

        for i in range(1, self.Value):

            if self.Value % i == 0:
                Sum = Sum + i

        if Sum == self.Value:
            return True
        else:
            return False
        
    def Factors(self):
        self.x=[]
        for i in range(1,self.Value,1):
            if self.Value%i==0:
                self.x.append(i)

        print("The Factors are: ",self.x)
    
    def SumFactors(self):

        Sumof=0
        for i in self.x:
            Sumof=Sumof+i

        return Sumof

def main():

    Obj1=Numbers(21)

    Result=Obj1.ChkPrime()
    if Result==True:
        print("The number is Prime")
    else:
       print("The number is not Prime") 

    Result=Obj1.ChkPerfect()
    if Result==True:
        print("The number is Perfect")
    else:
       print("The number is not Perfect") 

    Obj1.Factors()
    print(" The sum of factors is: ", Obj1.SumFactors())

    Obj2=Numbers(51)

    Result=Obj2.ChkPrime()
    if Result==True:
        print("The number is Prime")
    else:
       print("The number is not Prime") 

    Result=Obj2.ChkPerfect()
    if Result==True:
        print("The number is Perfect")
    else:
       print("The number is not Perfect") 

    Obj2.Factors()
    print(" The sum of factors is: ", Obj2.SumFactors())

if __name__=="__main__":
    main()
