def chkResult(Marks):

    if Marks>=75:
        print(Marks," is distinction")
    elif Marks>=60:
        print(Marks," is first class")
    elif Marks>=50:
        print(Marks," is second class")
    elif Marks<50:
        print(Marks," is Fail")


def main():

    Marks= int(input("Enter the marks obtained by the student: "))

    chkResult(Marks)

if __name__=="__main__":
    main()