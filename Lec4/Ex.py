score = int(input("Enter your score: "))
while score <0 and score > 100:
    print("EROR: The should not less than Zero and not More than 100")
    score = int(input("Enter your test score: "))

print("Your score is:", score)