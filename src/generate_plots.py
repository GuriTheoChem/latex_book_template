import matplotlib.pyplot as plt
import numpy as np

def generate_plot_1():
    # Generate sample data
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Plot the data
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, color='blue', linestyle='-')
    plt.xlabel('X-axis label')
    plt.ylabel('Y-axis label')
    plt.title('Sample Plot 1')
    plt.grid(True)
    plt.savefig('src/contents/figures_and_plots/plots/plot1.png')  # Save the plot as an image file
    plt.close()

def generate_plot_2():
    # Generate sample data
    x = np.linspace(-5, 5, 100)
    y = x ** 2

    # Plot the data
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, color='red', linestyle='--')
    plt.xlabel('X-axis label')
    plt.ylabel('Y-axis label')
    plt.title('Sample Plot 2')
    plt.grid(True)
    plt.savefig('src/contents/figures_and_plots/plots/plot2.png')  # Save the plot as an image file
    plt.close()

def main():
    # Generate and save plots
    generate_plot_1()
    generate_plot_2()

if __name__ == "__main__":
    main()
