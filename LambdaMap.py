
SquareIs= lambda No: No*No

def MapX(Task, Elements):
    result=[]
    for no in Elements:
        ret= Task(no)
        result.append(ret)
    return result

def main():
    No=int(input(" Enter the number of elements: "))
    Data = []
    for i in range(1,(No+1)):
        Val=int(input("Enter the number"))
        Data.append(Val)

    Result= MapX(SquareIs,Data)
    print(f"The Square of {Data} is: ", Result)

if __name__=="__main__":
    main()
