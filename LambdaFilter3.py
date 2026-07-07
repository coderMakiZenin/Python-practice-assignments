IsDivisible= lambda No: No%3==0 and No%5==0

def FilterX(Task, Elements):
    result=[]
    for no in Elements:
        ret= Task(no)
        if ret==True:
         result.append(no)
    return result

def main():
    No=int(input(" Enter the number of elements: "))
    Data = []
    for i in range(1,(No+1)):
        Val=int(input("Enter the number: "))
        Data.append(Val)

    Result= FilterX(IsDivisible,Data)
    print("The numbers divisible by 3 and 5 are: ", Result)

if __name__=="__main__":
    main()