#write a program to print the Floyd's triangle
n = int(input("enter the number:"))
print("The Floyd\'s Triangle")
for i in range(n+1):
    for j in range(1,i+1):
        #c = c+1
        print(j,end=" ")
    print()
