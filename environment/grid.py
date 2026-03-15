import numpy as np
import random


class OccupancyGrid3D:
    def __init__(self, x, y, z):
        """
        Initialize a 3D occupancy grid.
        0 = free space
        1 = obstacle
        """
        self.grid = np.zeros((x, y, z), dtype=int)

    # -----------------------------------
    # RANDOM OBSTACLES
    # -----------------------------------
    def random_obstacles(self, density):
        """
        Fill the grid randomly with obstacles.
        density: percentage of space to fill (0.1 = 10%)
        """
        total_voxels = self.grid.size
        obstacle_count = int(total_voxels * density)

        for _ in range(obstacle_count):
            x = random.randint(0, self.grid.shape[0] - 1)
            y = random.randint(0, self.grid.shape[1] - 1)
            z = random.randint(0, self.grid.shape[2] - 1)

            self.grid[x, y, z] = 1

    # -----------------------------------
    # ADD SOLID BOX
    # -----------------------------------
    def add_box(self, x1, x2, y1, y2, z1, z2):
        """
        Add a rectangular solid obstacle.
        """
        self.grid[x1:x2, y1:y2, z1:z2] = 1

    # -----------------------------------
    # ADD WALLS
    # -----------------------------------
    def add_wall_x(self, x_position):
        """
        Add vertical wall at fixed X.
        """
        self.grid[x_position, :, :] = 1

    def add_wall_y(self, y_position):
        """
        Add vertical wall at fixed Y.
        """
        self.grid[:, y_position, :] = 1

    def add_wall_z(self, z_position):
        """
        Add horizontal layer at fixed Z.
        """
        self.grid[:, :, z_position] = 1

    # -----------------------------------
    # ADD PILLAR
    # -----------------------------------
    def add_pillar(self, x, y):
        """
        Add vertical pillar from ground to top.
        """
        self.grid[x, y, :] = 1

    # -----------------------------------
    # ADD CORRIDOR
    # -----------------------------------
    def add_corridor(self, width=3):
        """
        Create a tunnel-like corridor through the environment.
        """
        mid = self.grid.shape[1] // 2

        # Fill everything with obstacles first
        self.grid[:, :, :] = 1

        # Carve out a corridor
        self.grid[:, mid - width:mid + width, :] = 0

    # -----------------------------------
    # CLEAR REGION
    # -----------------------------------
    def clear_area(self, x1, x2, y1, y2, z1, z2):
        """
        Clear a region (set to free space).
        """
        self.grid[x1:x2, y1:y2, z1:z2] = 0

    # -----------------------------------
    # GENERATE CITY ENVIRONMENT
    # -----------------------------------
    def generate_city(self, building_size=4, street_width=3, max_height=None):
        """
        Generate a simple city with tall buildings and streets.
        """

        if max_height is None:
            max_height = self.grid.shape[2] - 1

        # Clear entire grid
        self.grid[:, :, :] = 0

        x_size, y_size, z_size = self.grid.shape
        block_size = building_size + street_width

        for x in range(0, x_size, block_size):
            for y in range(0, y_size, block_size):

                # Random building height
                height = np.random.randint(z_size // 2, max_height)

                x_end = min(x + building_size, x_size)
                y_end = min(y + building_size, y_size)

                # Create building
                self.grid[x:x_end, y:y_end, 0:height] = 1

    # -----------------------------------
    # UTILITY FUNCTIONS
    # -----------------------------------
    def in_bounds(self, x, y, z):
        """
        Check if coordinates are inside grid.
        """
        return (
            0 <= x < self.grid.shape[0] and
            0 <= y < self.grid.shape[1] and
            0 <= z < self.grid.shape[2]
        )

    def is_free(self, x, y, z):
        """
        Return True if cell is not an obstacle.
        """
        return self.grid[x, y, z] == 0
        