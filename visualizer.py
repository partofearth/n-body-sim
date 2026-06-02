import numpy as np
import matplotlib.pyplot as plt

def plot_orbit(bodies):
    plt.figure(figsize=(8, 8))
    for b in bodies:
        positions = np.array(b.positions)
        plt.plot(
            positions[:, 0],
            positions[:, 1],
            label = b.name,
            color = b.color
        )


    plt.scatter(0, 0, s=200, label="Initial Sun Position", color="orange")
    plt.xlabel("x position (m)")
    plt.ylabel("y position (m)")
    plt.axis("equal")
    plt.legend()
    plt.show()