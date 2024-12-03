name = ['Rakibul','Rijiya','Madhu']

if True :
    name_1 = name[0]  # also a global variable
print(name_1)

def namePrint():
    if True :
        name_2 = name[2]
    print(name_2) # local variable

namePrint()