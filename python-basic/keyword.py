#write a program to determine the character entered by the user

char = input('press any keyword:')
if(char.isalpha()):
    print("The user entered character:",char)
if(char.isdigit()):
    print("The user enterd digit:",char)
if(char.isspace()):
    print("The user entered space:",char)

print("only enter the character,or number or space bar like press letter \"A\" or number \"2\" or \"SPACE BAR\" ")
