IsOdd= lambda No: No%2==0

def FilterX(Task, Elements):
    result=[]
    for no in Elements:
        ret= Task(no)
        if ret==False:
         result.append(no)
    return result

def main():
    No=int(input(" Enter the number of elements: "))
    Data = []
    for i in range(1,(No+1)):
        Val=int(input("Enter the number: "))
        Data.append(Val)

    Result= FilterX(IsOdd,Data)
    print("The odd numbers are: ", Result)

if __name__=="__main__":
    main()