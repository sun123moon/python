#write a  program to calculate electricity bill based on following information
m = int(input("enter the electricity units used by you:"))
print("*"*26)
if(m<=150):
    print("Electricity Bill =",m*3)
elif(151<=m<=350):
    print("Electricity Bill =",100+(m*3.75))
elif(451<=m<=600):
    print("Electricity Bill =",300+(m*4.25))
else:
    print("Electricity Bill =",400+(m*5))
print("*"*26)
