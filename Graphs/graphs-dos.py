#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 20:43:00 2024

@author: amanda
"""

import matplotlib.pyplot as plt
import numpy as np

# Specify the file path
file = '../../1T/1T-final/dos/MoTe2.dos.dat'

# Initialize lists to store data 
energy_ev = []
dos_e = []


# Read the data from the file B
with open(file, 'r') as file:
    # Skip the header line
    header = file.readline()

    # Read the remaining lines
    for line in file:
        # Split the line into values
        values = line.strip().split()

        # Convert values to appropriate data types
        energy = float(values[0])
        dos = float(values[1])

        # Append values to lists
        energy_ev.append(energy)
        dos_e.append(dos)
        

# Plotting energy vs. dos
plt.plot(energy_ev, dos_e, color='royalblue', linewidth =1.2, label='DOS')
 # Adding Fermi level line to the plot
plt.axvline(1.8069, color='r', linewidth =1, linestyle='--', label='Fermi Level')


# Adding labels and title
plt.xlabel('Energy [eV]')
plt.ylabel('DOS [E]')

# Adding grid
plt.grid(True)

# Displaying legend
plt.legend()

plt.savefig('1T-DOS.png', dpi=(250), bbox_inches='tight')

# Show the plot
plt.show()