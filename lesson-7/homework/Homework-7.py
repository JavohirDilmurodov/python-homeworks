# Homework-7

#1. https://www.w3resource.com/python-exercises/python-exception-handling-exercises.php

#1.1

def divide_numbers(x,y):
    try:
        z = x/y
        print(z)
    except ZeroDivisionError:
        print("Dividing by 0 is not permissible.")    

divide_numbers(10,0)

#1.2

def input_int():
    try:
        num = int(input("Enter an integer: "))
        print(num)
    except ValueError:
        print("Invalid input.")        

input_int()

#1.3
def open_file(filename):
    try:       
        file = open(filename, 'r')
        c = file.read()
        print(c)
        file.close()
    
    except FileNotFoundError:        
        print("Error: File not found.")

#1.4
def two_nums():
    try:
        num1 = int(input("Enter the 1st num: "))
        num2 = int(input("Enter the 2nd num: "))
        print(num1+num2)
    except ValueError:
        print("You have not entered integer number.")        

two_nums()

#1.5

def permission(filename):
    try:
        with open(filename,'r') as file:
            content = file.write('Hello')
    except PermissionError:
        print("Permission denied due to mismatching mode.")

#1.6
fruits = ['olma','nok','anjir']

try:
    print(fruits[3])
except IndexError:
    print(f'This list has only {len(fruits)} items.')

#2. https://www.w3resource.com/python-exercises/file/

#2.1
def read_fully(filename):
    with open(filename,'r') as f:
        contents = f.read()
        print(contents)

#2.3
def append_file(filename):
    with open(filename,'a') as file:
        file.write("I am appending the existing file.")

#2.5
def file_read(fname):
        with open(fname) as f:  
                content_list = f.readlines()
                print(content_list)




