# to find length
string ="Anushka"
print("Length of the String",len(string))

# Printing a string
l = len(string)
print(string[0])
print(string[l-1])
for i in range(0,l):
    print(string[i],end =" ")
#print("-----------------------------------------------------------------------------------------------")

# Reversing string
l = len(string)
print("Length of the String",len(string))
for i in range((l-1),-1,-1):
    print(string[i],end =" ")

# Traverse a string
for ch in string:
    print(ch,"-", end=" ")
'''
  
'''
