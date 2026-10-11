
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon

R1 = 2 
R2 = R1 / 2 

# Calculate hexagonal area
A1 = (3*np.sqrt(3)/2) * R1**2
A2 = (3*np.sqrt(3)/2) * R2**2

print("Original Cell Area:", round(A1, 2), "km^2")
print("Split Cell Area:", round(A2, 2), "km^2")

# Draw cells
fig, ax = plt.subplots()

ax.add_patch(RegularPolygon(
    (0, 0), numVertices=6, radius=R1,
    orientation=np.pi/6, fill=False,
    edgecolor='blue', linewidth=2
))

ax.add_patch(RegularPolygon(
    (5, 0), numVertices=6, radius=R2,
    orientation=np.pi/6, fill=False,
    edgecolor='red', linewidth=2
))

ax.text(0, -2.5, "Original Cell (R=2 km)", ha='center')
ax.text(5, -1.5, "Split Cell (R=1 km)", ha='center')

ax.set_title("Cell Coverage and Cell Splitting")
ax.set_aspect('equal')
ax.set_xlim(-3, 7)
ax.set_ylim(-3, 3)
ax.axis('off')
plt.show()
