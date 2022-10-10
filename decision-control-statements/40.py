n = int(input("enter the number:"))
for i in range(1,n+1):
    print("*",end=" ")
    if(i==1 or i==n):
        for j in range(1,n-1):
            print("*",end=" ")
        print("*")
    elif(i>=2):
        if(i!=n):
            for z in range(1,n+1):
                if(z!=n):
                    print(end=" ")
                if(z==(n-1)):
                    print((n-4)*" ","*")

    #print()
