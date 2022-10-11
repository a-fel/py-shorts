import matplotlib.pyplot as plt
import matplotlib.animation as anim
import math
import boid

NUM_OF_BOIDS = 15
STEPS = 400
positions = list()

for bo in range(NUM_OF_BOIDS):
    curr_boid = boid.Boid()
    curr_boid_positions = list()
    for step in range(1, STEPS + 1):
        curr_boid_positions.append((curr_boid.position.x, curr_boid.position.y))

        curr_boid.collision()
        curr_boid.move()




    positions.append(curr_boid_positions)

fig, ax = plt.subplots(1, 1)

def update(i):
    ax.clear()
    for idx in range(NUM_OF_BOIDS):
        ax.plot(positions[idx][i][0], positions[idx][i][1], "o")
    ax.set_xlim([0, boid.X_MAX])
    ax.set_ylim([0, boid.Y_MAX])


animation = anim.FuncAnimation(fig=fig, func=update, frames=STEPS, interval=5)
plt.show()
