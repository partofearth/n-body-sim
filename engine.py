import numpy as np
import matplotlib.pyplot as plt


G = 6.67430e-11         
AU = 1.496e11            
DAY = 86400              

class Body:
    def __init__(self, name, mass, position, velocity, color):
        self.name = name
        self.mass = mass

        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)

        self.positions = []
        self.color = color

    def kick_drift(self, acc, dt):
        self.velocity += 1/2 * acc * dt
        self.position += self.velocity * dt
        self.positions.append(self.position.copy())
    def kick(self, acc, dt):
        self.velocity += 1/2 * acc * dt
    
def get_accs(bodies):
    accs = {b: np.zeros(2) for b in bodies}
    for i, b1 in enumerate(bodies):
        for b2 in bodies[i+1:]:
            r_vec = b2.position - b1.position
            dist = np.linalg.norm(r_vec)
            if dist == 0:
                continue
            force = (G * b1.mass * b2.mass / dist**2) * (r_vec / dist)
            accs[b1] += force / b1.mass
            accs[b2] -= force / b2.mass
    return accs


def get_bodies():
    sun = Body(
        mass=1.989e30,
        position=[0, 0],
        velocity=[0, 0],
        name="Sun",
        color="orange"
    )

    earth = Body(
        mass=5.972e24,
        position=[AU, 0],
        velocity=[0, 29780],
        name="Earth",
        color="blue"
    )
    
    mars = Body(
        mass = 6.39e23, 
        position=[1.524*AU, 0],
        velocity=[0, 24070],
        name="Mars",
        color="red"
    )
    return sun,earth,mars



def gravity(m1, m2, r, r_hat):
    return G*m1*m2 * r_hat/r**2

dt = DAY
steps = 365

def run_sim(bodies, dt, steps):
    for _ in range(steps):
        accs = get_accs(bodies)
        for b in bodies:
            b.kick_drift(accs[b], dt)
        next_accs = get_accs(bodies)
        for b in bodies:
            b.kick(next_accs[b], dt)
