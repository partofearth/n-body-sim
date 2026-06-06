import numpy as np

G = 6.67430e-11
AU = 1.496e11
DAY = 86400

def get_init_state():
    metadata = [
        {"name": "Sun", "color": "orange"},
        {"name": "Earth", "color": "blue"},
        {"name": "Mars", "color": "red"}
    ]
    masses = np.array([1.989e30, 5.972e24, 6.39e23])
    positions = np.array([
        [0.0, 0.0, 0.0],
        [AU, 0.0, 0.0],
        [1.524 * AU, 0.0, 0.0]
    ])
    velocities = np.array([
        [0.0, 0.0, 0.0],
        [0.0, 29780.0, 0.0],
        [0.0, 24070.0, 3000.0]
    ])
    return masses, positions, velocities, metadata

def get_accs(pos, masses):
    r_vecs = pos[np.newaxis, :, :] - pos[:, np.newaxis, :]
    dists = np.linalg.norm(r_vecs, axis=2)
    inv_dist3 = np.zeros_like(dists)
    mask = dists > 0
    inv_dist3[mask] = 1.0 / (dists[mask] ** 3)
    acc = G * np.sum(r_vecs * inv_dist3[:, :, np.newaxis] * masses[np.newaxis, :, np.newaxis], axis=1)
    return acc

def simulate_orbits(steps, dt):
    masses, positions, velocities, metadata = get_init_state()
    num_bodies = len(masses)
    history = np.zeros((steps, num_bodies, 3))
    
    acc = get_accs(positions, masses)
    for step in range(steps):
        velocities += 0.5 * acc * dt
        positions += velocities * dt
        history[step] = positions
        acc = get_accs(positions, masses)
        velocities += 0.5 * acc * dt
        
    return history, metadata