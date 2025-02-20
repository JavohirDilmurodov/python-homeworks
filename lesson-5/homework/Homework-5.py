# Homework-5

#1. https://www.hackerrank.com/challenges/python-loops/problem

boundary = int(input("Enter the upper boundary(integer): "))

for i in range(0, boundary):
    print(i**2)

#2. Return the uncommon elements of lists

from collections import Counter

def find_uncommon_elements(list1, list2):
   
    count1 = Counter(list1)
    count2 = Counter(list2)
    result = []
    
    for element in count1:
        if element not in count2:
            result.extend([element] * count1[element])
        elif count1[element] != count2[element]:
            result.extend([element] * abs(count1[element] - count2[element]))
    
    for element in count2:
        if element not in count1:
            result.extend([element] * count2[element])
    
    return result

#3.

def add_underscore(text):
    text = text[0:3] + '_' + text[3:]
    return text

print(add_underscore("abcabcdabcde"))


#4. https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/

#4.1
i=1

while i<=10:
    print(i)
    i+=1

#4.2
    for i in range(1,6):
        for j in range(1, i+1):
            print(j, end=' ')
        print(' ')    

#4.3

num = int(input("Enter a number: "))
sum = 0
for i in range(1,num+1):
    sum = sum + i
print(sum)

#4.4
