import numpy as np
import matplotlib.pyplot as plt

def plot_orbit(sun, earth):
    earth_positions = np.array(earth.positions)
    sun_positions = np.array(sun.positions)

    plt.figure(figsize=(8, 8))
    plt.plot(
        earth_positions[:, 0],
        earth_positions[:, 1],
        label="Earth"
    )
    plt.plot(
        sun_positions[:, 0],
        sun_positions[:, 1],
        label="Sun"
    )
    plt.scatter(0, 0, s=200, label="Initial Sun Position", color="orange")
    plt.xlabel("x position (m)")
    plt.ylabel("y position (m)")
    plt.axis("equal")
    plt.legend()
    plt.show()