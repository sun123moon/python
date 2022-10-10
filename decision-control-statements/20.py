'''write aporgram to print the prime factors of a number'''
n = int(input("enter the number to find a prime factor number:"))
count = 0
for i in range(1,n+1):
    if(n%i==0):
        print(i,end=",")
        count = count+1
print("These are the prime factors of",n)
