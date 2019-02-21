#s='The column above illustrates apparently' \
#   ' the polularity of people ' \
#   'doing exercise in a certain year ' \
#   'from 2013 to 2018.Based upon the data,' \
#   'we can see that python is wonderful. ' \
#   'python is wonderful. Python ' \
# 对这段文字中的单词进行数字统计，并且进行个数升序
#字符串
s='The column above illustrates apparently' \
  ' the polularity of people ' \
  'doing exercise in a certain year ' \
  'from 2013 to 2018.Based upon the data,' \
  'we can see that python is wonderful. ' \
  'python is wonderful. Python ' \
#创建字典
zi={}
#切割字符串
s=s.split(" " or "," or ".")
#输出查看
print(s)
#循环遍历列表
for i in s:
    #加入字典
    zi[i]=len(i)
#输出字典
print(zi)
#创建数轴
key=[]
val=[]
#遍历字典
for i in zi:
    #添加进新建的数组
    key.append(i)
    val.append(zi[i])
#输出建和值的列表
print(key)
print(val)
#将值列表排序
val.sort()
#创建新字典
nzi={}
#循环进行排序
for i in range(len(key)):
    #循环遍历键列表
    for j in key:
        #如果长度与排序好的值列表元素相同name就将值放进字典
        if val[i]==len(j):
            nzi[j]=val[i]
#最终输出
print("最终结果",nzi)