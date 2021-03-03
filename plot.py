import csv

import matplotlib
import matplotlib.dates as mdates
from matplotlib import pyplot

with open('moba.csv', 'r') as f:
    reader = csv.reader(f)

    for i in range(2):
        next(reader)

    labels = list(next(reader))

    data = []
    x = []
    for line in reader:
        x.append(line[0]) # add the date to the x data
        data.append(line[1:])

dates = matplotlib.dates.date2num(x)

for i in range(len(data[0])):
    pyplot.plot_date(dates, [int(y[i]) for y in data], fmt='.-', label=labels[i+1])


pyplot.legend()
pyplot.show()