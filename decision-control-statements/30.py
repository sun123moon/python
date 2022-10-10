print("choose your vehicle \n 1.Truck\Bus = B \n 2.Car = C \n 3.Scooter\Motorcycle = S")
n = input("Enter the character of the vehicle:")
print("Enter the entering time in 24 hours format")
h1 = int(input("enter the hours number:"))
m1 = int(input("enter the minutes:"))
print("Enter the leaving time in 24 hours format")
h2 = int(input("enter the hours:"))
m2 = int(input("enter the minutes:"))
if(m1>m2):
    m2 = 60+m2
    h2 = h2-1
    m = m2-m1
else:
    m = m2 - m1
if(h1>h2):
    h = 12-h1
    h = (h2+h)*60
else:
    h = (h2-h1)*60
m = m+h
print("mintues:",m)
h = round(m/60,2)
print("-"*30)
if(n == "B"):
    if(h>3):
        c = h*30
    else:
        c = h*20
    print("Truck/bus fee:",c)
if(n == "C"):
    if(h>3):
        c = h*20
    else:
        c = h*10
    print("Car Fee:",c)
if(n == "S"):
    if(h>3):
        c = h*10
    else:
        c = h*5
    print("Scooter/bike Fee:",h*5)
print("Thank you for using service")
print("****** visit again ******")
print("-"*30)
