import matplotlib.pyplot as plt
import matplotlib.animation as anim
import math
import boid

x_arr = list()
y_arr = list()

b = boid.Boid()

for i in range(1, 201):
    x_arr.append(b.position.x)
    y_arr.append(b.position.y)

    if i % 50 == 0:
        b.change_direction()

    b.move()


fig, ax = plt.subplots(1, 1)

def update(i):
    ax.clear()
    ax.plot(x_arr[i], y_arr[i], "o")
    ax.set_xlim([0, boid.X_MAX])
    ax.set_ylim([0, boid.Y_MAX])


animation = anim.FuncAnimation(fig=fig, func=update, frames=200, interval=10)
plt.show()
