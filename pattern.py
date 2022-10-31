# Pattern
'''for i in range(10):
    print(i*"#")
print()

#BOOK ka Pattern
string="#"
pattern=""
for a in range(5):
    pattern +=string
    print(pattern)
s = "hello123"
sum=0
for a in s:
    if a.isdigit():
        sum = sum +int(a)
print(sum)
count = 0
count1 = 0
s = input("Enter the input")
for a in s:
    if a >= "A" and a<="Z":
        count+=1
    elif a >="a" and a<="z" :
        count1 +=1
print("Uppercase leters are",count)
print("Lowercase letters are",count1)

count = 0
count1 = 0
s = input("Enter the input")
for a in s:
    if a.isupper():
        count+=1
    elif a.islower():
        count1 +=1
print("Uppercase leters are",count)
print("Lowercase letters are",count1)
'''
s = input("Enter the input")
sub = s.split(" ")
print(sub)
for a in sub:
    print(a,"(",len(a),")")

