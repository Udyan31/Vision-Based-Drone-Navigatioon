import heapq
import math
from drone.motion import MOVES
from planner.cost import movement_cost


def heuristic(a, b):
    """Euclidean distance heuristic."""
    return math.dist(a, b)


def astar(grid, start, goal):
    """
    Perform A* search on the 3D grid.
    Returns the path if found, otherwise None.
    """

    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        # Goal reached
        if current == goal:
            path = []

            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.append(start)
            path.reverse()
            return path

        # Explore neighbors
        for move in MOVES:
            neighbor = (
                current[0] + move[0],
                current[1] + move[1],
                current[2] + move[2]
            )

            if not grid.in_bounds(*neighbor):
                continue

            if not grid.is_free(*neighbor):
                continue

            tentative_g = g_score[current] + movement_cost(current, neighbor)

            if neighbor not in g_score or tentative_g < g_score[neighbor]:

                came_from[neighbor] = current
                g_score[neighbor] = tentative_g

                f_score = tentative_g + heuristic(neighbor, goal)

                heapq.heappush(open_set, (f_score, neighbor))

    return None
