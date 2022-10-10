#write the program to print the month and day
startday = int(input("enter the starting day of month(1-7):"))
num_of_day = int(input("enter number of days :"))
print("sun mon Tue Wed Thurs fri sat")
print(30*"-")
for i in range(startday):
    print(end = "    ")
for j in range(1,num_of_day+1):
    if(i>6):
        print()
        i = 1
    else:
        i = i+1
    print(str(j) + " ",end = "  ")
