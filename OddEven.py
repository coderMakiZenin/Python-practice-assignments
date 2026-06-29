def Even(No):
      for i in range(1,No,1):
        if (i%2==0):
          print(i)
       
def Odd(No):
   for i in range(1,No,1):
        if (i%2!=0):
          print(i)
       
def main():

    Val1 = int(input("Enter a number: "))

    while Val1==0:
        print("Enter a valid number")
        Val1= int(input("Enter a number: "))

    if Val1!=0:
      Val2 = int(input("Enter 1 if you want Even numbers and 0 if you want Odd numbers"))  
      while Val2!=0 and Val2!=1:
         print("Please enter a valid input")
         Val2 = int(input("Enter 1 if you want Even numbers and 0 if you want Odd numbers"))
      if Val2==1:
        Even(Val1)
      elif Val2==0:
        Odd(Val1)      
       
if __name__=="__main__":
   main()