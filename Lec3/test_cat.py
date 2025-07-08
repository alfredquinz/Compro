inchar = input("Input your character: ")
if inchar >= 'A' and inchar <= 'Z':
    print("Upper case letter", inchar)
elif inchar >= 'a' and inchar <= 'z':
    print("Lower case letter", inchar)
elif inchar >= '0' and inchar <= '9':
    print("Number", inchar)
else:
    print("Special character", inchar)