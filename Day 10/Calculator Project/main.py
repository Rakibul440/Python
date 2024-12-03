import art
def add(n1, n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mul(n1,n2):
    return n1 * n2

def div(n1,n2):
    return n1 / n2

operations = {
    '+' : add,
    '-' : sub,
    '*' : mul,
    '/' : div,
}

def calculator() :
    print(art.logo)
    should_accumulate = True
    f_num = int(input("What's the first number ? : "))

    while should_accumulate :
        operator = input("What type of operation do you want to perform\n'+' - Addition\n'-' - Subtraction\n'*' - Multiplication\n'/' - Division\nPick an operation :")
        n_num = int(input("What's the next number ? : "))
        result = operations[operator](f_num,n_num)
        print(f"{f_num} {operator} {n_num} = {result}")
        continue_cal = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()


        if continue_cal == 'y':
            f_num = result
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()