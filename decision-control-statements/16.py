'''wite a program that display oxford university press
   a.oxford university press
   b.OXFORD UNIVERSITY PRESS
   C.oXFORD uNIVERSITY pRESS'''
m = input("enter the string:")
x=0
for i in m:
    i = m[x].lower()
    print(i,end="")
    x = x+1
y=0
print()
for i in m:
    i = m[y].upper()
    print(i,end="")
    y = y+1
