import csv

import matplotlib
from matplotlib import pyplot

with open('moba.csv', 'r') as f:
    reader = csv.reader(f)

    next(reader)
    next(reader)

    labels = next(reader)
    dates = []
    terms = []
    for line in reader:
        date = line[0]
        search_term_popularity = line[1:]
        dates.append(date)
        terms.append(search_term_popularity)

reversed_terms = []
for i in range(len(terms[0])):
    data = []
    for datum in terms:
        data.append(datum[i])
    reversed_terms.append(data)

pyplot.xlabel("time")
pyplot.ylabel("search popularity")
dates = matplotlib.dates.datestr2num(dates)

for index, search_term in enumerate(reversed_terms):
    pyplot.plot_date(dates, search_term, fmt='.-', label=labels[index+1])

pyplot.legend()
pyplot.show()

