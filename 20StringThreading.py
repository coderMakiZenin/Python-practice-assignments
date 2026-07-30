import threading

Lock=threading.Lock()

def Small(String):

    count=0
    for ch in String:
        if 97 <= ord(ch) <= 122:
            count=count+1

    Lock.acquire()

    print(f"There are {count} small letters in the string")
    Current = threading.current_thread()

    print("Thread Name:", Current.name)
    print("Thread ID:", Current.ident)

    Lock.release()

def Capital(String):

    count=0
    for ch in String:
        if 65 <= ord(ch) <= 90:
            count=count+1
    Lock.acquire()

    print(f"There are {count} capital letters in the string")
    Current = threading.current_thread()

    print("Thread Name:", Current.name)
    print("Thread ID:", Current.ident)

    Lock.release()

def DigitCount(String):

    count=0
    for ch in String:
        if 48 <= ord(ch) <= 57:
            count=count+1

    Lock.acquire()

    print(f"There are {count} digit values in the string")
    Current = threading.current_thread()

    print("Thread Name:", Current.name)
    print("Thread ID:", Current.ident)

    Lock.release()

def main():
    String=input("Enter the string: ")

    Thread1 = threading.Thread(target=Small,args=(String,))
    Thread2 = threading.Thread(target=Capital,args=(String,))
    Thread3 = threading.Thread(target=DigitCount, args=(String,))

    Thread1.start()
    Thread2.start()
    Thread3.start()

    Thread1.join()
    Thread2.join()
    Thread3.join()

if __name__=="__main__":
    main()
