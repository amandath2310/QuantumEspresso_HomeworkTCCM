#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 21:38:02 2024

@author: amanda
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colormaps

def read_bands(file_path):
    bands = []
    current_band = []

    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():  # Non-blank line
                # Parse numerical values and append to current_band
                data = [float(value) for value in line.split()]
                current_band.append(data)
            else:  # Blank line indicates end of one band
                if current_band:
                    # Append the current band to bands
                    bands.append(np.array(current_band))
                    current_band = []

        if current_band:
            # Append the last band if there is remaining data
            bands.append(np.array(current_band))

    return bands

def plot_bands(bands, fermi_level, k_point_range=(0, 3)):
    plt.figure(figsize=(10, 6))
    

    for band in bands:
        # Extract k-points and energies from the band data
        k_points = band[:, 0]
        energies = band[:, 1]
        
        # Subtract Fermi level to shift it to zero energy
        energies -= fermi_level

        # Filter k-points between the specified range
        mask = (k_points >= k_point_range[0]) & (k_points <= k_point_range[1])
        k_points = k_points[mask]
        energies = energies[mask]

        # Plot the band
        plt.plot(k_points, energies, color='green')

    # Plot Fermi level as a horizontal dashed line
    plt.axhline(0, color='red', linestyle='--', label='Fermi Level')

    # Set y-axis limits to focus on the desired energy range
    plt.ylim(-4, 4)
    
    # Customize x-axis ticks and labels
    tick_positions = [0, 0.6, 0.75, 1.25, 1.45, 1.90, 2.15, 2.40, 2.70, 2.80, 3]  # Adjust as needed
    tick_labels = [r'$\Gamma$', 'K', 'M',  r'$\Gamma$', 'A', 'H', 'L', 'A', 'H', 'K', r'$\Gamma$']  # Labels for each tick position
    plt.xticks(tick_positions, tick_labels)
    plt.axvline(0, color='royalblue', linewidth =0.8, linestyle='--')
    plt.axvline(0.6, color='royalblue', linewidth =0.8, linestyle='--')
    plt.axvline(0.75, color='royalblue', linewidth =0.8, linestyle='--')
    plt.axvline(1.25, color='royalblue', linewidth =0.8, linestyle='--')
    plt.axvline(1.45, color='royalblue', linewidth =0.8, linestyle='--')
    plt.axvline(1.90, color='royalblue', linewidth =0.8, linestyle='--')
    plt.axvline(2.15, color='royalblue', linewidth =0.8, linestyle='--')
    plt.axvline(2.40, color='royalblue', linewidth =0.8, linestyle='--')
    plt.axvline(2.70, color='royalblue', linewidth =0.8, linestyle='--')
    plt.axvline(2.80, color='royalblue', linewidth =0.8, linestyle='--')
    plt.axvline(3, color='royalblue', linewidth =0.8, linestyle='--')
 
 

    # Add labels, title, legend, and show the plot
    plt.xlabel('k-points')
    plt.ylabel('Energy (eV)')
    plt.legend()
    plt.savefig('2H-bands-filter.png', dpi=250, bbox_inches='tight')
    plt.show()

# Example Usage
file_path = '../2H-final/band/MoTe2.bands.dat.gnu'
fermi_level = 2.1550  # Fermi level in eV
bands_data = read_bands(file_path)
plot_bands(bands_data, fermi_level)
