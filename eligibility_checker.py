# Ask for the person's age
age = int(input("Enter your age: "))

# If they are under 18, also ask "Do you have parental consent? (yes/no)"
# We set a default value of "no" so the compound condition works for adults too
consent = "no"
if age < 18:
    consent = input("Do you have parental consent? (yes/no): ").lower()

# Condition 1: Anyone 18 or older does not need consent (uses OR)
# Condition 2: Members must be 13 or older AND have parental consent if under 18 (uses AND)
# Combined into a single compound condition using both OR and AND
if (age >= 18) or (age >= 13 and consent == "yes"):
    print("Welcome to the club!")
else:
    print("Sorry, you are not eligible yet.")