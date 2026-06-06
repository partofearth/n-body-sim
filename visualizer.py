import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate_orbit(history, metadata):
    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(111, projection="3d")

    num_bodies = history.shape[1]
    lines = []
    points = []

    for i in range(num_bodies):
        meta = metadata[i]
        line, = ax.plot([], [], [], color=meta["color"], label=meta["name"], linewidth=1.5)
        point, = ax.plot([], [], [], marker='o', color=meta["color"], markersize=8)
        lines.append(line)
        points.append(point)

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
        for i in range(num_bodies):
            pos_trend = history[:frame+1, i, :]
            lines[i].set_data_3d((pos_trend[:, 0], pos_trend[:, 1], pos_trend[:, 2]))
            current_pos = history[frame, i, :]
            points[i].set_data_3d(([current_pos[0]], [current_pos[1]], [current_pos[2]]))
        return lines + points

    ani = animation.FuncAnimation(
        fig, 
        update,
        frames=history.shape[0],
        repeat=False,
        interval=10
    )
    plt.show()