import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Resonance parameters
f0 = 1.0        # Natural frequency
A0 = 1.0        # Base amplitude
beta = 0.05     # Damping

# Time array
t = np.linspace(0, 10, 1000)

# Resonance function
def amplitude(f):
    return A0 / np.sqrt((f0**2 - f**2)**2 + (2 * beta * f)**2)

# Initial frequency
f_init = 1.0
A_init = amplitude(f_init)
y_init = A_init * np.sin(2 * np.pi * f_init * t)

# Plot setup
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.25)
line, = ax.plot(t, y_init, lw=2)
ax.set_xlim(0, 10)
ax.set_ylim(-2, 2)
ax.set_title("Interactive Resonance Oscillator")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Amplitude")

# Slider setup
axfreq = plt.axes([0.1, 0.1, 0.8, 0.05])
freq_slider = Slider(axfreq, 'Frequency (Hz)', 0.5, 2.0, valinit=f_init, valstep=0.01)

# Update function
def update(val):
    f = freq_slider.val
    A = amplitude(f)
    y = A * np.sin(2 * np.pi * f * t)
    line.set_ydata(y)
    fig.canvas.draw_idle()

freq_slider.on_changed(update)

plt.show()
