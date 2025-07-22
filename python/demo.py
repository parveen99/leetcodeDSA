#Lets learb about __name__

#if I run this file it prints -> Hello __main__

def func1():
    print("Printing FUnction 1")

def func2():
    print("Printing Function 2")

def main_1():
    func1()
    func2()

if __name__ == "__main__":
    print("Hello", __name__) 
    main_1()