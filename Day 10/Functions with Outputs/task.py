def format_name(f_name,l_name):
    name = (f_name+" "+ l_name).title()
    return  name

print(format_name("raKibul","iSlam"))



def inputs():
    name = input("Enter name :")
    roll = input("Enter ROll")

    return  name,roll

name_ = inputs()
print(name_[1])