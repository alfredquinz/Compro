N1 = int(input("Enter the score for test 1 : "))
N2 = int(input("Enter the score for test 2 : "))
N3 = int(input("Enter the score for test 3 : "))    

average = (N1 + N2 + N3) / 3   
print(f"The average score is: {average:.2f}")

if average >= 95:
    print("Congratulactions!")

