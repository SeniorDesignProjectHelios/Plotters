import numpy as np
import matplotlib.pyplot as plt

# Pendulum properties
initial_length = 1.0  # Initial length of the pendulum in meters
gravity = 9.81  # Acceleration due to gravity (m/s^2)
initial_angle_deg = 30  # Initial angle of the pendulum in degrees
num_pendulums = 3  # Number of pendulums

# Time properties
time_step = 0.01  # Time step for the simulation (s)
total_time = 10  # Total simulation time (s)

# Convert initial angle to radians
initial_angle_rad = np.deg2rad(initial_angle_deg)

# Function to calculate the pendulum's angle as a function of time
def pendulum_angle(t, initial_angle, length):
    return initial_angle * np.cos(np.sqrt(gravity / length) * t)

# Plot the pendulum swings in polar coordinates
plt.figure()
colors = ['b', 'r', 'g', 'm', 'c', 'y', 'k']

for i in range(num_pendulums):
    # Calculate the pendulum's position in polar coordinates
    length = initial_length / (2 ** i)
    times = np.arange(0, total_time, time_step)
    angles = pendulum_angle(times, initial_angle_rad, length)
    radii = np.ones_like(angles) * length

    # Plot the pendulum swing
    plt.polar(angles, radii, color=colors[i % len(colors)], label=f"Pendulum {i + 1} (Length: {length:.2f} m)")

plt.title(f"Pendulum Swing (Initial Angle: {initial_angle_deg} degrees)")
plt.legend()
plt.grid(True)
plt.show()

#########################

import numpy as np
import matplotlib.pyplot as plt

# Pendulum properties
initial_length = 1.0  # Initial length of the pendulum in meters
gravity = 9.81  # Acceleration due to gravity (m/s^2)
initial_angle_deg = 30  # Initial angle of the pendulum in degrees
num_pendulums = 3  # Number of sub-pendulums

# Time properties
time_step = 0.01  # Time step for the simulation (s)
total_time = 10  # Total simulation time (s)

# Convert initial angle to radians
initial_angle_rad = np.deg2rad(initial_angle_deg)

# Function to calculate the pendulum's angle as a function of time
def pendulum_angle(t, initial_angle, length):
    return initial_angle * np.cos(np.sqrt(gravity / length) * t)

# Function to calculate the pendulum's end point in Cartesian coordinates
def pendulum_position(t, initial_angle, lengths):
    angles = [pendulum_angle(t, initial_angle, length) for length in lengths]
    x = np.sum(np.multiply(lengths, np.cos(angles)))
    y = np.sum(np.multiply(lengths, np.sin(angles)))
    return x, y

# Calculate time values for the plot
times = np.arange(0, total_time, time_step)

# Plot the end points of all 10 main pendulums with respect to time
plt.figure()

for i in range(10):
    main_pendulum_length = initial_length * (i + 1)
    lengths = [main_pendulum_length / (2 ** j) for j in range(num_pendulums)]

    x_coords = []
    y_coords = []

    for t in times:
        x, y = pendulum_position(t, initial_angle_rad, lengths)
        x_coords.append(x)
        y_coords.append(y)

    plt.plot(x_coords, y_coords, label=f"Main Pendulum {i + 1} (Length: {main_pendulum_length:.2f} m)")

plt.title(f"End Points of Main Pendulums (Initial Angle: {initial_angle_deg} degrees)")
plt.xlabel("X Coordinate (m)")
plt.ylabel("Y Coordinate (m)")
plt.legend()
plt.grid(True)
plt.show()

#########################################################

import numpy as np
import matplotlib.pyplot as plt

# Pendulum properties
initial_length = 1.0  # Initial length of the pendulum in meters
gravity = 9.81  # Acceleration due to gravity (m/s^2)
num_pendulums = 3  # Number of sub-pendulums

# Time properties
time_step = 0.01  # Time step for the simulation (s)
total_time = 10  # Total simulation time (s)

# Function to calculate the pendulum's angle as a function of time
def pendulum_angle(t, initial_angle, length):
    return initial_angle * np.cos(np.sqrt(gravity / length) * t)

# Function to calculate the pendulum's end point in Cartesian coordinates
def pendulum_position(t, initial_angle, lengths):
    angles = [pendulum_angle(t, initial_angle, length) for length in lengths]
    x = np.sum(np.multiply(lengths, np.cos(angles)))
    y = np.sum(np.multiply(lengths, np.sin(angles)))
    return x, y

# Calculate time values for the plot
times = np.arange(0, total_time, time_step)

# Plot the end points of all 10 main pendulums with respect to time
plt.figure()

for i in range(10):
    main_pendulum_length = initial_length * (i + 1)
    initial_angle_deg = i + 1  # Set initial angle for each main pendulum
    initial_angle_rad = np.deg2rad(initial_angle_deg)
    lengths = [main_pendulum_length / (2 ** j) for j in range(num_pendulums)]

    x_coords = []
    y_coords = []

    for t in times:
        x, y = pendulum_position(t, initial_angle_rad, lengths)
        x_coords.append(x)
        y_coords.append(y)

    plt.plot(x_coords, y_coords, label=f"Main Pendulum {i + 1} (Length: {main_pendulum_length:.2f} m, Initial Angle: {initial_angle_deg}°)")

plt.title(f"End Points of Main Pendulums")
plt.xlabel("X Coordinate (m)")
plt.ylabel("Y Coordinate (m)")
plt.legend()
plt.grid(True)
plt.show()

###########################

import numpy as np
import matplotlib.pyplot as plt

# Pendulum properties
initial_length = 1.0  # Initial length of the pendulum in meters
gravity = 9.81  # Acceleration due to gravity (m/s^2)
num_pendulums = 3  # Number of sub-pendulums

# Time properties
time_step = 0.01  # Time step for the simulation (s)
total_time = 10  # Total simulation time (s)

# Function to calculate the pendulum's angle as a function of time
def pendulum_angle(t, initial_angle, length):
    return initial_angle * np.cos(np.sqrt(gravity / length) * t)

# Function to calculate the pendulum's end point in Cartesian coordinates
def pendulum_position(t, initial_angle, lengths):
    angles = [pendulum_angle(t, initial_angle, length) for length in lengths]
    x = np.sum(np.multiply(lengths, np.cos(angles)))
    y = np.sum(np.multiply(lengths, np.sin(angles)))
    return x, y

# Calculate time values for the plot
times = np.arange(0, total_time, time_step)

# Plot the end points of all 10 main pendulums with respect to time
fig, ax = plt.subplots()

# Set black background
ax.set_facecolor('black')
fig.patch.set_facecolor('black')

for i in range(10):
    main_pendulum_length = initial_length * (i + 1)
    initial_angle_deg = 10 * (i + 1)  # Set initial angle for each main pendulum
    initial_angle_rad = np.deg2rad(initial_angle_deg)
    lengths = [main_pendulum_length / (2 ** j) for j in range(num_pendulums)]

    x_coords = []
    y_coords = []

    for t in times:
        x, y = pendulum_position(t, initial_angle_rad, lengths)
        x_coords.append(x)
        y_coords.append(y)

    ax.plot(x_coords, y_coords, label=f"Main Pendulum {i + 1} (Length: {main_pendulum_length:.2f} m, Initial Angle: {initial_angle_deg}°)")

# Set title and remove grid and axis
ax.set_title(f"End Points of Main Pendulums", color='white')
ax.axis('off')
plt.legend()
plt.show()

############################################

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Pendulum properties
initial_length = 1.0  # Initial length of the pendulum in meters
gravity = 9.81  # Acceleration due to gravity (m/s^2)
num_pendulums = 3  # Number of sub-pendulums

# Time properties
time_step = 0.01  # Time step for the simulation (s)
total_time = 10  # Total simulation time (s)

# Function to calculate the pendulum's angle as a function of time
def pendulum_angle(t, initial_angle, length):
    return initial_angle * np.cos(np.sqrt(gravity / length) * t)

# Function to calculate the pendulum's end point in Cartesian coordinates
def pendulum_position(t, initial_angle, lengths):
    angles = [pendulum_angle(t, initial_angle, length) for length in lengths]
    x = np.sum(np.multiply(lengths, np.cos(angles)))
    y = np.sum(np.multiply(lengths, np.sin(angles)))
    return x, y

# Calculate time values for the plot
times = np.arange(0, total_time, time_step)

# Set up the plot
fig, ax = plt.subplots()
ax.set_facecolor('black')
fig.patch.set_facecolor('black')
ax.axis('off')

# Set axis limits for better visualization
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)

# Prepare pendulum lines for animation
lines = []
for i in range(10):
    line, = ax.plot([], [], lw=1)
    lines.append(line)

# Initialize animation function
def init():
    for line in lines:
        line.set_data([], [])
    return lines

# Animation update function
def update(frame):
    for i, line in enumerate(lines):
        main_pendulum_length = initial_length * (i + 1)
        initial_angle_deg = 10 * (i + 1)  # Set initial angle for each main pendulum
        initial_angle_rad = np.deg2rad(initial_angle_deg)
        lengths = [main_pendulum_length / (2 ** j) for j in range(num_pendulums)]

        x, y = pendulum_position(times[frame], initial_angle_rad, lengths)
        line.set_data([0, x], [0, y])

    return lines

# Create animation
ani = FuncAnimation(fig, update, frames=len(times), init_func=init, blit=True)

# Display the animation
plt.show()
