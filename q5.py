dig = 0
str =input("Enter a string")
length= len(str)
digits="0123456789"
test=False
print("The original string are",str)
for i in str:
     if i in digits:
        dig = dig+int(i)
        print(i)
        test=True
print("Sum of digits",dig)
if test == False:
    print(str,"has no digits")

