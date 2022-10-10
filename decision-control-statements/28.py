'''write a program that accepts the current date and
the date of birth of the user.Then calculate the age of the user
and display on its screen.Note that the date should be displayed
in the format specified as -dd/mm/yy.'''
c_d =int(input("enter the current date:"))
c_m = int(input("enter the current month:"))
c_y =int(input("enter the current year:"))
u_d = int(input("enter user date of date of birth:"))
u_m = int(input("enter user month of date of birth:"))
u_y = int(input("enter user year of date of birth:"))
print("-"*30)
x = c_y-u_y
if(u_m<=c_m):
    if(u_d<c_d):
        x = x-1
        print("The age of the user is",x)
else:
    print("The age of the user is",x)
print("The \"date of birth\" of the user is","\n","*"*5,u_d,"\\",u_m,"\\",u_y,"*"*5)
print("-"*30)
