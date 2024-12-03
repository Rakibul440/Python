for number in range(1,10): # exclude 10
    print(number,end=" ")
print("\n")

for number in range(0,11,2): # step 2
    print(number,end=",")
print("\n")

# The Gauss Challenge
total = 0
for number in range(1,101):
    total += number
print(f"Total : {total}")


