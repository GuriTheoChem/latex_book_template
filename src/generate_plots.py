import matplotlib.pyplot as plt
import numpy as np

# Data for Star Trek Captains and Years Served
captains = ['Archer', 'Kirk', 'Picard', 'Sisko', 'Janeway']
years_served = [10, 8, 21, 7, 7]

# Data for Star Trek Planets and Populations
planets = ['Vulcan', 'Kronos', 'Earth', 'Bajor', 'Romulus']
populations = [6, 6, 7, 2, 5]  # Adjusted populations including Romulus
# Custom color scheme
custom_colors = ['#1F77B4', '#FF7F0E', '#2CA02C', '#D62728', '#9467BD', '#8C564B', '#E377C2', '#7F7F7F', '#BCBD22', '#17BECF']

# Create and save plots

# Starfleet Captains and Years Served
plt.figure(figsize=(8, 6))
plt.bar(captains, years_served, color=custom_colors[0:len(captains)])
plt.title('Starfleet Captains and Years Served', fontsize=12)
plt.xlabel('Captains', fontsize=10)
plt.ylabel('Years Served', fontsize=10)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('src/contents/figures_and_plots/plots/captains_and_years_served.png')
plt.close()

# Planets and Populations
plt.figure(figsize=(8, 6))
plt.pie(populations, labels=planets, autopct='%1.1f%%', colors=custom_colors[0:len(planets)], startangle=140)
plt.title('Planets and Populations', fontsize=12)
plt.tight_layout()
plt.savefig('src/contents/figures_and_plots/plots/planets_and_populations.png')
plt.close()

# Constants
speed_of_light = 299792  # Speed of light in kilometers per second

# Define the warp factor formula (a hypothetical formula for demonstration)
def warp_speed(warp_factor):
    return speed_of_light * warp_factor ** 3.0

# Generate warp factors from 1 to 10
warp_factors = np.arange(1, 11, 1)

# Calculate corresponding speeds in terms of the speed of light
speeds_in_c = warp_speed(warp_factors) / speed_of_light

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(warp_factors, speeds_in_c, marker='o', linestyle='-', color=custom_colors[0])
plt.title('Warp Factor vs. Speed in terms of Speed of Light', fontsize=14)
plt.xlabel('Warp Factor', fontsize=12)
plt.ylabel('Speed (times speed of light)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(np.arange(1, 11, 1))  # Set ticks for warp factors 1 to 10
plt.xlim(0.5, 10.5)  # Extend x-axis limits slightly
plt.tight_layout()

# Annotate points with their values
for i, txt in enumerate(speeds_in_c):
    plt.annotate(f'{txt:.2f}', (warp_factors[i], speeds_in_c[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Save and show the plot
plt.savefig('src/contents/figures_and_plots/plots/warp_factor_vs_speed_of_light.png')
plt.close()
