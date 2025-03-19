# Get user input
salary = float(input("Enter your salary: "))
years= int(input("Enter your years of service: "))


if years > 5:
    bonus = 0.05 * salary
    print(f"You receive a bonus of: {bonus:.2f}")
else:
    print("You are not eligible for a bonus.")
