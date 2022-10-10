#print range the number of amstrong number
m = int(input("enter the starting number:"))
n = int(input("enter the ending number:"))
count = 0
for i in range(m,n+1):
    t = 0
    z = i
    #print(i)
    while(i>0):
        #print("x = ",x)
        tem = i%10
        i = i//10
        s = tem**3
        t = s+t
        #print("t = ",t)
        #print('***********')
    if(z == t):
       print(z,end= " ")
       count = count+1
if(count!=0):
    print("These are amstrong number between",m,"and",n)
else:
    print("There is no amstrong number between",m,"and",n)
