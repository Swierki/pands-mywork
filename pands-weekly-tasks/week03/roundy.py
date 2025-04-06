# rounds a number
#  that prompts the user to enter a float, rounds it to the nearest integer, and then prints the result
# Author: Lukasz Swierkowski

# Prompt the user to enter a float number
number = float(input("Enter a float number: "))

# Round the number to the nearest integer
rounded_number = round(number)

# Print the rounded result
print(f"{number} rounded is {rounded_number}")