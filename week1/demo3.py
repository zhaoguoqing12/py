import random
list=[]
list1=[]
for i in range(20):
    list.append(random.randrange(1,100))
print("列表是:",list)
for j in range(len(list)):
    if(j%2==0):
        list1.append(list[j])
        list1.sort(reverse=True)
print("降序：",list1)
for m in range(10):
    list[m*2]=list1[m]
print("降序列表是:",list)



