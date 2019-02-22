zi={1:2,5:3,4:3}
a=sorted(zi.items(),key=lambda x:x[0],reverse=True)
li=dict(a)
print(li)