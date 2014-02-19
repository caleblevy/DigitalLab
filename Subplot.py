import numpy as np
import matplotlib.pyplot as plt

box = dict(facecolor='yellow', pad=5, alpha=0.2)

fig = plt.figure()
fig.subplots_adjust(left=0.2, wspace=0.6)


# ax1 = fig.add_subplot(221)
ax1 = plt.subplot2grid((3,2), (0,0))
ax1.plot(2000*np.random.rand(10))
ax1.set_title('ylabels not aligned')
ax1.set_ylabel('misaligned 1', bbox=box)
ax1.set_ylim(0, 2000)

# ax3 = fig.add_subplot(223)
ax3 = plt.subplot2grid((3,2), (1,0))
ax3.set_ylabel('misaligned 2',bbox=box)
ax3.plot(np.random.rand(10))


labelx = -0.3  # axes coords

# ax2 = fig.add_subplot(222)
ax2 = plt.subplot2grid((3,2), (0,1))
ax2.set_title('ylabels aligned')
ax2.plot(2000*np.random.rand(10))
ax2.set_ylabel('aligned 1', bbox=box)
ax2.yaxis.set_label_coords(labelx, 0.5)
ax2.set_ylim(0, 2000)

# ax4 = fig.add_subplot(224)
ax4 = plt.subplot2grid((3,2), (1,1))
ax4.plot(np.random.rand(10))
ax4.set_ylabel('aligned 2', bbox=box)
ax4.yaxis.set_label_coords(labelx, 0.5)

# ax5 = plt.subplot2grid((3,2), (2,0), colspan=2)
# ax5.plot(np.random.rand(10))
# ax5.set_ylabel('misaligned 3', bbox=box)

plt.show()