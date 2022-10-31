count=0
count1=0
s=input("Enter a string")
#s="I love my country India 12310"
length= len(s)
slist=s.split(' ')
for i in slist:
    count= count+1
print("No. of words are",count)
print("No. of characters are",length)
for j in s:
    if (j>='A' and j<='Z')or (j>='a' and j<='z') or (j>='0' and j<='9'):
        count1=count1+1
print("The no. of alpha numeric", count1)
p = count1/length
print("Percentage of alpha numeric characters are",p*100)