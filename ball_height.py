import matplotlib.pyplot as plt
import numpy as np

# Create time values from 0 to 5 seconds (100 points for smooth curve)
t = np.linspace(0, 5, 100)

# Calculate height using h(t) = -5*t² + 20*t + 1.5
h = -5 * t**2 + 20 * t + 1.5

# Plot the graph
plt.figure(figsize=(10, 6))
plt.plot(t, h, label='Height of Ball', color='red', linewidth=3)

# Mark the vertex (max height at t=2)
plt.plot(2, 21.5, 'bo', markersize=10, label='Max Height (2s, 21.5m)')

# Customize
plt.title("Ball Thrown in the Air - Quadratic Motion", fontsize=16)
plt.xlabel("Time (seconds)", fontsize=12)
plt.ylabel("Height (meters)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)
plt.axhline(0, color='black', linewidth=0.8)  # ground line

# Show plot
plt.tight_layout()
plt.show()