def Pattern(no):

    for i in range(no+1):
            for x in range(1,(i+1),1):
                print(x, end="")
            print("")

def main():

    no=int(input("Enter the number: "))
    Pattern(no)

if __name__=="__main__":
    main()