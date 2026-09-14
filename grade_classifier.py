# Ask the user for a score between 0 and 100
score = int(input("Enter your score (0-100): "))

# First, validate: if the score is below 0 or above 100, print an error message
if score < 0 or score > 100:
    print("Error: Invalid score. Please enter a score between 0 and 100.")
else:
    # Otherwise use if / elif / else to decide the grade
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"
    
    # Print the grade clearly
    print(f"A score of {score} earns grade: {grade}")