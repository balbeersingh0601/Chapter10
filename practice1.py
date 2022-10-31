count=0
str= "jngle bells jingle bells"
sub= "bells"
if sub in str:
    count = count+1
print("No. of lines :",sub," occured ",count)
'''
s= input("Enter ur email-id")
sub = "@gmail.com"
if sub in s:
    if(len(s)!=len(sub)):
        print("correct email-id")
    else:
        print('U entered the domain name only')
else:
    print("incorrect")
'''
s3=" "
s1= input("Enter string 1")
s2= input("Enter string 2")
print("Original String ",s1,s2)
if s1 in s2:
    s3 = "Restore"
print("final string",s3)


