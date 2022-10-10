#write a program to print the following program
n = int(input("enter the number:"))
for i in range(1,n):
    for j in range(i):
        print("*",end=" ")
    print("")
for i in range(1,n):
    for z in range(1,(n-i)):
        print("*",end=" ")
    print("")
