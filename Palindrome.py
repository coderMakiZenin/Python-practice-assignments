def chkPalindrome(No):
    x=0
    i=0
    Num= No
    while No!=0:
          i=No%10
          x=x*10+i
          No=No//10
    if Num==x:
        return True
    return False

def main():

    Value= int(input("Enter the number: "))
    Palindrome= chkPalindrome(Value)
    if Palindrome==True:
        print("The number is palindrome")
    else:
        print("The number is not a palindrome")

if __name__=="__main__":
    main()