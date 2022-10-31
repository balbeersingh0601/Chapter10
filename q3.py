s= input("Enter the input")
str=""
l=len(s)
for i in range(l-1,-1,-1):
    str = str + s[i]
print("The reversed string is",str)