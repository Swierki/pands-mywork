# Program that takes a positive floating-point number as input and outputs an approximation of its square root.
# Author: Lukasz Swierkowski
# References: Newton's Method: https://en.wikipedia.org/wiki/Newton%27s_method
# References: Python documentation on string formatting: https://docs.python.org/3/library/string.html#format-specification-mini-language
# References: Python documentation on loops: https://docs.python.org/3/tutorial/controlflow.html#while-statements

def sqrt(x):
    # First check if the number is positive
    if x < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    
    guess = 0  # Start from number 0
    step = 0.0001  # A small step to increment the guess
    
    # Keep increasing the guess in small steps until the square of guess is close enough to x
    while guess * guess < x:
        guess += step
    
    return guess

def main():
    try:
        # Enter the number only positive accepted
        number = float(input("Enter a positive floating-point number: "))
        if number <= 0:
            print("Please enter a positive number.")
        else:
            # Calculate the square root using our custom sqrt function
            result = sqrt(number)
            print(f"The approximate square root of {number} is {result:.4f}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
