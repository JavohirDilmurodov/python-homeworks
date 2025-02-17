# Homework-6

#1. is_prime(n) funksiyasini hosil qiling. Agar n soni tub bulsa True, ask holda False qiymat qaytarilsin.

import math


def is_prime(n):
    """Function that returns whether the given number is prime or not"""

    if n == 1:
        print("Number is not prime")
    elif n == 2:
        print("Number is prime")      

    else:
        for i in range(2,math.ceil(n**0.5)):
            if n%i == 0:
                print("Number is not prime")
                break
        else:
            print("Number is prime")
           

is_prime(99)       

#2. K sonining raqamlari yigindisini hisoblovchi digit_sum(k) rekursiv funksiya yozing.

def digit_sum(k):
    """Function that returns sum of digits to the given number"""
    
    sum = 0
    for i in str(k):
        sum += int(i)
    return sum 

print(digit_sum(123))   

#3. It is required to print all integer powers of 2. that don't exceed the number N.


def func3(num):
    i = 2
    while num>=i:
        print(i)
        i *= 2

func3(16)

