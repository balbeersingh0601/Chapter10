s = input("Enter a string")
#s= "my name is deepika"
slist=s.split(' ')
print(slist)
str=""
for i in slist:
    a = len(i)
    str = i
    for j in range(a-1,-1,-1):
        print(str[j],end="")
    print()
