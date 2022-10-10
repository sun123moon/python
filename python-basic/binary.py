decimal_number = int(input("enter the decimal_number:"))
binary_number = 0
i = 0
while(decimal_number!=0):
    remainder = decimal_number%2
    pow1 = pow(10,i)
    remainder1 = remainder*pow1
    binary_number = binary_number+remainder1
    decimal_number = decimal_number//2
    i = i+1
print("The binary_number is:",binary_number)
