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

def gravity(G, m1, m2, r, r_hat):
    return G*m1*m2 * r_hat/r**2

dt = DAY
steps = 365

r_vec = sun.position - earth.position
r = np.linalg.norm(r_vec)
r_hat = r_vec / r
force = gravity(G, sun.mass, earth.mass, r, r_hat)
for _ in range(steps):
    earth.kick_drift(force, dt)
    sun.kick_drift(-force, dt)

    r_vec = sun.position - earth.position
    r = np.linalg.norm(r_vec)
    r_hat = r_vec / r
    new_force = gravity(G, sun.mass, earth.mass, r, r_hat)

    earth.kick(new_force, dt)
    sun.kick(-new_force, dt)
    force = new_force



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