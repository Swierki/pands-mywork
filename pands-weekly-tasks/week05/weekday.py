# Write a program that outputs whether or not today is a weekday.
# Author: Lukasz Swierkowski
# References  https://docs.python.org/3/library/datetime.html#datetime.datetime.weekday
# References  https://docs.python.org/3/library/datetime.html

# First import calendar date/time

import datetime

def main():
    # Import the timedate
    now = datetime.datetime.now()

    # Extract the day of the week as an integer (0=Monday, 6=Sunday)
    day_of_week = now.weekday()

    # Mark the days less then 5 weekday when bigger Weekend 5,6 (Monday to Friday)
    if day_of_week < 5:
        print("Ahh it is a weekday.")
    else:
        print("Great is the weekend.")

if __name__ == "__main__":
    main()

