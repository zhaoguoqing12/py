a=[1,5,3,4,9,8,7]
b=[]
for i in a:
    if not(b in a):
        b.append(i)
b.sort(reverse=True)
print(b)