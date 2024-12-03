import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#method - 1
random_index = random.randint(0,len(friends)-1)
print(friends[random_index])

#method - 2 (Best For List)
random_choice = random.choice(friends) # it'll take random element from the list
print(random_choice)

