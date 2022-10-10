'''write a program to read two numbers.Then find out whether the
first number is a multiple of the second number.'''
m = int(input("enter the multiple number:"))
n = int(input("enter the second number:"))
y = m%n
if(y==0):
    print("The first number is multiple of second numbers")
else:
    print("The first number is not multiple of second number")
