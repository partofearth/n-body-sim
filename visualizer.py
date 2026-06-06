import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate_orbit(bodies, steps):
    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(111, projection="3d")

    lines = {b: ax.plot([], [], [], color=b.color, label=b.name, linewidth=1.5)[0] for b in bodies}
    points = {b: ax.plot([], [], [], marker='o', color=b.color, markersize=8)[0] for b in bodies}
    
    limit = 2.0 * 1.496e11
    ax.set_xlim([-limit, limit])
    ax.set_ylim([-limit, limit])
    ax.set_zlim([-limit, limit])
    ax.set_xlabel("x position (m)")
    ax.set_ylabel("y position (m)")
    ax.set_zlabel("z position (m)")
    ax.set_aspect('equal')
    ax.legend(loc="upper left")

    def update(frame):
        for b in bodies:
            pos_trend = b.positions[:frame+1]
            lines[b].set_data_3d((pos_trend[:, 0], pos_trend[:, 1], pos_trend[:, 2]))
    
            current_pos = b.positions[frame]
            points[b].set_data_3d(([current_pos[0]], [current_pos[1]], [current_pos[2]]))
            
        return list(lines.values()) + list(points.values())
    

    ani = animation.FuncAnimation(
        fig, 
        update,
        frames=steps,
        repeat=False,
        interval=10
    )
    plt.show()