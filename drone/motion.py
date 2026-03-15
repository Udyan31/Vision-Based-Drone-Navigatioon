# Generate all possible 3D moves (26-connected grid)

MOVES = []

for dx in [-1, 0, 1]:
    for dy in [-1, 0, 1]:
        for dz in [-1, 0, 1]:

            # Skip (0,0,0) because that means no movement
            if dx == 0 and dy == 0 and dz == 0:
                continue

            MOVES.append((dx, dy, dz))