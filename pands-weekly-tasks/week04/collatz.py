# The program that asks the user to input any positive integer and outputs the successive values
# Author: Lukasz Swierkowski

# Rules

# If the number is even, divide it by 2.

# If the number is odd, multiply by 3 and add 1.

# Repeat until the number becomes 1.

def collatz_sequence(n):
    while n != 1:
        print(n, end=' ')
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    print(1)

def main():
    try:
        num = int(input("Please enter a positive integer: "))
        if num > 0:
            collatz_sequence(num)
        else:
            print("That is not a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")

if __name__ == "__main__":
    main()
