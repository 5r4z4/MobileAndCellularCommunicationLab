import math
import matplotlib.pyplot as plt

Pt, Gt, Gr, f = 30, 2, 2, 900          # Tx power (dBm), Tx gain (dB), Rx gain (dB), frequency (MHz)
distances = list(range(1, 11))         # distances in km

fspl = [32.44 + 20 * math.log10(f) + 20 * math.log10(d) for d in distances]   # path loss (dB)
Pr = [Pt + Gt + Gr - L for L in fspl]                                          # received power (dBm)

print("FSPL AND RECEIVED POWER")

for d, L, p in zip(distances, fspl, Pr):
    print("Distance:", d, "km | FSPL:", round(L, 2), "dB | Pr:", round(p, 2), "dBm")
    
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
ax1.plot(distances, fspl, marker='o')
ax1.set(xlabel="Distance (km)", ylabel="FSPL (dB)", title="Distance vs Free-Space Path Loss")
ax1.grid(True)

ax2.plot(distances, Pr, marker='o')
ax2.set(xlabel="Distance (km)", ylabel="Received Power (dBm)", title="Distance vs Received Power")
ax2.grid(True)

plt.tight_layout()
plt.show()