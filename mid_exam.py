#1. Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

input_hour = int(input("Enter the hours: "))
rate = int(input("Enter the rate: "))
result = input_hour*rate
print(f"Your weekly earning: {result}")


#2. Make the following using string formatting methods:

# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1*num2
division = num1/num2
modulo = num1 % num2
int_part = num1//num2
power = num1**num2

print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")
print(f"{num1} % {num2} = {modulo}")
print(f"{num1} // {num2} = {int_part}")
print(f"{num1} ** {num2} = {power}")

#3. Get user input using input(“Enter your age: ”). 
# If user is 18 or older, give feedback: You are old enough to drive. 
# If below 18 give feedback to wait for the missing amount of years.


age = int(input("Enter your age: "))

if age > 18:
    print("You are old enough to drive.")
elif age < 18:
    print(f"You should wait {18-age} years more")
else:
    print("Invalid input.")

#4. Write code for that output, using loops:

#
##
###
####
#####
######
#######


for i in range(8):
    print("#"*i)


#5. Use any loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

#The sum of all evens is 2550. And the sum of all odds is 2500.

sum = 0
for i in range(101):
    if i % 2 == 0:
        sum += i
print(f"The sum of all evens is: {sum}")


#6. Write a functions which checks if all items are unique in the list. Return True or False

def unique_items(ls):
    return len(ls) == len(set(ls))


ls = [1, 2, 3, 4, 5]
print(unique_items(ls)) 

ls2 = [1, 2, 3, 3, 5]
print(unique_items(ls2)) 


