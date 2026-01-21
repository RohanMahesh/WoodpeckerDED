import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib.colors import ListedColormap

p = 0.4
n = 30
iterations = 10

def single_center_grid(n):
    # 30x30 grid of 0's
    grid = np.zeros((n, n), dtype=int)
    # center at (15,15) = 1
    center = (n // 2, n // 2)
    grid[center] = 1
    return grid

def step(grid, p=0.4):
    # create new grid copy 
    n = grid.shape[0]
    new_grid = grid.copy()

    # run thru each cell, check neighbors, then return new grid
    for i in range(n):
        for j in range(n):
            if grid[i, j] == 1:
                # the 8 neighboring squares
                neighbors = [
                    (i-1, j-1), (i-1, j), (i-1, j+1), (i,   j-1), (i,   j+1), (i+1, j-1), (i+1, j), (i+1, j+1)
                ]
                for x, y in neighbors:
                    # Check that neighbor is inside the grid - not at the borders
                    if 0 <= x < n and 0 <= y < n:
                        if grid[x, y] == 0 and random.random() < p:
                            new_grid[x, y] = 1
    return new_grid

#initialize grid
grid = single_center_grid(n)
#colors
cmap = ListedColormap(['green', 'saddlebrown'])

plt.ion()
fig, ax = plt.subplots()
for t in range(iterations + 1):
    ax.clear()
    ax.imshow(grid, cmap=cmap, vmin=0, vmax=1)
    ax.axis('off')
    ax.set_title(f"Step {t}")
    #pause 0.75 second per step
    plt.pause(0.4)

    # stop after last iteraiton
    if t < iterations:
        grid = step(grid, p)

plt.ioff()
plt.show()
