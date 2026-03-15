import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from vision.depth_anything_v2 import DepthAnythingV2
from environment.grid import OccupancyGrid3D
from planner.astar3d import astar
from mapping.depth_to_surface import depth_to_surface
from config import *


def main():

    image = "scene.jpg"

    # -------- Depth Estimation --------
    model = DepthAnythingV2()
    depth = model.estimate_depth(image)

    # -------- Old Voxel Environment --------
    grid = OccupancyGrid3D(GRID_X, GRID_Y, GRID_Z)

    grid.random_obstacles(0.05)  # your previous building generator

    path = astar(grid, START, GOAL)

    fig = plt.figure(figsize=(18,5))

    # --------------------------------
    # Depth Map
    # --------------------------------
    ax1 = fig.add_subplot(131)

    im = ax1.imshow(depth, cmap="plasma")
    ax1.set_title("Depth Map")

    plt.colorbar(im, ax=ax1)

    # --------------------------------
    # Height Surface
    # --------------------------------
    ax2 = fig.add_subplot(132, projection='3d')

    h,w = depth.shape
    X,Y = np.meshgrid(np.arange(w),np.arange(h))

    ax2.plot_surface(X,Y,depth,cmap="viridis")

    ax2.set_title("Height Surface")

    # --------------------------------
    # Voxel City + Drone Path
    # --------------------------------
    ax3 = fig.add_subplot(133, projection='3d')

    xs,ys,zs = grid.grid.nonzero()

    ax3.scatter(xs,ys,zs,c="red",s=10,alpha=0.4)

    if path:
        px,py,pz = zip(*path)
        ax3.plot(px,py,pz,color="green",linewidth=3)

    ax3.scatter(*START,c="blue",s=80,label="Start")
    ax3.scatter(*GOAL,c="yellow",s=80,label="Goal")

    ax3.set_title("Voxel City Navigation")

    ax3.legend()

    plt.show()


if __name__ == "__main__":
    main()