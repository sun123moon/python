x = input("enter the file name:")
f = open(x,"r")
for line in f:
    print(line)
f.close()
