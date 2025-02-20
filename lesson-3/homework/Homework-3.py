# Homework-3
#https://www.w3resource.com/python-exercises/dictionary/

#2

dict = {1:10,2:20}

dict[3] = 30
print(dict)

#3
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}

dic4 = {}

for d in (dic1, dic2, dic3):
    dic4.update(d)
print(dic4)

