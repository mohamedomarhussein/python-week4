# Week 4 Assignment: Hands-On Lab — Grades, Eligibility & Smart Decisions

- `grade_classifier.py` — Takes a score (0–100) and prints the matching letter grade (A–F) using if/elif/else.
- `eligibility_checker.py` — Checks a user's age and parental consent to decide club eligibility.
- `atm_menu.py` — Simulates an ATM with a PIN check and a nested withdrawal decision.

## When is elif better than several separate if statements?
`elif` is better because Python stops checking the remaining conditions as soon as one matches, 
which makes the program faster and clearer. Using separate `if` statements would force Python 
to evaluate every condition even after a match, which is inefficient and harder to read.