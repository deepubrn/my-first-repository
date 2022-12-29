# Fibonacci series for n- terms
num = int(input("enter num for term = "))
a = int(0)
b = int(1)
for i in range(num):
    c = a + b
    b = a
    a = c
    print(c, end=(" "))



