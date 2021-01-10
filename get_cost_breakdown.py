from __future__ import division

from tqdm import tqdm
import matplotlib as mtp
mtp.rcParams.update({'font.size': 16})
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
import json
from matplotlib import font_manager as fm
import math
import sys
import os
import json 
import matplotlib.pyplot as plt
from time import gmtime, strftime
import subprocess
import json
from scipy.stats import sem, t
from scipy import mean
from datetime import datetime
import time
import os
from urlparse import urlparse
markers = ["v", "s", "p", "*", "8", "<", ">"]


def simplify_cdf(data):
	data_len = len(data)
	assert data_len != 0
	cdf = np.arange(data_len) / data_len
	simple_cdf = [0]
	simple_data = [data[0]]

	if data_len > 1:
		simple_cdf.append(1.0 / data_len)
		simple_data.append(data[1])
		for cdf_value, data_value in zip(cdf, data):
			if data_value == simple_data[-1]:
				simple_cdf[-1] = cdf_value
			else:
				simple_cdf.append(cdf_value)
				simple_data.append(data_value)
	assert len(simple_cdf) == len(simple_data)
	simple_cdf.append(1)
	simple_data.append(data[-1])

	return simple_cdf, simple_data

def cdfplot(data_in):
	data = sorted(filter(lambda x: (x is not None and ~np.isnan(x)
									and ~np.isinf(x)),
						 data_in))

	data_len = len(data)
	if data_len == 0:
		return
	simple_cdf, simple_data = simplify_cdf(data)
	return simple_data, simple_cdf

def get_cost(log_file):

	f = open(log_file, 'r')
	serv_serv_cost = []
	serv_req_count = []
	serv_vm_cost = []
	while True:
		line = f.readline()
		if not line: break 

		if 'serverless_cloud - INFO - requests served by serverless at' in line: 
			tok = line.split('|')[-1].strip().split(',')
			serv_serv_cost.append(float(tok[-1]))
			serv_req_count.append(int(tok[-3]))
		if 'vm_cloud - INFO - vm cost' in line:
			tok = line.split('|')[-1].strip().split(',')
			serv_vm_cost.append(float(tok[-1]))
	# print sum(serv_req_count)
	# print log_file, sum(serv_serv_cost), sum(serv_vm_cost)
	# print 'Total Cost:', sum(serv_serv_cost)+sum(serv_vm_cost)
	return sum(serv_serv_cost), sum(serv_vm_cost)



lib_log = 'lib.log'
ser_log = 'ser.log'
max_log = 'max.log'
spock_log = 'spock.log'
auto_log = 'auto.log'


# lib_ser_cost, lib_vm_cost = get_cost(lib_log)
# auto_ser_cost, auto_vm_cost = get_cost(auto_log)
# spock_ser_cost, spock_vm_cost = get_cost(spock_log)
# print (lib_ser_cost, lib_vm_cost)
# print (auto_ser_cost, auto_vm_cost)
# print (spock_ser_cost, spock_vm_cost)



lib_ser_cost, lib_vm_cost = 9.955386165000183, 15.200000000004653
auto_ser_cost, auto_vm_cost = 0, 29.273888888896806
spock_ser_cost, spock_vm_cost = 0.23895439499999985, 29.273888888896806

vm_cost = [lib_vm_cost, auto_vm_cost,spock_vm_cost]
ser_cost = [lib_vm_cost+lib_ser_cost, auto_vm_cost+auto_ser_cost,spock_vm_cost+spock_ser_cost]
labels = ['LIBRA', 'AUTO', 'SPOCK']




x = np.arange(3)
ax1 = plt.subplot(1,1,1)
w = 0.3
plt.xticks(x, labels, rotation=60)
plt.ylabel('cost')
cost_bar =ax1.bar(x, ser_cost, width=w, color='r', align='center', label='Serverless cost')
cost_bar =ax1.bar(x, vm_cost, width=w, color='b', align='center', label='VM cost')

plt.ylabel('$')
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig('uptime.pdf')
plt.show()













