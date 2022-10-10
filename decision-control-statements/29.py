'''write a program that displays all the number
from 1-100 that are not divisible by 2 as well as by 3'''
for i in range(1,100):
    if(i%3!=0 and i%2!=0):
        print(i,end=" ")
print("These number are not divisble with 2,3")
#for i in range(1,100):
    #x = i%2
    #y = i%3
    #if(x==y!=1):
        #print(i,end=" ")
