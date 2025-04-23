import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parameters for the mass-spring system
n_floors = 5               # Number of floors (masses)
mass = 1.0                  # Mass of each floor
k = 10.0                   # Spring constant
damping = 0.2              # Damping factor (friction)
dt = 0.05                  # Time step
time_end = 10              # Simulation time

# Colors for each floor
colors = ['red', 'green', 'blue', 'orange', 'purple']

# Initial conditions (initial displacement and velocity of each mass)
initial_displacement = np.zeros(n_floors)
initial_velocity = np.zeros(n_floors)

# Force applied to the base (simulating earthquake)
def external_force(t):
    # Simple sinusoidal force (like an earthquake shake)
    return np.sin(2 * np.pi * 0.5 * t)  # Frequency of 0.5 Hz

# Mass-spring system equations of motion
def equations(t, y):
    # y contains displacement and velocity for each mass
    displacement = y[:n_floors]
    velocity = y[n_floors:]

    # Forces on each mass (spring forces and damping forces)
    force = np.zeros(n_floors)
    for i in range(n_floors):
        if i == 0:
            force[i] = k * (displacement[1] - displacement[0]) - damping * velocity[i] + external_force(t)
        elif i == n_floors - 1:
            force[i] = k * (displacement[n_floors-2] - displacement[n_floors-1]) - damping * velocity[i]
        else:
            force[i] = k * (displacement[i-1] - displacement[i]) + k * (displacement[i+1] - displacement[i]) - damping * velocity[i]

    # Equations of motion (F = ma), acceleration is force/mass
    acceleration = force / mass

    # Return velocity and acceleration (for the solver)
    return np.concatenate([velocity, acceleration])

# Initial conditions: displacement and velocity
initial_conditions = np.concatenate([initial_displacement, initial_velocity])

# Time array for simulation
time_points = np.linspace(0, time_end, int(time_end / dt))

# Solve the system of equations
solution = solve_ivp(equations, [0, time_end], initial_conditions, t_eval=time_points)

# Plotting the results
fig, ax = plt.subplots()

# Plot the displacement for each floor with color and name
for i in range(n_floors):
    ax.plot(solution.t, solution.y[i], label=f'Floor {i+1} ({colors[i]})', color=colors[i])

ax.set_xlabel('Time (s)')
ax.set_ylabel('Displacement (m)')
ax.set_title('Mass-Spring Resonator Array (Building Simulation)')
ax.legend()
plt.show()
