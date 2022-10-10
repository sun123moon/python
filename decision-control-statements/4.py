'''write a program that determines whether a digit,uppercase,
or a lower case character enetered'''
m = input("enter the character:")
if(m.isdigit()):
    print("digit")
if("A"<=m<="Z"):
    print("uppercase")
if("a"<=m<="z"):
    print("lowercase")
