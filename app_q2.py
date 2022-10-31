#(a)
y = str(123)
x = "hello" * 3
print(x, y)
x = "hello" + "world"
y = len(x)
print(y, x)
#(b)
x = "hello" + \
    "to Python" + \
    "world"
for char in x :
    y = char
print(y, ' : ', end=' ')
#(c)
x = "hello world"
print(x[ :2], x[ :-2], x[-2: ])
