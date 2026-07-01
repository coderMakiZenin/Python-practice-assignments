def SeriesPrint(No):
    for i in range(1,(No+1)):
        print(i)

def main():
    Value=int(input("Enter a number"))
    SeriesPrint(Value)

if __name__=="__main__":
    main()