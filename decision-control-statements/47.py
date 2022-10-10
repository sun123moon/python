c = 0
n = int(input("enter the number:"))
for i in range(1,n):
    for j in range(i+c):
        z = i-j
        if(z<=0):
            y = m+1
            z = y
            print(y,end=" ")
        else:
            print(z,end=" ")
        m = z
    print(" ")
    c = c+1
