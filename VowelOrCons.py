def chkVowel(Ch):
    if Ch=='a'or Ch=='e' or Ch=='i' or Ch=='o' or Ch=='u' or Ch=='A' or Ch=='E' or Ch=='I' or Ch=='O'or Ch=='U':
        return True
    else:
        return False
    
def main():
    Char=input("Enter a letter")
    Ch=chkVowel(Char)
    if Ch==True:
        print("The letter is a vowel")
    else:
        print("The letter is not a vowel")
if __name__=="__main__":
    main()