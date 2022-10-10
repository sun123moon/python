'''write program that prompts users to enter numbers.
once the user enters -1, it displays the count,sum and average
of even numbers and that of odd numbers'''
c_o = 0
c_e = 0
s_o = 0
s_e = 0
while True:
    n = int(input("enter the numbers:"))
    if(n==-1):
        print("average of even:",s_e/c_e)
        print("average of odd:",s_o/c_o)
        break
    elif(n%2==0):
        s_e = n+s_e
        c_e = c_e+1
    else:
        s_o = n+s_o
        c_o = c_o+1
