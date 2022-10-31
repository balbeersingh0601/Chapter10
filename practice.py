#13
'''s= input("Enter the input")
count=0
l=len(s)
for i in range(0,l):
    if(s[i]=='a' or s[i]=='e'or s[i]=='i'or s[i]=='o'or s[i]=='u'):
       count+=1
print("The no. of vowels are",count)

'''

s= input("Enter the input")
count=1
l=len(s)
for i in range(0,l):
    if(s[i]==' '):
        count+=1
print("The no. of words are",count)
'''


s= input("Enter the input") # ---valid input of phone no. or not
print(s[0:3],"-",s[3:6],"-",s[6:10])

s= input("Enter the input")
str = ""
l=len(s)
for ch in s:
    if ch>='a'and ch<='z':
        str =str + s.upper()

print(str)
'''



