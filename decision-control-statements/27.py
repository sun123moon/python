#write program to read an angle from the user and then display its quardant
m = int(input("enter the angle:"))
print("-"*35)
if(0<=m<=90):
    print("The angle is in 1 st quardant",m)
if(90<m<=180):
    print("The angle is in 2 nd quardant",m)
if(180<m<=270):
    print("The angle is in 3 rd quardant",m)
if(270<m<=360):
    print("The angle is in 4 th quardant",m)
if(m>360):
    print("Enter below 360 or 360 Degress")
print("-"*35)
