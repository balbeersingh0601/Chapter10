testStr="abcdefghi"
testStr1="abcdefghi"
inputStr=input("Enter the integer")
inputInt = int(inputStr)
count=2
newStr = ''
while count <= inputInt:
    newStr = newStr + testStr[0:count]
    testStr = testStr[2:] #Line1
    count = count +1
print(newStr) #Line2
print(testStr) #Line3
print(count) # Line4
print(inputInt) # Line5