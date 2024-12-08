# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 00:00:28 2024

@author: joahb
"""

import numpy as np
import matplotlib.pyplot as plt


# Constants
G = 4 * np.pi**2  # Gravitational constant in AU^3 / (yr^2 * Msun)
Ms = 1            # Mass of the Sun in solar masses
AU = 1            # 1 Astronomical Unit
t_max = 5         # Simulation time in years
dt = 0.002        # Time step in years

# Initial conditions
x, y = AU, 0      # Initial position in AU
vx, vy = 0, 2 * np.pi  # Initial velocity in AU/year

# Arrays for storing results
steps = int(t_max / dt)
x_vals, y_vals = np.zeros(steps), np.zeros(steps)

# Simulation using Euler-Cromer method
for i in range(steps):
    r = np.sqrt(x**2 + y**2)
    ax, ay = -G * Ms * x / r**3, -G * Ms * y / r**3  # Acceleration

    # Update velocity
    vx += ax * dt
    vy += ay * dt

    # Update position
    x += vx * dt
    y += vy * dt

    # Store position
    x_vals[i], y_vals[i] = x, y

# Plot results
plt.figure(figsize=(8, 8))
plt.plot(x_vals, y_vals, label="Earth's Orbit")
plt.scatter(0, 0, color='orange', label='Sun', s=100)  # Sun at the origin
plt.xlabel("x (AU)")
plt.ylabel("y (AU)")
plt.title("Two-Body Problem: Earth's Orbit Around the Sun")
plt.axis('equal')
plt.legend()
plt.grid()
plt.savefig("two_body_orbit.png")
plt.show()
