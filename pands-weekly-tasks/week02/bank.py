# bank.py
# Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
# Author: Lukasz Swierkowski

# bank.py

# Prompt the user to enter two amounts in cents
amount1 = int(input("Enter amount1 (in cent): "))
amount2 = int(input("Enter amount2 (in cent): "))

# Add the two amounts together
total_cents = amount1 + amount2

# Convert the total cents to euros and cents
euros = total_cents // 100  # Get the whole euro part
cents = total_cents % 100   # Get the remaining cents part

# Print the result in the required format
print(f"The sum of these is €{euros}.{cents:02d}")
