import matplotlib
import matplotlib.pyplot as plt
import csv
import numpy as np

# ========================= parameter ========================= #
path = "/Users/pwq/Downloads/"
name = "2022-07-12-18-24-22.csv"

# ============================================================= #

# open file
f = open(path + name, 'r')

nthreads = []
intensity = []
runtime = []
bandwidth = []

with f:
    reader = csv.reader(f)
    for id, row in enumerate(reader):
        if int(row[0]) not in nthreads:
            nthreads.append(int(row[0]))
        if float(row[1]) not in intensity:
            intensity.append(float(row[1]))
        runtime.append(float(row[2]))
        bandwidth.append(float(row[3]))


map = np.array(bandwidth).reshape(len(nthreads), len(intensity))
# data = np.transpose(map)  # matrix transpose
# plot_data = np.flip(data, axis=0)  # upside down
plot_data = map

# fig = plt.figure(figsize=(10, 5), dpi=500)
fig = plt.figure()

ax = fig.add_subplot(111)
mycolors = 'viridis'
cm = plt.cm.get_cmap(mycolors)

normalize = matplotlib.colors.Normalize(vmin=np.min(plot_data), vmax=np.max(plot_data))
lognorm = matplotlib.colors.Normalize(vmin=0.1, vmax=10)
plot = ax.pcolormesh(plot_data, norm=normalize, cmap=cm)
# plot = ax.pcolormesh(plot_data, norm=lognorm, cmap=cm)
# plot = ax.pcolormesh(plot_data, cmap=cm)

ax.set_xticks(range(len(intensity)))
ax.set_xticklabels(intensity)
ax.set_yticks(range(len(nthreads)))
ax.set_yticklabels(nthreads)
ax.set_title("contiguous access")
plt.xlabel("operational intensity")
plt.ylabel("nthreads")


fig.colorbar(plot, ax=ax)

# plt.imshow(plot_data)
plt.tight_layout()
plt.show()
