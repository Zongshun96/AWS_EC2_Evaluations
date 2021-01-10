from __future__ import division

# from tqdm import tqdm
import matplotlib as mtp
mtp.rcParams.update({'font.size': 16})
# import matplotlib.pyplot as plt
# import numpy as np
# import matplotlib.patches as mpatches
# import json
# from matplotlib import font_manager as fm
# import math
# import sys
# import os
# import json
import matplotlib.pyplot as plt
# from time import gmtime, strftime
# import subprocess
# import json
# from scipy import mean
# import os



wits_file = open('wits_logs.txt', 'r')
berkley_file = open('berkeley_logs.txt', 'r')

alpha = 0.2

wits_data = []
while True:
	line = wits_file.readline()
	if not line: break
	wits_data.append(int(line))


berkley_data = []
while True:
	line = berkley_file.readline()
	if not line: break
	berkley_data.append(int(line))

print(len(wits_data), len(berkley_data))




wits_cum_mean = []
wits_weighted_mean = []
wits_std = []
mean = None 
std = None
for i in range(len(wits_data)):
	wits_cum_mean.append(sum(wits_data[:i+1])/len(wits_data[:i+1]))

	if mean is None:
		mean  = wits_data[i]
		std = 0 
	else:
		mean = (1-alpha)*mean + alpha*wits_data[i]
		std = alpha*std + (1-alpha)*(abs(mean-wits_data[i]))
	wits_weighted_mean.append(mean)
	wits_std.append(std)

berkley_cum_mean = []
berkley_weighted_mean = []
berkley_std = []
mean = None 
std = None
for i in range(len(berkley_data)):
	berkley_cum_mean.append(sum(berkley_data[:i+1])/len(berkley_data[:i+1]))

	if mean is None:
		mean  = berkley_data[i]
		std = 0 
	else:
		mean = (1-alpha)*mean + alpha*berkley_data[i]
		std = alpha*std + (1-alpha)*(abs(mean-berkley_data[i]))
	berkley_weighted_mean.append(mean)
	berkley_std.append(std)


plt.subplot(3, 2, 1)
plt.axis([0, len(wits_data), 0, max(wits_data)])
plt.plot(range(len(wits_data)), wits_data, 'b')
plt.plot(range(len(wits_cum_mean)), wits_cum_mean, 'r')
plt.title('WITS')
plt.ylabel('# of requests')
plt.xlabel('time(s)')
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))


plt.subplot(3, 2, 2)
plt.axis([0, len(berkley_data), 0,max(berkley_data)])
plt.plot(range(len(berkley_data)), berkley_data, 'b')
plt.plot(range(len(berkley_cum_mean)), berkley_cum_mean, 'r')
plt.title('BERKLEY')
plt.ylabel('# of requests')
plt.xlabel('time(s)')
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))



plt.subplot(3, 2, 3)
plt.axis([0, len(wits_data), 0,max(wits_data)])
plt.plot(range(len(wits_data)), wits_data, 'b')
plt.plot(range(len(wits_weighted_mean)), wits_weighted_mean, 'r')
plt.ylabel('# of requests')
plt.xlabel('time(s)')
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))


plt.subplot(3, 2, 4)
plt.axis([0, len(berkley_data), 0,max(berkley_data)])
plt.plot(range(len(berkley_data)), berkley_data, 'b')
plt.plot(range(len(berkley_weighted_mean)), berkley_weighted_mean, 'r')
plt.ylabel('# of requests')
plt.xlabel('time(s)')
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))


plt.subplot(3, 2, 5)
plt.axis([0, len(wits_std), 0,max(wits_std)])
plt.plot(range(len(wits_std)), wits_std, 'r')
plt.ylabel('std (# of requests)')
plt.xlabel('time(s)')
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))


plt.subplot(3, 2, 6)
plt.axis([0, len(berkley_std), 0,max(berkley_std)])
plt.plot(range(len(berkley_std)), berkley_std, 'r')
plt.ylabel('std (# of requests)')
plt.xlabel('time(s)')
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))





plt.savefig('for_today.pdf')
plt.show()


