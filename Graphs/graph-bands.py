#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 18:40:50 2024

@author: amanda
"""

import numpy as np
import matplotlib.pyplot as plt

def read_bands(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    bands = []
    current_band = []

    for line in lines:
        if line.strip() == '':
            # Blank line indicates the end of one band and the start of a new one
            if current_band:
                bands.append(np.array(current_band))
                current_band = []
        else:
            data = [float(val) for val in line.split()]
            current_band.append(data)

    if current_band:
        bands.append(np.array(current_band))

    return bands

def plot_bands(bands, fermi_level):
    for band in bands:
        k_points = band[:, 0]
        energies = band[:, 1]
        
        # Substract Fermi level to shift it to zero energy
        energies -=fermi_level
        
        plt.plot(k_points, energies)

    # Adding Fermi level line to the plot
    plt.axhline(2.155, color='r', linestyle='--', label='Fermi Level')

    plt.xlabel('k-points')
    plt.ylabel('Energy (eV)')
    plt.legend()
    #plt.savefig('1T-bands.png', dpi=(250), bbox_inches='tight')
    plt.show()

# Data used
file_path = '../../1T/1T-final/band/MoTe2.bands.dat.gnu'
fermi_level = 2.155  # Fermi level in eV
bands_data = read_bands(file_path)
plot_bands(bands_data, fermi_level)


