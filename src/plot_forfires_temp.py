import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import my_utils

data_file = sys.argv[1]
out_file = sys.argv[2]
country = sys.argv[3]
title = sys.argv[4]
x=sys.argv[5]
y=sys.argv[6]

forest_fires = my_utils.get_column(data_file, 0, country, result_column = 3)
avg_temps = my_utils.get_column(data_file, 0, country, result_column = 30)

fig, ax = plt.subplots()
ax.scatter(avg_temps, forest_fires)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlabel(x)
ax.set_ylabel(y)
ax.set_title(title)

plt.savefig(out_file,bbox_inches='tight')