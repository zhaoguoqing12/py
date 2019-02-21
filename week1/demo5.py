s='The column above illustrates apparently' \
  ' the polularity of people ' \
  'doing exercise in a certain year ' \
  'from 2013 to 2018.Based upon the data,' \
  'we can see that python is wonderful. ' \
  'python is wonderful. Python '
zi={}
for i in s:
    if not(i in zi):
        zi[i]=1
    else:
        zi[i]+=1
print(zi)