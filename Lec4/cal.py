max = 5
total = 0.0 
print('This program calculates the sun of')
print(max , 'numbers you will enter.')

for count in range(max):
    number = float(input('Enter number '))
    total =total + number

print('The total is', total)