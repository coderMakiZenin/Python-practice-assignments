def Show(x):
    for i in range(1,(x+1),1):
       if (i%2==0):
          print(i)
       i=i+1

def main():
    no= int(input("Enter any number: "))
    Show(no)
if __name__=='__main__':
    main()