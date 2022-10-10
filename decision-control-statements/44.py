m = 0
while True:
    try:
        n = int(input("enter the number:"))
        if(m<n):
            m = n
            print("1=",m)
        if(m==0):
            m = n+0
            print("2=",m)
    except:
        break
print("The higest is",m)
