str1='PYTHON'
str2=''
for i in range(len(str1)-1,-1,-1):
    str2+=str1[i]
print(str2)
'''Using lists:
a=len(str1)
reverse=[]
for i in range(a-1,-1,-1):
    reverse.append(str1[i])
str2=''.join(reverse)
print(str2)'''
