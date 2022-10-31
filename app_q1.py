#a
print("""
1
 2
  3
  """)
#b
text = "Test. \n NExt line"
print(text)

#c
print('One''Two'*2)
print('One'+ 'Two'*2)
print(len('0123456789'))

#d
s='0123456789'
print(s[3],",",s[0:3],"-",s[2:5])
print(s[:3],"-",s[3:],",",s[3:100])
print(s[20:],s[2:1],s[1:1])

#e
s='987654321'
print(s[-1],s[-3])
print(s[-3:],s[:-3])
print(s[-100:-3],s[-100:3])