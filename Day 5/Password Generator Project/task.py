import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Hard Level


# Easy level
password = ''
pass_letter =[]
pass_num = []
pass_sym = []
password_list = []

if (nr_numbers >= 0 and nr_numbers < len(numbers)) and (nr_symbols >=0 and nr_symbols < len(symbols)) and (nr_letters >=0 and nr_letters < len(letters)) :

    for i in range(nr_letters) :
        pass_letter.append(letters[random.randint(0,len(letters)-1)])

    for i in range(nr_symbols):
        pass_sym.append(symbols[random.randint(0,len(symbols)-1)])

    for i in range(nr_numbers):
        pass_num.append(numbers[random.randint(0,len(numbers)-1)])

    password_list = pass_letter + pass_sym + pass_num
    print(password_list)

    random.shuffle(password_list) # change list item's position randomly
    for i in range(len(password_list)-1):
        password += password_list[i]


    print(password_list)
    print(f"Your password is : {password}")

else:
    print("Enter a positive number.\nTry Again!!")


''' 
# Easy level
password = ''
pass_letter =[]
pass_num = []
pass_sym = []
password_list = []

if (nr_numbers >= 0 and nr_numbers < len(numbers)) and (nr_symbols >=0 and nr_symbols < len(symbols)) and (nr_letters >=0 and nr_letters < len(letters)) :

    for i in range(nr_letters) :
        pass_letter.append(letters[random.randint(0,len(letters)-1)])
        password += pass_letter[i]

    for i in range(nr_symbols):
        pass_sym.append(symbols[random.randint(0,len(symbols)-1)])
        password += pass_sym[i]

    for i in range(nr_numbers):
        pass_num.append(numbers[random.randint(0,len(numbers)-1)])
        password += pass_num[i]

    password_list = pass_letter + pass_sym + pass_num

    # print(pass_letter)
    # print(pass_sym)
    # print(pass_num)
    print(password_list)
    print(f"Your password is : {password}")

else:
    print("Enter a positive number.\nTry Again!!")
'''

