import math
phone=input("请输入手机号:")
if(len(phone)==6)and(type(int(phone))==int):
        print("手机号有效")
else:
        print("手机号必须为数字,长度为6")
