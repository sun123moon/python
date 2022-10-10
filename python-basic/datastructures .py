def supper(password):
    s = 0
    for i in password:
        for j in special_chars:
            if i==j:
                s+=1
    s = s
    print(s)
password = input("enter the password")
special_chars = "#@"
supper(password)
