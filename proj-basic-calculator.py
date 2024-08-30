import art

def add(n1, n2):
    return n1 + n2

def subs(n1,n2):
    return n1-n2

def mult(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

def calculator():
    print(art.calc_logo)
    no1=float(input("Enter the First number: "))

    while True:
        symbols = {
            "+": add,
            "-": subs,
            "*": mult,
            "/": divide,
        }
        for symb in symbols:
            print(symb)

        operation_symbol=input("Pick an operation: ")
        no2=float(input("Enter the Second number: "))
        ans=symbols[operation_symbol](no1,no2)
        print(f"{no1} {operation_symbol} {no2} = {ans}")
        ch2=input(f"Type 'y' to operate with {ans}? Enter 'no' if you want to end:"'\n')
        if ch2=='y':
            no1=ans
        else:
            print("Good luck solving! ")
            print('\n' * 20)
            calculator()

calculator()
