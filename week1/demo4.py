import random
str="abcdefghijklmnopqrstuvwsyz"
str1=""
list=[]
zi={}
for i in range(1000):
    str1=random.choice(str)
    list.append(str1)
for j in list:
    if not(j in zi):
        zi[j]=1
    else:
        zi[j]+=1
print(zi)