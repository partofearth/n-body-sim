import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate_orbit(bodies, gen):
    fig, ax = plt.subplots(figsize=(8,8))
    lines = {b: ax.plot([], [], color=b.color, label=b.name, linewidth=1.5)[0] for b in bodies}
    points = {b: ax.plot([], [], marker='o', color=b.color, markersize=8)[0] for b in bodies    }
    limit = 2.0 * 1.496e11
    ax.set_xlim([-limit, limit])
    ax.set_ylim([-limit, limit])
    ax.set_xlabel("x position (m)")
    ax.set_ylabel("y position (m)")
    ax.set_aspect('equal')
    ax.legend(loc="upper left")

    def update(frame):
        updated_bodies = next(gen)
        for b in updated_bodies:
            pos = b.position
            pos_array = np.array(b.positions)
            if len(pos_array) > 0:
                lines[b].set_data(pos_array[:, 0], pos_array[:, 1])
                points[b].set_data([pos[0]], [pos[1]])
        return list(lines.values()) + list(points.values())
    

    ani = animation.FuncAnimation(
        fig, 
        update,
        frames=728,
        repeat=False,
        blit=True,
        interval=10
    )
    plt.show()