import matplotlib
import matplotlib.pyplot as plt
import csv
import numpy as np

# file name
path = ""
elec_name = ".csv"

price_in_name = ".csv"
price_out_name = ".csv"

# open file
f_price_in = open(path + price_in_name, 'r')
f_price_out = open(path + price_out_name, 'r')
f_electricity = open(path + elec_name, 'r')

price_in = []
price_out = []
electricity = []

with f_price_in:
    reader = csv.reader(f_price_in)
    for id, row in enumerate(reader):
        time = row[0]
        year = time.split('-')[0]
        if year == "2021":
            price_in.append(float(row[4]))

with f_price_out:
    reader = csv.reader(f_price_out)
    for id, row in enumerate(reader):
        time = row[0]
        year = time.split('-')[0]
        if year == "2021":
            price_out.append(float(row[4]))

with f_electricity:
    reader = csv.reader(f_electricity)
    for id, row in enumerate(reader):
        if id == 0:
            continue
        electricity.append(float(row[1]))

cost = []
minus = {}
for step, ele in enumerate(electricity):
    slot = step // 30
    if ele > 0:
        cost.append(ele / 60000 * price_in[slot])
    else:
        cost.append(ele / 60000 * price_out[slot])
    # if cost[len(cost) - 1] < 0:
        # minus[step] = [slot, cost[len(cost) - 1]]

minute_per_day = 24 * 60
n_day = len(cost) / minute_per_day
map = np.array(cost).reshape(int(n_day), int(minute_per_day))
data = np.transpose(map)
plot_data = np.flip(data, axis=0)

min = np.min(data)
max = np.max(data)
avg = np.average(data)
close = np.min(np.abs(data))

# fig = plt.figure(figsize=(10, 5), dpi=500)
fig = plt.figure()

ax = fig.add_subplot(111)
mycolors = 'viridis'
cm = plt.cm.get_cmap(mycolors)

normalize = matplotlib.colors.Normalize(vmin=-1, vmax=1)
plot = ax.pcolormesh(plot_data, norm=normalize, cmap=cm)

# plt.imshow(plot_data)
plt.show()

# Cheers~~