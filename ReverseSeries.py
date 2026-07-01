def SeriesPrint(No):
    for i in range(No,0,-1):
        print(i)

def main():
    Value=int(input("Enter a number"))
    SeriesPrint(Value)

if __name__=="__main__":
    main()