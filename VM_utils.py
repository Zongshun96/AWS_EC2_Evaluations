import logging
import math

import matplotlib.pyplot as plt
import time

# import configuration
from datetime import datetime
import pytz
import boto3

import json

import readLog_utils

logger = logging.getLogger(__name__)
# logging.getLogger('boto').setLevel(logging.CRITICAL)
logging.getLogger('boto3').setLevel(logging.CRITICAL)
logging.getLogger('botocore').setLevel(logging.CRITICAL)

# debug
AutoScalingClient = boto3.client('autoscaling')
# AutoScalingGroup = "20200427_fix_num_VM"

# Last_Epoch = 1587563792.6595685
# First_Epoch = 1587521753.1519208

d = {}
# epoch_tz = datetime.utcfromtimestamp(0).astimezone(pytz.utc)
# epoch = datetime.utcfromtimestamp(0)

def unix_time_millis(tt, t):
    # print(tt.timestamp())
    # print((1587393418.6641715 - t.timestamp()/3600))
    # if tt.timestamp() > Last_Epoch:
    #     # print("!!!!")
    #     return (Last_Epoch - t.timestamp()) * 1000.0
    # else:
    return (tt - t).total_seconds() * 1000.0

def setup_logging(AutoScalingGroup):
    logging.basicConfig(filename=AutoScalingGroup, level=logging.INFO,
                        format='%(name)s - %(levelname)s - %(message)s', filemode='w')
    console = logging.StreamHandler()
    formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    console.setFormatter(formatter)

def pretty(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value))


def PollDurationDict(AutoScalingGroup):
        setup_logging(AutoScalingGroup)
        # global Last_Epoch
        # Last_Epoch = Last_Epoch_
        # global First_Epoch
        # First_Epoch= First_Epoch_
        response = AutoScalingClient.describe_scaling_activities(AutoScalingGroupName=AutoScalingGroup,)
        for a in response["Activities"]:
            if a["Description"].split()[-1] in d and isinstance(d[a["Description"].split()[-1]], float):
                continue
            d_temp={}
            if(a["Description"].split()[-1] in d):
                d_temp = d[a["Description"].split()[-1]]
            if(a["Description"].split()[0] == "Launching"):
                try:
                    d_temp["Launched_Time"]=a["EndTime"]
                except:
                    continue
            if (a["Description"].split()[0] == "Terminating"):
                try:
                    d_temp["Terminating_Time"] = a["StartTime"]
                except:
                    continue
            d[a["Description"].split()[-1]]= d_temp

        return CalculateAndLogDuration(AutoScalingGroup)


def CalculateAndLogDuration(AutoScalingGroup):
    # duration = {}
    # pretty(d)
    duration = 0
    price = 0
    for k, v in d.items():
        # print(v)
        if isinstance(v, float) or "Terminating_Time" not in v or "Launched_Time" not in v:
            continue
        # try:
        #     Termination_Time_object = datetime.strptime(v["Terminating_Time"], '%Y-%m-%d %X%z')
        # except:
        #     Termination_Time_object = datetime.strptime(v["Terminating_Time"], '%Y-%m-%d %X.%f%z')
        # try:
        #     Launched_Time_Time_object = datetime.strptime(v["Launched_Time"], '%Y-%m-%d %X%z')
        # except:
        #     Launched_Time_Time_object = datetime.strptime(v["Launched_Time"], '%Y-%m-%d %X.%f%z')
        # Termination_Time = time.mktime(v["Terminating_Time"].timetuple()) + v["Terminating_Time"].microsecond / 1E6
        Termination_Time = time.mktime(v["Terminating_Time"].timetuple())
        # Launched_Time_Time = time.mktime(v["Launched_Time"].timetuple()) + v["Launched_Time"].microsecond / 1E6
        Launched_Time_Time = time.mktime(v["Launched_Time"].timetuple())
        # d[k] = unix_time_millis(Termination_Time_object, Launched_Time_Time_object)
        try:
            # print(type(v["Terminating_Time"]))
            # print(v["Launched_Time"])
            d[k] = unix_time_millis(v["Terminating_Time"], v["Launched_Time"])
            # print(v["Terminating_Time"])
            # if(Launched_Time_Time >= First_Epoch):
            # print(First_Epoch)
            # print(v["Launched_Time"])
            # print("(duration): InstanceID, duration, Launched_Time, Terminating_Time: " + k + ", " + str(d[k]) + ", " + str(Launched_Time_Time) + ", " + str(Termination_Time))
            logger.info("!!(duration): InstanceID, duration, Launched_Time, Terminating_Time: " + k + ", " + str(d[k]) + ", " + str(Launched_Time_Time) + ", " + str(Termination_Time))
            # print(d[k]/(3600*1000))
            duration = duration + d[k]/1000
            price = d[k]*0.0416/(3600*1000) + price
        except Exception:
            continue

    # logger.info("price: "+ str(price))
    # print(price)
    print("VM duration: "+str(duration))
    with open(AutoScalingGroup+'.txt', 'w') as file:
        file.write(json.dumps(d))
    return price

    # return duration



# config = configuration.configuration()
# setup_logging(config)
# PollDurationDict()
def price(MAXVM_rvm_logdata):
    # config = configuration.configuration()
    # setup_logging(config)
    # logdata = readLog_utils.readLog(
    #     "t3_medium_1_sec_img_load/20200428_MAX_VM")
    # VM_MAX_price = PollDurationDict("20200427_fix_num_VM")
    VM_MAX_price = sum(MAXVM_rvm_logdata.d_VM_duration)/1000/3600*0.0416
    # print("VM_MAX_price: "+str(VM_MAX_price))
    return VM_MAX_price


def Num_Req_to_VM(MAXVM_req_logdata, ax):
    lists = sorted(MAXVM_req_logdata.d_VM_num_of_req.items())
    x, y = zip(*lists)
    # fig = plt.figure(0)
    ax.set_title('number of requests (VM)',fontdict={'fontsize': 8, 'fontweight': 'medium'})
    ax.set_xlabel('epoch')
    ax.set_xlabel('# of requests')
    ax.plot(x, y)
    # ax.scatter(x, y, c="b", s=4)
    VM_Req_Fail(MAXVM_req_logdata, ax)
    SLS_Req_Fail(MAXVM_req_logdata, ax)
    # plt.legend(MAXVM_req_logdata.d_VM_num_of_req.keys())
    # plt.savefig('plot0.pdf', dpi=600, bbox_inches='tight')
    # return fig

def VM_Req_TurnAround_time(MAXVM_req_logdata, ax):
    # fig = plt.figure()
    ax.set_title('Performance', fontdict={'fontsize': 8, 'fontweight': 'medium'})
    # ax.scatter(list(range(0, len(MAXVM_req_logdata.d_VM_TAtime))), MAXVM_req_logdata.d_VM_TAtime, s=2)
    ax.scatter(list(MAXVM_req_logdata.d_VM_AVG_TAtime_d.keys()), list(MAXVM_req_logdata.d_VM_AVG_TAtime_d.values()), s=2)
    ax.set_xlabel('request')
    ax.set_ylabel('turn-around time (s)')
    # return fig

def VM_duration(MAXVM_vm_logdata, ax):
    # find min Launched Time
    min_launched_time = math.inf
    for i in range(len(MAXVM_vm_logdata.d_VM_duration)):
        if MAXVM_vm_logdata.d_VM_Launched_Time[i] < min_launched_time:
            min_launched_time = MAXVM_vm_logdata.d_VM_Launched_Time[i]
    ax.set_title('VM duration')
    ax.set_xlabel('time')
    ax.set_ylabel('VM index')
    for i in range(len(MAXVM_vm_logdata.d_VM_duration)):
        ax.plot((MAXVM_vm_logdata.d_VM_Launched_Time[i],
                 MAXVM_vm_logdata.d_VM_Terminated_Time[i]), (i, i))
        # if MAXVM_vm_logdata.d_VM_Launched_Time[i] < min_launched_time + 6*60:
        #     ax.plot((0, MAXVM_vm_logdata.d_VM_Terminated_Time[i] - (min_launched_time + 6*60)), (i, i))
        # else:
        #     ax.plot((MAXVM_vm_logdata.d_VM_Launched_Time[i] - (min_launched_time + 6*60), MAXVM_vm_logdata.d_VM_Terminated_Time[i] - (min_launched_time + 6*60)), (i, i))

def VM_healthy(MAXVM_req_logdata, ax):
    # find min Launched Time
    ax.set_title('VM healthy count')
    ax.set_xlabel('epoch')
    ax.set_ylabel('VM count')
    min_healthy_index = math.inf
    for i in range(len(MAXVM_req_logdata.d_total_count)):
        if MAXVM_req_logdata.d_total_count[i] != 0:
            min_healthy_index = i
            break
    ax.plot(list(range(0, len(MAXVM_req_logdata.d_healthy_count[i-1:]))), MAXVM_req_logdata.d_healthy_count[i-1:])



def VM_Req_Fail(MAXVM_req_logdata, ax):
    lists = sorted(MAXVM_req_logdata.d_VM_num_of_fail.items())
    if lists:
        x, y = zip(*lists)
        ax.set_title('VM req failure', fontdict={'fontsize': 8, 'fontweight': 'medium'})
        ax.set_xlabel('epoch (s)', fontdict={'fontsize': 4, 'fontweight': 'medium'})
        ax.set_ylabel('failure count', fontdict={'fontsize': 4, 'fontweight': 'medium'})
        # ax.scatter(list(range(0, len(hybrid_req_logdata.d_SLS_TAtime))), hybrid_req_logdata.d_SLS_TAtime, s=2)
        ax.plot(x, y)
        # ax.scatter(x, y, c="y", s=1)
        # ax.scatter(list(MAXVM_req_logdata.d_VM_num_of_fail.keys()), list(MAXVM_req_logdata.d_VM_num_of_fail.values()), s=2)

def SLS_Req_Fail(MAXVM_req_logdata, ax):
    lists = sorted(MAXVM_req_logdata.d_SLS_num_of_fail.items())
    if lists:
        x, y = zip(*lists)
        ax.set_title('VM req failure', fontdict={'fontsize': 8, 'fontweight': 'medium'})
        ax.set_xlabel('epoch (s)', fontdict={'fontsize': 4, 'fontweight': 'medium'})
        ax.set_ylabel('failure count', fontdict={'fontsize': 4, 'fontweight': 'medium'})
        # ax.scatter(list(range(0, len(hybrid_req_logdata.d_SLS_TAtime))), hybrid_req_logdata.d_SLS_TAtime, s=2)
        ax.plot(x, y)
        # ax.scatter(x, y, c="y", s=1)
        # ax.scatter(list(MAXVM_req_logdata.d_VM_num_of_fail.keys()), list(MAXVM_req_logdata.d_VM_num_of_fail.values()), s=2)

def plot_progress(MAXVM_req_logdata, MAXVM_vm_logdata, ax):
    f1 = Num_Req_to_VM(MAXVM_req_logdata, ax[0])
    f2 = VM_Req_TurnAround_time(MAXVM_req_logdata, ax[1])
    # f3 = VM_duration(MAXVM_vm_logdata, ax[2])





if __name__ == "__main__":
    setup_logging("25_testing")
    PollDurationDict("25_testing")
