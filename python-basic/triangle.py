n = 10
k = n-1
for i in range(1,n):
    #for k in (1,k+1):
        #print(end=" ")
    print(k*" ",end=" ")
    for j in range(i):
        print("* ",end="")
    print("\r")
    k = k-1
