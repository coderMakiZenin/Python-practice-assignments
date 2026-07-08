StrLen=lambda str: len(str)>5

def FilterX(Task,Elements):
    result=[]
    for str in Elements:
        ret= Task(str)
        if ret==True:
            result.append(str)
    return result
    
def main():
    No=int(input(" Enter the number of elements: "))
    Data = []
    for i in range(1,(No+1)):
        Val=input("Enter the number: ")
        Data.append(Val)

    Result= FilterX(StrLen,Data)
    print("The strings with length more than 5 characters are",Result)

if __name__=="__main__":
    main()