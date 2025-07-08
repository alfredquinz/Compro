employees = int(input("Enter the number of employees: "))
if employees < 50:
    print("Small company")
elif employees < 250:
    print("Medium company")
elif employees >= 250:
    print("Large company")