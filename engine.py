import numpy as np
import matplotlib.pyplot as plt


G = 6.67430e-11         
AU = 1.496e11            
DAY = 86400              

class Body:
    def __init__(self, mass, position, velocity):
        self.mass = mass

        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)

        self.positions = []

    def kick_drift(self, force, dt):
        acc = force/self.mass
        self.velocity += 1/2 * acc * dt
        self.position += self.velocity * dt
        self.positions.append(self.position.copy())
    def kick(self, force, dt):
        acc = force/self.mass
        self.velocity += 1/2 * acc * dt

def get_bodies():
    sun = Body(
        mass=1.989e30,
        position=[0, 0],
        velocity=[0, 0]
    )

    earth = Body(
        mass=5.972e24,
        position=[AU, 0],
        velocity=[0, 29780]   
    )
    
    return sun,earth



def gravity(m1, m2, r, r_hat):
    return G*m1*m2 * r_hat/r**2

dt = DAY
steps = 365

def run_sim(b1, b2, r_hat, r, force, dt, steps):
    for _ in range(steps):
        b2.kick_drift(force, dt)
        b1.kick_drift(-force, dt)

        r_vec = b1.position - b2.position
        r = np.linalg.norm(r_vec)
        r_hat = r_vec / r
        new_force = gravity(b1.mass, b2.mass, r, r_hat)

        b2.kick(new_force, dt)
        b1.kick(-new_force, dt)
        force = new_force
