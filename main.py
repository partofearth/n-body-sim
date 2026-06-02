import numpy as np
from engine import get_bodies, run_sim, DAY
from visualizer import plot_orbit

if __name__ == "__main__":
    bodies = get_bodies()
    run_sim(bodies, DAY, 728)
    plot_orbit(bodies)