# page 313 plotting random_walk.py

import matplotlib.pyplot as plt

from random_walk import RandomWalk

#Keep makaing new walks, as long as the program is active. 
while True:
#Make random walk
    rw= RandomWalk(5000)
    rw.fill_walk()

    #plot the points in the walk
    plt.style.use('classic')
    fig,ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values , linewidth=1)
    ax.set_aspect('equal')

    # Emphasize the first and last points
    ax.scatter(0,0,c='green',edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    #Remove Axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()


    keep_running = input ("Make another walk (y/n): ")
    if keep_running == 'n':
        break