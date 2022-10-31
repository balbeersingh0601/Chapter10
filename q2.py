s= input("Enter the input")
str=""
l=len(s)
for i in range(0,l):
    if(s[i]=='a' or s[i]=='e'or s[i]=='i'or s[i]=='o'or s[i]=='u'):
       str = str + '*'
    else:
        str = str + s
print("Final string",str)