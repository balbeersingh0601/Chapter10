s= "TEAM"
l= len(s)
for i in range(0,l):
    print(s[i]*2 ,end='')

s="5690.453"
p = s.partition('.')
print("Decimal part",p[2])
print("Real no part",p[0])
print("Partition part",p[1])

s="VBJSHBVKUEOWNDJEFMKWDKJNF"
print("Codon1",s[0:3])
print("Codon2",s[3:6])
print("Codon3",s[6:9])

print(s.replace('J','@'))

s="i love programming"
print(s.title())