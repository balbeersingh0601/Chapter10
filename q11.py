s=input("Enter a string")
#s="I love my country India 12310"
length= len(s)
slist=s.split(' ')
for i in slist:
    count= count+1
print("No. of words are",count)