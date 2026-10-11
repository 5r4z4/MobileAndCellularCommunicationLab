
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon

# Input
R = 1
i, j = 3, 1

# Calculation
N = i**2 + i*j + j**2
Q = np.sqrt(3*N)
D = R*Q

print("Cluster Size N =", N)
print("Reuse Ratio Q =", round(Q, 2))
print("Reuse Distance D =", round(D, 2), "km")

# Hexagonal cells
fig, ax = plt.subplots(figsize=(8, 6))

for x in range(-2, 5):
    for y in range(-2, 4):
        cx = np.sqrt(3)*R*(x + y/2)
        cy = 1.5*R*y

        # Highlight two co-channel cells
        same = (x, y) in [(0, 0), (i, j)]
        color = 'gold' if same else 'lightgray'

        hexagon = RegularPolygon(
            (cx, cy), 6, radius=R,
            orientation=0,
            facecolor=color, edgecolor='black'
        )
        ax.add_patch(hexagon)

        if same:
            ax.text(cx, cy, "F1", ha='center', va='center')

# Reuse distance line
x1, y1 = 0, 0
x2 = np.sqrt(3)*R*(i + j/2)
y2 = 1.5*R*j

ax.plot([x1, x2], [y1, y2], 'r--', label=f'D = {D:.2f} km')


ax.set_title(f"Co-channel Reuse (N = {N}, Q = {Q:.2f})")
ax.set_xlabel("Distance (km)")
ax.set_ylabel("Distance (km)")
ax.set_aspect('equal')
ax.legend()
ax.grid()
plt.show()
