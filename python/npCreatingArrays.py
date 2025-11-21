# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 12:37:56 2025

@author: Phoenix
"""

import numpy as np

# Arrays of zeros
growth_data = np.zeros(10)
print("Zeros:", growth_data)

# Arrays of ones
mask = np.ones(5)
print("Ones:", mask)

# Range of values (start, stop, step)
time = np.arange(0, 60, 10)  # 0 to 60 minutes, step=10
print("Time points:", time)

# Evenly spaced values (start, stop, count)
temps = np.linspace(900, 1100, 5)  # 5 temps from 900 to 1100
print("Temperature range:", temps)

# Identity matrix
identity = np.eye(3)
print("\nIdentity matrix:")
print(identity)

# Random arrays
np.random.seed(42)
random_diameters = np.random.uniform(40, 60, 10)
print("\nRandom diameters:", random_diameters.round(2))

# Normal distribution (mean=50, std=5)
gaussian_sizes = np.random.normal(50, 5, 100)
print("Gaussian mean:", gaussian_sizes.mean().round(2))
print("Gaussian std:", gaussian_sizes.std().round(2))