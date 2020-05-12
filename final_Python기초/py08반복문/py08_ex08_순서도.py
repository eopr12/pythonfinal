
a = 1
b = 2
c = a + b # c = 0

while c < 30:
    c = a + b
    a = b
    b = c

print(c)
