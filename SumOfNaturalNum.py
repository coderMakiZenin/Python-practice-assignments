def SumOf(No):
    x=1
    for x in range(1,(No),1): 
        No=No+x
    return No
      
def main():
    Val = int(input("Enter a number: "))
    result= SumOf(Val)
    print("The sum of natural number is: ", result)

if __name__=="__main__":
    main()