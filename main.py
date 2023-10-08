import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)


sun = plt.Circle((0, 0), 0.5, color='yellow')
earth = plt.Circle((1.2, 0), 0.1, color='blue')
moon = plt.Circle((1, 0), 0.05, color='gray')
alignment_line, = ax.plot([], [], color='black')

ax.add_artist(sun)
ax.add_artist(earth)
ax.add_artist(moon)

def init():
    alignment_line.set_data([], [])
    return sun, earth, moon, alignment_line


def update(frame):

    earth_x = 1.5 * np.cos(np.radians(frame * 9))
    earth_y = 1.5 * np.sin(np.radians(frame * 9))
    moon_x = 1 * np.cos(np.radians(frame * 15))
    moon_y = 1 * np.sin(np.radians(frame * 15))
    

    earth.set_center((earth_x, earth_y))
    moon.set_center((moon_x, moon_y))
    
    distance_earth_moon = np.sqrt((earth_x - moon_x) ** 2 + (earth_y - moon_y) ** 2)
    
    
    print(distance_earth_moon)
    if distance_earth_moon <= 0.50 or distance_earth_moon >=  2.5 :
        moon.set_color('red')
        earth.set_color('gray')
        alignment_line.set_data([earth_x,moon_x],[earth_y,moon_y]) 
        
    else:
        moon.set_color('gray')
        earth.set_color('blue')
        alignment_line.set_data([],[])
    
    return sun, earth, moon,alignment_line

animation = FuncAnimation(fig, update, frames=360, init_func=init, blit=True)

plt.show()
