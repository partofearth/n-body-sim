import numpy as np
from engine import get_bodies, gravity, run_sim, DAY
from visualizer import plot_orbit

if __name__ == "__main__":
    sun, earth = get_bodies()
    dt = DAY
    steps = 365
    r_vec = sun.position - earth.position
    r = np.linalg.norm(r_vec)
    r_hat = r_vec/r
    force = gravity(sun.mass, earth.mass, r, r_hat)
    run_sim(sun, earth, r_hat, r, force, dt, steps)
    plot_orbit(sun, earth)