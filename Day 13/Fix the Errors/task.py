try :
    age = int(input("How old are you?"))
except ValueError :
    print("You can't mix integers and strings in a comparison")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")
