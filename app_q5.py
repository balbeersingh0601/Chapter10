inputStr= input("Give me a string")
bigInt = 0
littleInt = 0
otherInt =0
for ele in inputStr:
    if ele>='a' and ele<='m':
        littleInt=littleInt+1
    elif ele>'m' and ele<='z':
        bigInt = bigInt+1
    else:
        otherInt = otherInt+1

print(bigInt)       #Line2
print(littleInt)    #Line3
print(otherInt)     #Line4
print(inputStr.isdigit())#Line5