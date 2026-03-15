import numpy as np
import matplotlib.pyplot as plt


def depth_to_surface(depth_map):

    h, w = depth_map.shape

    X = np.arange(0, w)
    Y = np.arange(0, h)

    X, Y = np.meshgrid(X, Y)

    Z = depth_map

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(
        X,
        Y,
        Z,
        cmap="viridis",
        linewidth=0
    )

    plt.show()