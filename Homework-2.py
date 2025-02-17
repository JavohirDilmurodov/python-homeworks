# Homework-2

    # Sub Homework-1
    #1. Create a tuple literal named cardinal_numbers that holds the strings
    #"first", "second", and "third", in that order.
    #2. Using index notation and print(), display the string at index 1 in
    #cardinal_numbers.
    #3. In a single line of code, unpack the values in cardinal_numbers into
    #three new strings named position1, position2, and position3. Then
    #print each value on a separate line.
    #4. Using tuple() and a string literal, create a tuple called my_name that
    #contains the letters of your name.
    #5. Check whether the character "x" is in my_name using the in keyword.
    #6. Create a new tuple containing all but the first letter in my_name using
    #slice notation.

    #1.1 
cardinal_numbers = ("first", "second", "third")
    #1.2
print(cardinal_numbers[1])
    #1.3
position1, position2, position3 = cardinal_numbers
print(position1)
print(position2)
print(position3)

    #1.4
my_name = tuple("Javohir")
    #1.5
if 'x' in my_name:
    print("exists")
else:
    print("not exists")

    #1.6
new_tuple = tuple(my_name[1::])    
print(new_tuple)



    # Sub Homework-2
    # 1. Create a list named food with two elements, "rice" and "beans".
    # 2. Append the string "broccoli" to food using .append().
    # 3. Add the strings "bread" and "pizza" to food using .extend().
    # 4. Print the first two items in the food list using print() and slice notation.
    # 5. Print the last item in food using print() and index notation.
    # 6. Create a list called breakfast from the string "eggs, fruit, orange
    # juice" using the string .split() method.
    # 7. Verify that breakfast has three items using len().
    # 8. Create a new list called lengths using a list comprehension that contains the lengths of each string in the breakfast list
        

#2.1
food = ["rice", "beans"]
#2.2
food.append("broccoli")
#2.3
food.extend(["bread", "pizza"])
#2.4
print(food[:2])
#2.5
print(food[-1])
#2.6
breakfast = ["eggs", "fruit", "orange juice"]
#2.7
print(len(breakfast))

#2.8
lengths = [len(x) for x in breakfast]
print(lengths) 


    # Sub Homework-3
    # Given two integer variables: a and b. Swap the values of the variables.

    # a = int(input())
    # b = int(input())

    # Solve this problem in 3 ways

a = int(input("Enter the first num: "))
b = int(input("Enter the second num: "))

c = a
a = b
b = c
print("Swapped values: ", a, b)