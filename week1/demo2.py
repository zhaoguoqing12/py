import random
list=[]
#求50随机整数
for i in range(50):
    list.append(random.randrange(-10,10))
print("列表是",list)
zs=[]
fs=[]
#判断正数或者负数
for j in list:
    if(j>0):
        zs.append(j)
    elif(j<0):
        fs.append(j)
print("正数有：",zs)
print("负数有：",fs)