# Palindrome1
'''n = input("Enter a string")
if (n==n[::-1]): #using STRING SLICES
    print(n,"is a Palindrome")
else:
    print(n,"is NOT a Palindrome")
'''
# Pallindrome 2
str= input("Enter the string")
l= len(str)
mid = l//2
rev = -1
for i in range(mid):
    if (str[i]== str[rev]):
        i+=1
        rev-=1
    else:
        print(str, "is not palindrome")
        break
else:
        print(str,"is palindrome")


