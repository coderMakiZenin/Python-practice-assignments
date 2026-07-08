CountEven=lambda No: No%2==0

def FilterX(Task,Elements):
    count=0
    for no in Elements:
        ret= Task(no)
        if ret==True:
         count=count+1
    return count
    
def main():
    No=int(input(" Enter the number of elements: "))
    Data = []
    for i in range(1,(No+1)):
        Val=int(input("Enter the number: "))
        Data.append(Val)

    Result= FilterX(CountEven,Data)
    print("The number of even numbers in your list is: ", Result)

if __name__=="__main__":
    main()