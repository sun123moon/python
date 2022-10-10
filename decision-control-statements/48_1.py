n = input("enter the the number")
c = 0
x = 0
for i in (n):
    c = c + 1
n = int(n)
for j in range(c):
    x = x+1
    n = n%(10**(c-j))
    print(x,j*" ",n)
