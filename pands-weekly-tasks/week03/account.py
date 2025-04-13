# accounts.py
# Bank account numbers can stored as 10 character strings, for security reasons some applications only display the last 4 characters (with the other other characters replaced with Xs)
# Author: Lukasz Swierkowski

# use the function input to enter numbers of the account

account_number = input("Please enter a 10 digit account number: ")

# Check if input is valid (10 digits and all numbers) use the command length to confirm it has 10 digits in order.

 Check if input is valid (10 digits and all numbers)

if len(account_number) == 10 and account_number.isdigit():
    # Mask the first 6 digits define what is masked 

    masked = "X" * 6 + account_number[-4:]
    print(masked)

else:
    print("Invalid input. Please enter exactly 10 digits.")