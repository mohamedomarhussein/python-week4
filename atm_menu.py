# Start with a balance in your code
balance = 1000
# Choose a correct PIN
correct_pin = "1234"

# Ask the user for a 4-digit pin
pin = input("Enter your 4-digit PIN: ")

# If the PIN is wrong, print "Incorrect PIN" and stop
if pin != correct_pin:
    print("Incorrect PIN")
else:
    # If the PIN is correct, ask how much they want to withdraw
    withdraw_amount = int(input("Enter amount to withdraw: "))
    
    # Inside that decision: if the amount is less than or equal to the balance...
    if withdraw_amount <= balance:
        # print the new balance
        new_balance = balance - withdraw_amount
        print(f"Withdrawal successful. Your new balance is: {new_balance}")
    else:
        # otherwise print "Insufficient funds"
        print("Insufficient funds")