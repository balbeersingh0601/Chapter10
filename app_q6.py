in1Str= input("Enter string of digits :")
in2Str= input("Enter string of digits :")
if len(in1Str)> len(in2Str):
    small = in2Str
    large = in1Str
else:
    small = in1Str
    large = in2Str
newStr = ''
for element in small:
    result = int(element)+int(large[0])
    newStr = newStr + str(result)
    large = large[1:]
print(len(newStr)) #Line1
print(newStr)       #Line2
print(large)        #Line3
print(small)        #Line4