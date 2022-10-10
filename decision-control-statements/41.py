for i in range(1,6):
    for j in range(1,6):
        if(i==j):
            print("$",end=" ")
        elif(i>j and j==1):
            print("*",end=" ")
        elif(i==1 and j>i):
            print("*",end=" ")
        elif(i==5 and i>j):
            print("*",end=" ")
        elif(i<j or i>j):
            print(end=" ")
        elif(j==5 and j>i):
            print("  *")
    print()
