Multi= lambda No1,No2: No1*No2

def ReduceX(Task, Elements):
    result=1
    for no in Elements:
        result=Task(result,no)
    return result

def main():
    No=int(input(" Enter the number of elements: "))
    Data = []
    for i in range(1,(No+1)):
        Val=int(input("Enter the number: "))
        Data.append(Val)

    Result= ReduceX(Multi,Data)
    print("The Product is: ", Result)

if __name__=="__main__":
    main()