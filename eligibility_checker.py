# Ask for the person's age
age = int(input("Enter your age: "))

# If they are under 18, also ask for parental consent
if age < 18:
    consent = input("Do you have parental consent? (yes/no): ").lower()
    
    # Condition 1: Members must be 13 or older AND have parental consent if under 18
    if age >= 13 and consent == "yes":
        print("Welcome to the club!")
    else:
        print("Sorry, you are not eligible yet.")
        
# Condition 2: Anyone 18 or older does not need consent
else:
    print("Welcome to the club!")