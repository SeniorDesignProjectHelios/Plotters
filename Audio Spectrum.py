import numpy as np
import matplotlib.pyplot as plt

# Create x values from 0 to 2*pi (one cycle)
x = np.linspace(0, 2 * np.pi, 100)

# Calculate the sine values for the x values
y1 = np.sin(x)

# Create an array with the same size as x with a constant value of 1
y2 = np.ones_like(x)

# Set up the plot
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 6), sharex=True)

# Plot the sine wave on the first subplot
ax1.plot(x, y1)
ax1.set_ylim(-1.2, 1.2)
ax1.set_ylabel("Amplitude")
ax1.set_title("Sine Wave")

# Plot the constant amplitude on the second subplot
ax2.plot(x, y2)
ax2.set_ylim(-1.2, 1.2)
ax2.set_xlabel("x")
ax2.set_ylabel("Amplitude")
ax2.set_title("Constant Amplitude")

# Show the plots
plt.show()
