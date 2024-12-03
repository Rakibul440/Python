
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}
print(programming_dictionary["Function"])

# add new entry
programming_dictionary["Programmer_Name"] = "Rakibul Islam Mondal"

print(programming_dictionary)
#
# # Loop through Dict
# for key in programming_dictionary:
#     print(key , end=" : ")
#     print(programming_dictionary[key])
#
# # wipe entire dict
# programming_dictionary = {}
# print(programming_dictionary)

user = {
    "name" : ["Rijiya","Rakibul","Madhu"],
    "price" : [400,500,150]
}
print(max(user["price"]))
print(user['price'].index(500))
highest = 0
for i in range(len(user["price"])):
    if user['price'][i] > highest :
        highest = user["price"][i]

print(highest)