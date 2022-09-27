from asyncore import read


def file_open():
    with open('C:/Users/AbdulRahman/empty-repo/AbdulRahman @ python basics/Kemi.txt','r' ) as f:
        print(f.read())
        print("Successfully Opened the file")

    return "1"    

file_open()    

open = lambda f : f * 45
print(open(3))


def trois(*args):
    return ("last kid :" + args[2])
print(trois("Tola","Tolu","Tayo"))

def validate(money):
    return money

def validate_salary():
    f = input("Enter your salary amount: ")
    salary = f
    print(salary)


while True:
    if validate_salary() >= validate(12000) :
        print("You are doing good ")
    else:
        print("Invalid ")    

    



