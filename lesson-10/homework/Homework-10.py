# Homework-10

#1. Write a Python program to create a class representing a Circle.
# Include methods to calculate its area and perimeter.


from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def cal_area(self):
        return pi*(self.radius**2)
    
    def cal_circumference(self):
        return 2*pi*self.radius
    
#2. Write a Python program to create a person class. 
# Include attributes like name, country and date of birth.
# Implement a method to determine the person's age.

from datetime import date
class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.date_of_birth = dob
    
    def cal_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        return age
    
#3. Write a Python program to create a calculator class. Include methods for basic arithmetic operations.

class calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2
    def subtraction(self):
        return self.num1 - self.num2
    def multiplication(self):
        return self.num1 * self.num2
    def division(self):
        return self.num1 / self.num2

#4. Write a Python program to create a class that represents a shape. 
# Include methods to calculate its area and perimeter.
# Implement subclasses for different shapes like circle, triangle, and square.

class Shape:
    def cal_area(self):
        pass
    def cal_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    
    def cal_area(self):
        return pi*(self.radius**2)
        
    def cal_perimeter(self):
        return 2*pi*(self.radius)

class Square(Shape):
    def __init__(self,a):
        self.a = a
    def cal_area(self):
        return self.a**2
    def cal_perimeter(self):
        return 4*self.a

class Triangle(Shape):
    def __init__(self, base, height, s1, s2, s3):
        self.base = base
        self.height = height
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3

    def cal_area(self):
        return 0.5* self.base* self.height
                
    def cal_perimeter(self):
        return self.side1 + self.side2 + self.side3                




