#s = input("Enter a string")
s= "my_sbcjufbdsurbbcurretyewgt name_sehfejbfrnrijgnrg is deepikaeuroep"
slist=s.split(' ')
print(slist)
str=""
largest_len =2
for i in slist:
    print(i , len(i))
    if (largest_len<len(i)):
        largest_len=len(i)
print(largest_len)



