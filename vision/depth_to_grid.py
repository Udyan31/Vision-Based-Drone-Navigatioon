import numpy as np


def depth_to_grid(depth_map, grid):

    h, w = depth_map.shape

    # Choose threshold for near objects
    threshold = np.percentile(depth_map, 40)

    for y in range(h):
        for x in range(w):

            if depth_map[y, x] < threshold:

                gx = int(x / w * grid.grid.shape[0])
                gy = int(y / h * grid.grid.shape[1])

                # Mark obstacle in lower altitude
                grid.grid[gx, gy, 0:3] = 1