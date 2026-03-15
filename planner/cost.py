import math
from config import W_DISTANCE, W_ALTITUDE, W_ENERGY


def movement_cost(current, neighbor):
    """
    Multi-objective cost function considering:
    - distance
    - altitude change
    - energy usage
    """

    dx = neighbor[0] - current[0]
    dy = neighbor[1] - current[1]
    dz = neighbor[2] - current[2]

    # Euclidean distance
    distance = math.sqrt(dx * dx + dy * dy + dz * dz)

    # Penalize altitude changes
    altitude_penalty = abs(dz)

    # Simulate extra energy when climbing
    energy = distance * 1.2 if dz != 0 else distance

    total_cost = (
        W_DISTANCE * distance +
        W_ALTITUDE * altitude_penalty +
        W_ENERGY * energy
    )

    return total_cost
