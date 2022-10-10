#write a program to calculate the sum of numbers from m to n.
m = int(input("enter the number of m:"))
n = int(input("enter the number of n:"))
s = 0
if(m<n):
    while(m<=n):
        #print(s,"+",m,"=",s+m)
        s = s+m
        m = m+1

else:
    while(n<=m):
        #print(s,"+",m,"=",s+m)
        s = s+m
        m = m-1
print("sum",s)
