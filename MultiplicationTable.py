def TableIs(No):
    x=1
    for x in range(1,11): 
        N=No*x
        print(N)
      

def main():
    Val = int(input("Enter a number: "))
    TableIs(Val)

if __name__=="__main__":
    main()