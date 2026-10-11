import numpy as np
import matplotlib.pyplot as plt

# Parameters
f = 900       # Frequency (MHz)
Pt = 43       # Transmit power (dBm)
Gt = 15       # Transmit antenna gain (dBi)
Gr = 0        # Receive antenna gain (dBi)
L = 2         # Additional losses (dB)

d = np.linspace(0.1, 20, 400)  # Distance (km)

# Free-Space Path Loss
FSPL = 32.44 + 20*np.log10(d) + 20*np.log10(f)

# Received Power
Pr = Pt + Gt + Gr - FSPL - L

# Figure 1: FSPL vs Distance
plt.figure()
plt.plot(d, FSPL)
plt.xlabel('Distance (km)')
plt.ylabel('FSPL (dB)')
plt.title('FSPL vs Distance')
plt.grid(True)

# Figure 2: Received Power vs Distance
plt.figure()
plt.plot(d, Pr)
plt.xlabel('Distance (km)')
plt.ylabel('Received Power (dBm)')
plt.title('Received Power vs Distance')
plt.grid(True)

plt.show()