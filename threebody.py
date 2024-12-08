# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 00:08:08 2024

@author: joahb
"""

import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 4 * np.pi**2  # Gravitational constant in AU^3 / (yr^2 * Msun)
Ms = 1            # Sun's mass in solar masses
ME = 3e-6         # Earth's mass in solar masses
MJ = 0.001        # Jupiter's mass in solar masses
AU = 1            # 1 Astronomical Unit
t_max = 40        # Simulation time in years
dt = 0.002        # Time step in years

# Initial positions (in AU)
xE, yE = 1, 0
xJ, yJ = 5.2, 0
xS, yS = 0, 0  # Placeholder, will adjust based on COM

# Initial velocities (in AU/year)
vxE, vyE = 0, 2 * np.pi
vxJ, vyJ = 0, 2 * np.pi * xJ / 12
vxS, vyS = 0, 0  # Placeholder, will adjust based on momentum conservation

# Calculate center of mass
x_cm = (Ms * xS + ME * xE + MJ * xJ) / (Ms + ME + MJ)
y_cm = (Ms * yS + ME * yE + MJ * yJ) / (Ms + ME + MJ)
xS -= x_cm
xE -= x_cm
xJ -= x_cm
yS -= y_cm
yE -= y_cm
yJ -= y_cm

# Adjust Sun's initial velocity using momentum conservation
vxS = -(ME * vxE + MJ * vxJ) / Ms
vyS = -(ME * vyE + MJ * vyJ) / Ms

# Arrays to store results
steps = int(t_max / dt)
xE_vals, yE_vals = np.zeros(steps), np.zeros(steps)
xJ_vals, yJ_vals = np.zeros(steps), np.zeros(steps)
xS_vals, yS_vals = np.zeros(steps), np.zeros(steps)

# Simulation loop
for i in range(steps):
    # Distances
    rE = np.sqrt((xE - xS)**2 + (yE - yS)**2)
    rJ = np.sqrt((xJ - xS)**2 + (yJ - yS)**2)
    rEJ = np.sqrt((xE - xJ)**2 + (yE - yJ)**2)

    # Accelerations
    axE = -G * Ms * (xE - xS) / rE**3 + G * MJ * (xJ - xE) / rEJ**3
    ayE = -G * Ms * (yE - yS) / rE**3 + G * MJ * (yJ - yE) / rEJ**3
    axJ = -G * Ms * (xJ - xS) / rJ**3 + G * ME * (xE - xJ) / rEJ**3
    ayJ = -G * Ms * (yJ - yS) / rJ**3 + G * ME * (yE - yJ) / rEJ**3
    axS = -G * ME * (xS - xE) / rE**3 - G * MJ * (xS - xJ) / rJ**3
    ayS = -G * ME * (yS - yE) / rE**3 - G * MJ * (yS - yJ) / rJ**3

    # Update velocities
    vxE += axE * dt
    vyE += ayE * dt
    vxJ += axJ * dt
    vyJ += ayJ * dt
    vxS += axS * dt
    vyS += ayS * dt

    # Update positions
    xE += vxE * dt
    yE += vyE * dt
    xJ += vxJ * dt
    yJ += vyJ * dt
    xS += vxS * dt
    yS += vyS * dt

    # Store positions
    xE_vals[i], yE_vals[i] = xE, yE
    xJ_vals[i], yJ_vals[i] = xJ, yJ
    xS_vals[i], yS_vals[i] = xS, yS

# Plot results
plt.figure(figsize=(10, 10))
plt.plot(xE_vals, yE_vals, label="Earth's Orbit")
plt.plot(xJ_vals, yJ_vals, label="Jupiter's Orbit")
plt.plot(xS_vals, yS_vals, label="Sun's Orbit")
plt.scatter(0, 0, color='orange', label='Initial Sun Position', s=100)
plt.scatter(5.2, 0, color='red', label='initial jupiter position', s=100)
plt.xlabel("x (AU)")
plt.ylabel("y (AU)")
plt.title("Full Three-Body Problem: Orbits of Earth, Jupiter, and the Sun")
plt.axis('equal')
plt.legend()
plt.grid()
plt.show()
