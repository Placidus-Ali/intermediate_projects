# Q1:
# Use else block to display a message “Done” after successful execution of for loop.
for i in range(5,10):
    print(i)
else:
    print('Done!')

#Q2:
# Write a program to display all prime numbers within a range.
for x in range(1,20):
  if x >1:
    for y in range(2, x):
        if x % y==0:
            break
    else:
        print(x)

#Q3:
#Use a loop to display elements from a given list present at odd index positions

for numbers in range(20):
    if numbers % 2 !=0:
        print(numbers)


#Q4:
#Calculate the cube of all numbers from 1 to a given number
for a in range(1,11):
    print(a**3)
