while True:
    m = input("enter the string:")
    s = " "
    count = 0
    if(m=="quit"):
        break
    for i in m:
        count = count+1
    print(count,m)
