#program for printing prime number and composite number
n = int(input("enter the starting number:"))
m = int(input("enter the ending number:"))
print("prime number  \t   composite number \t  neither prime nor composite number")
print("*"*78)
count = 0
for i in range(n,m+1):
    count = 0
    for z in range(1,i+1):
        num = i%z
        if(num==0):
            count = count+1
    if(count==2):
        print(" "*3,i," "*17, "-"*6," "*30,"-"*7)
    elif(count==1):
        print("-"*5," "*17,"-"*6," "*32,   i    )
    else:
        print("-"*5," "*17," "*2,i," "*32,"-"*7)
print("#"*78)
