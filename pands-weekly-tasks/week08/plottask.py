# Program thats displays:
# 1. a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2,
# 2. and a plot of the function  h(x)=x3 in the range 0 to 10, on the one set of axes.

import numpy as np
import matplotlib.pyplot as plt

def main():
    # Create 1000 random values from a normal distribution with mean=5 and std=2
    data = np.random.normal(5, 2, 1000)

    # Create a range of x values for plotting h(x) = x^3
    x = np.linspace(0, 10, 1000)
    y = x**3

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot the histogram of the normal distribution
    ax.hist(data, bins=30, alpha=0.6, color='g', label='Normal Distribution')

    # Plot the function h(x) = x^3
    ax.plot(x, y, color='b', label='h(x) = x^3')

    # Add labels and title
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Histogram of Normal Distribution and Function h(x) = x^3')

    # Add a legend
    ax.legend()

    # Show the plot
    plt.show()

    # Save the plot as a PNG image
    fig.savefig('plottask_output.png')

if __name__ == "__main__":
    main()
