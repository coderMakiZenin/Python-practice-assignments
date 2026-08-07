class Demo:
    Value=0
    def __init__(self,No1,No2):
        self.No1=No1
        self.No2=No2   

    def Fun(self):
        print("This is No1 of Fun: ", self.No1)
        print("This is No2 of Fun: ", self.No2)

    def Gun(self):
        print("This is No1 of Gun: ", self.No1)
        print("This is No2 of Gun: ", self.No2)

def main():
    Obj1= Demo(11,51)
    Obj2=Demo(51,101)

    Obj1.Fun()
    Obj2.Fun()

    Obj1.Gun()
    Obj2.Gun()

if __name__=="__main__":
    main()
