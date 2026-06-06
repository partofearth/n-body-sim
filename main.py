from engine import get_bodies, run_simulation, DAY
from visualizer import animate_orbit

if __name__ == "__main__":
    steps = 728
    bodies = get_bodies(steps)
    run_simulation(bodies, steps, DAY)
    animate_orbit(bodies, steps)