import matplotlib.pyplot as plt


def plot(grid, path, start, goal):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot obstacles
    xs, ys, zs = grid.grid.nonzero()
    ax.scatter(xs, ys, zs, c='red', marker='s', s=20)

    # Plot path
    if path:
        px, py, pz = zip(*path)
        ax.plot(px, py, pz, color='green', linewidth=3)

    # Plot start
    ax.scatter(start[0], start[1], start[2], c='blue', s=100, label="Start")

    # Plot goal
    ax.scatter(goal[0], goal[1], goal[2], c='yellow', s=100, label="Goal")

    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")

    ax.legend()

    plt.show()