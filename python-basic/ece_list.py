while True:
    c = input("enter the file name:")
    f = open(c, "a")
    x = input("enter the name:")
    y = input("enter the rollno:")
    z = input("enter your address:")
    w = input("enter your mobile no:")
    a = input("ente your e-mail id:")
    b = input("enter the \"1\" ")
    lines = ["Name: ",x,"\n","Roll no: ",y,"\n","Adress: ",z,"\n","Mobile no:",w,"\n","E-mail id: ",a,"\n","******","\n"]
    f.writelines(lines)
    if b == "quit":
        f.close()
        break
