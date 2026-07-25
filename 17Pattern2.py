def Pattern(no):

    for i in range(no):
            print("*"*no)
            no=no-1

def main():

    no=int(input("Enter the number: "))
    Pattern(no)

if __name__=="__main__":
    main()