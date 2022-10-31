s= input("Enter the input")
str=""
l=len(s)
count=0
for i in range(0,l):
    if(s[i]=='a' or s[i]=='e'or s[i]=='i'or s[i]=='o'or s[i]=='u'):
       count+=1
print("The no. of vowels in the string are",count)