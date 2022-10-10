num = int(input("enter the number:"))
s = 0
t = 0
q = num
while(num>0):
    tem = num%10
    num = num//10
    s = tem**3
    t = s+t
if(0<q<=9):
    print(q,"is amstrong number")
elif(q == t):
    print(t,"is amstrong number")
else:
    print(q,"is not amstrong number")
