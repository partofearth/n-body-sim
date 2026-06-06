import numpy as np
import matplotlib.pyplot as plt


G = 6.67430e-11         
AU = 1.496e11            
DAY = 86400              

class Body:
    def __init__(self, name, mass, position, velocity, color, total_steps):
        self.name = name
        self.mass = mass

        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)

        self.positions = np.zeros((total_steps, 3))
        self.step_idx = 0
        self.color = color

    def kick_drift(self, acc, dt):
        self.velocity += 1/2 * acc * dt
        self.position += self.velocity * dt
        self.positions[self.step_idx] = self.position.copy()
        self.step_idx += 1
    def kick(self, acc, dt):
        self.velocity += 1/2 * acc * dt
    
def get_accs(bodies):
    accs = {b: np.zeros(3) for b in bodies}
    for i, b1 in enumerate(bodies):
        for b2 in bodies[i+1:]:
            r_vec = b2.position - b1.position
            dist = np.linalg.norm(r_vec)
            if dist == 0:
                continue
            common_factor = G / (dist ** 3)
            accs[b1] += r_vec * (b2.mass * common_factor)
            accs[b2] -= r_vec * (b1.mass * common_factor)
    return accs


def get_bodies(total_steps):
    sun = Body(
        mass=1.989e30,
        position=[0, 0, 0],
        velocity=[0, 0, 0],
        name="Sun",
        color="orange",
        total_steps=total_steps
    )

    earth = Body(
        mass=5.972e24,
        position=[AU, 0, 0],
        velocity=[0, 29780, 0],
        name="Earth",
        color="blue",
        total_steps=total_steps
    )
    
    mars = Body(
        mass = 6.39e23, 
        position=[1.524*AU, 0, 0],
        velocity=[0, 24070, 3000], #z-velocity exaggerated for easier visualization
        name="Mars",
        color="red",
        total_steps=total_steps
    )
    return sun,earth,mars



def gravity(m1, m2, r, r_hat):
    return G*m1*m2 * r_hat/r**2

dt = DAY
steps = 365

def run_simulation(bodies, steps, dt):
    accs = get_accs(bodies)
    for _ in range(steps):
        for b in bodies:
            b.kick_drift(accs[b], dt)
        accs = get_accs(bodies)
        for b in bodies:
            b.kick(accs[b], dt)
