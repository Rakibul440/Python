
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

# find max score
#using for loop
max_score = student_scores[0]
for score in student_scores:
    if score > max_score :
        max_score = score

print("Max score is : ",max_score)

# using max function
maximum = max(student_scores)
print("maximum : ",maximum)

#find sum
# Using for loop
total = 0
for score in student_scores:
    total = total + score
print("Total score  : ",total)

#using sum function
total_score = sum(student_scores)
print(total_score)