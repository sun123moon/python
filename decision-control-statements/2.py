'''write a program that prompts users to enter a charcter (O,A,B,C,F).
then using if-elif-else construct display outstanding very good good average
and fail respectibvely'''
print("Please enter these character only O,A,B,C,F:")
x  = input("enter the character:")
x = x.upper()
print(x)
if(x=="O"):
    print("outstanding")
elif(x=="A"):
    print("very Good")
elif(x=="B"):
    print("Good")
elif(x=="C"):
    print("average")
else:
    print("Fail")
