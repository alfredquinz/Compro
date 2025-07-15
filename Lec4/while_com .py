keep_going = 'y'
while keep_going == 'y':
    sale = float(input("Enter amount of sale: "))
    com_rate = float(input("Enter commission rate: "))
    commission = sale * com_rate
    print(f"Commission is: {commission:.2f}")
    keep_going = input("Do you want to continue? (y/n): ")