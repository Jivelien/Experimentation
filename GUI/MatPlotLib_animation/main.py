from matplotlib import pyplot as plt
from matplotlib import animation as anim
import time
import random

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

lx = []
ly = []

def animate(i):
    lx.append(len(lx)+1)
    ly.append(random.randint(0,100))    
    ax1.clear()
    ax1.plot(lx[-50:],ly[-50:])
    
ani = anim.FuncAnimation(fig, animate, interval = 10)
plt.show()
