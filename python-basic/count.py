"""wirte a program to
read the number and also count the negative
positive and zeros entered by the user"""
negative = positive = zeros = 0
print("enter \"a\" to exit")
while True:
    try:
        num = int(input("enter any number:"))
        if(num==0):
            zeros = zeros+1
        elif(num>0):
            positive = positive+1
        else:
            negative = negative+1
    except:
         break
print("count of number of positive number entered:",positive)
print("count of number of negative number entered:",negative)
print("count of number of zeros number entered:",zeros)
