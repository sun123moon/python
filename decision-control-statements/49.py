print("The movie CD cost :\n1.New movie = 75 per day \n2.Old movie = 50 per day")
print(40*"*")
n = int(input("enter the number of New movies:"))
m = int(input("enter the number of Old movies:"))
o = int(input("enter the number days for rent:"))
print(40*"*")
print("--------------- BILL ----------------")
if(n>=1):
    x = 75*o*n
    print("cost of New Movies:",x)
if(m>=1):
    y = 50*o*n
    print("cost of Old movies:",y)
print("The Total cost of the movies:",x+y)
print("-------------- THANK YOU --------------")
print("---------------VISIT AGAIN -------------")
