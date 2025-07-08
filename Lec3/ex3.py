h = int(input("Enter the number of hours worked: "))
r = int(input("Enter the hourly pay rate: "))
if h<=40:
    money = h * r
elif h > 40:
    money = (40 * r) + ((h - 40) * (r * 1.5))
print(f"Total pay: {money:.2f}")