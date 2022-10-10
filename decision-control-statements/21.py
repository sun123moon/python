#write program to test given number is a power of 2
n = int(input("enter the number:"))
m = n
i = 0
c = 0
while(n!=2):
    i = n%2
    n = n/2
    if(i!=0):
        print("The number is not power of 2",m)
        c = c+1
        break
    if(n==2):
        print("The number is power of 2",m)
