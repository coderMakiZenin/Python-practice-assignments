def Show(x):
    no=x
    while no!=0:
      print(no)
      no=no-1

def main ():
    x=int(input("Enter a number"))
    Show(x)

if __name__=='__main__':
    main()