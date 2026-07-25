def Factorial(x):
    No=x
    for i in range(1,(x),1): 
        No=No*i
    return No
      
def main():
    Val = int(input("Enter a number: "))
    Result=Factorial(Val)
    print("The Factorial is: ",Result)

if __name__=="__main__":
    main()