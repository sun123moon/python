#program for finding of gcd of two number
num1 = int(input("enter the dividend number:"))
num2 = int(input("enter the divisor number:"))
dividend = num1
divisor = num2
while(num1!= 0):
    remainder = num2%num1
    num2 = num1
    num1 = remainder
print("gcd of",dividend,"and",divisor,"is:",num2) 
