class BookStore:
    NoOfbooks=0
    def __init__(self,Name,Author):
        self.Name=Name
        self.Author=Author
        BookStore.NoOfbooks=BookStore.NoOfbooks+1

    def Display(self):

        print(f"The Book name is: {self.Name} by Author {self.Author}.The number of books available are: {BookStore.NoOfbooks}")


def main():
    Obj1=BookStore("Linux Programming System", "Robert Love")
    Obj1.Display()

    Obj2=BookStore("C Programming", "Dennis Ritchie")
    Obj2.Display()

if __name__=="__main__":
    main()