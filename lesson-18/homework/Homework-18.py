import pandas as pd 

#2.

df = pd.read_csv('lesson-18\homework\stackoverflow_qa.csv')

#2.1
print(df[df['creationdate'] < '2014-01-01 00:00:00'])

#2.2
print(df[df['score'] > 50])

#2.3
print(df[df['score'].between(50,100)])

#2.4
print(df[df['ans_name'] == 'Scott Boston'])

#2.5
print(df[df['ans_name'].isin(['Scott Boston', 'Jason Strimpel', 'Mike Pennington'])])

#2.6
print(df[df['creationdate'].between('2014-03-01', '2014-10-01') & (df['ans_name'] == 'Unutbu') & (df['score'] < 5)])

#2.7
print(df[df['score'].between(5,10) | (df['viewcount'] > 10_000)])

#2.8
print(df[df['ans_name'] != 'Scott Boston'])


#3.

df2 = pd.read_csv('lesson-18\homework\/titanic.csv')

#3.1
print(df2[(df2['Sex'] == 'female') & (df2['Pclass'] == 1) & (df2['Age'].between(20,30))])
print(df2[(df2['Sex'] == 'female') & (df2['Pclass'] == 1) & (df2['Age'].between(20,30))][['Sex', 'Pclass', 'Age']])

#3.2
print(df2[df2['Fare'] > 100])

#3.3
print(df2[(df2['Survived'] == 1) & (df2['SibSp'] == 0) & (df2['Parch'] == 0)])

#3.4
print(df2[(df2['Embarked'] == 'C') & (df2['Fare'] > 50)])

#3.5
print(df2[(df2['SibSp'] > 0) & (df2['Parch'] > 0)])

#3.6
print(df2[(df2['Age'] <= 15) & (df2['Survived'] == 0)])

#3.7
print(df2[(df2['Cabin'] != 'NaN') & (df2['Fare'] > 200)])

#3.8
print(df2[df2["PassengerId"] % 2 == 1])

#3.9

# In this sub-task every ticket has unique numbers.

#3.10
print(df2[(df2['Name'].str.contains('Miss', case= False, na= False)) & (df2['Pclass'] == 1)])
