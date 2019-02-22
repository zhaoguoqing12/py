s=int(input("请输入阶乘数字："))
sum=1
for i in range(s+1):
    sum+=sum*i
print(sum)