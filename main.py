import numpy as np
from engine import get_bodies, physics_generator, DAY
from visualizer import animate_orbit

if __name__ == "__main__":
    bodies = get_bodies()
    gen = physics_generator(bodies, DAY)
    animate_orbit(bodies, gen)