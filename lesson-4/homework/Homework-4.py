# Homework-4

#1. https://www.hackerrank.com/challenges/write-a-function/problem

year = int(input("Please enter the year: "))

if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")    
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")    


#2. https://www.hackerrank.com/challenges/py-if-else/problem      

num = int(input("Enter the number: "))

if num%2:
    print("Weird.")
elif num%2 == 0 and num in range(2,6):
    print("Not weird.")
elif num%2 == 0 and num in range(6,21):
    print("Weird.")
elif num%2 == 0 and num > 20:
    print("Not weird.")

#3. Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop.

num1= int(input("Enter the 1st number: "))
if num1%2:
    num1+=1
num2= int(input("Enter the 2nd number: "))

even_nums = list(range(num1, num2+1, 2))

print(f"Even numbers between {num1-1} and {num2}: ", even_nums)

