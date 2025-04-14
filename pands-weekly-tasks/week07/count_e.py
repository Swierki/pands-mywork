# Program that reads in a text file and outputs the number of e's it contains
# Author: Lukasz Swoierkowski
# References: https://docs.python.org/3/library/sys.html#sys.argv

import sys
import os

def count_e_in_file(filename):
    try:
        # Open the file for reading
        with open(filename, 'r') as file:
            content = file.read()
            
        # Count occurrences of 'e' and 'E'
        count = content.lower().count('e')
        return count
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        sys.exit(1)
    except IsADirectoryError:
        print(f"Error: '{filename}' is a directory, not a file.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    # Check if the user has provided the filename as a command-line argument
    if len(sys.argv) != 2:
        print("Error: Please provide a filename as a command-line argument.")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    # Check if the file exists and is a text file
    if not os.path.isfile(filename):
        print(f"Error: '{filename}' is not a valid file.")
        sys.exit(1)
    
    # Count the occurrences of 'e' in the file
    e_count = count_e_in_file(filename)
    
    # Output the result
    print(f"The number of 'e' characters in '{filename}' is: {e_count}")

if __name__ == "__main__":
    main()
