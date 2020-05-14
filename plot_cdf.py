#! /usr/bin/python

from __future__ import division

from tqdm import tqdm

import matplotlib as mtp
mtp.rcParams.update({'font.size': 16})


import matplotlib.pyplot as plt
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
import numpy as np
from scipy.stats import sem, t
# from scipy import mean


from datetime import datetime
import time
import os
# from urlparse import urlparse

import numpy as np

def simplify_cdf(data):
    '''Return the cdf and data to plot
        Remove unnecessary points in the CDF in case of repeated data
        '''
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
    # to have cdf up to 1
    simple_cdf.append(1)
    simple_data.append(data[-1])

    return simple_cdf, simple_data

def cdfplot(data_in):
    """Plot the cdf of a data array
        Wrapper to call the plot method of axes
        """
    # cannot shortcut lambda, otherwise it will drop values at 0
    data = sorted(filter(lambda x: (x is not None and ~np.isnan(x)
                                    and ~np.isinf(x)),
                         data_in))

    data_len = len(data)
    if data_len == 0:
#        LOG.info("no data to plot")
        return
    simple_cdf, simple_data = simplify_cdf(data)

    #label = name
    #line = _axis.plot(simple_data, simple_cdf, drawstyle='steps', label=label)
    return simple_data, simple_cdf
    #adjust_plot()


def plot_con(X, col, ax, Y=[], Z=[]):
    x, y = cdfplot(X)

    # fig = plt.figure()
    ax.plot(x, y,color=col)
    ax.axis([0, 2, 0,1])
    ax.set_title('Response Times',fontdict={'fontsize': 8, 'fontweight': 'medium'})
    ax.set_xlabel("turn-around time (s)")
    ax.set_ylabel("CDF")

    if Y!=[]:
        x, y = cdfplot(Y)
        ax.plot(x, y, color="g")
    if Z!=[]:
        x, y = cdfplot(Z)
        ax.plot(x, y, color="b")



d_VM_num_of_req = {}  # epoch: # of req
d_SLS_num_of_req = {}
d_VM_predict_time = []  # epoch: # of req
d_SLS_predict_time = []
d_provisioned = {}
d_VM_TAtime = []
d_SLS_TAtime = []
def readLog(logfile):
    with open(logfile) as f:
        for line in f:
            if "!!" not in line:
                l = line.split(" ")
                # print(l)
                if l[4] == "epoch" and l[5] == "701\n":
                    print(line)
                    break
                continue
            try:
                l = line.split("!!")[1].split(": ")
            except:
                continue
            if "(VM)" == l[0]:
                data = l[2].split(", ")
                if int(data[0]) not in d_VM_num_of_req:
                    d_VM_num_of_req[int(data[0])] = 1
                else:
                    d_VM_num_of_req[int(data[0])] = d_VM_num_of_req[int(data[0])] + 1
                if len(data) < 8:
                    d_VM_TAtime.append(0.0)
                    continue
                d_VM_TAtime.append(float(data[4]))
                d_VM_predict_time.append(float(data[3]))
            if "(Serverless)" == l[0]:
                data = l[2].split(", ")
                if int(data[0]) not in d_SLS_num_of_req:
                    d_SLS_num_of_req[int(data[0])] = 1
                else:
                    d_SLS_num_of_req[int(data[0])] = d_SLS_num_of_req[int(data[0])] + 1
                if len(data) < 6:
                    d_SLS_TAtime.append(0.0)
                    continue
                d_SLS_TAtime.append(float(data[4]))
                d_SLS_predict_time.append(float(data[3]))
            if "(provisioned)" == l[0]:
                data = l[2].split(", ")
                d_provisioned[int(data[0])] = int(data[1])



# readLog("/Users/muyun/Research/evaluation/t3_medium_1_sec_img_load/serverless_hybrid_update_150_0.8.log_request_t3_medium_1_sec_img_load")
# # plot_con(d_VM_TAtime)
# d_VM_TAtime.extend(d_SLS_TAtime)
# plot_con(d_VM_TAtime)
# # plot_con(d_SLS_TAtime)
