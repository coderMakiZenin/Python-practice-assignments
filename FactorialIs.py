def Factorial(No):
    x=1
    for x in range(1,(No),1): 
        No=No*x
    return No
      
def main():
    Val = int(input("Enter a number: "))
    if (Val!=0):
       result= Factorial(Val)
       print("The Factorial of",Val,"! number is:", result)
    else:
       print("The Factorial of 0! is 1")

if __name__=="__main__":
    main()