from engine import simulate_orbits, DAY
from visualizer import animate_orbit

if __name__ == "__main__":
    steps = 728
    history, metadata = simulate_orbits(steps, DAY)
    animate_orbit(history, metadata)