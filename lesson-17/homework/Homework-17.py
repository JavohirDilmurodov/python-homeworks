# Homework-17

import pandas as pd
import numpy as np

#1.
data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} 
df = pd.DataFrame(data)

#1.1
mapper = {"First Name":"first_name", "Age":"age"}
df = df.rename(columns=mapper)
print(df)

#1.2
print(df.head(3))

#1.3
mean_age = df['age'].mean()
print(mean_age)

#1.4
print(df[["first_name", "City"]])

#1.5
df["Salary"] = [10_000, 20_000, 30_000, 25_000]
print(df)

#1.6
print(df.describe())

#2.1 

import pandas as pd

data2 = {"Month" : ['Jan', 'Feb', 'Mar', 'Apr'],
         "Sales" : [5000, 6000, 7500, 8000],
         "Expenses" : [3000, 3500, 4000, 4500]}
sales_and_expenses = pd.DataFrame(data2)
# print(df2)

#2.2, 2.3, 2.4
print(sales_and_expenses['Sales'].describe())
print(sales_and_expenses['Expenses'].describe())

#3.1

import pandas as pd

data3 = {"Category" : ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
         "January" : [1200, 200, 300, 150],
         "February" : [1300, 220, 320, 160],
         "March" : [1400, 240, 330, 170],
         "April" : [1500, 250, 350, 180]}
expenses = pd.DataFrame(data3)
expenses = expenses.set_index("Category")

#3.2

expenses['Max_exp'] = expenses.max(axis=1)

#3.3

expenses['Min_exp'] = expenses.min(axis=1)

#3.4

expenses['Avg_exp'] = expenses.mean(axis=1)

print(expenses)
