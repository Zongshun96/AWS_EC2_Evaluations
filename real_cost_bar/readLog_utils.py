import statistics
import math
class logdata:
    d_VM_num_of_req = {}  # epoch: # of req
    d_SLS_num_of_req = {}
    d_VM_predict_time = []  # epoch: # of req
    d_SLS_predict_time = []
    d_provisioned = {}
    d_VM_TAtime = []
    d_SLS_TAtime = []
    d_VM_duration = []
    d_VM_Launched_Time = []
    d_VM_Terminated_Time = []


    def __init__(self):
        # Instance Variable
        self.d_VM_num_of_req = {}  # epoch: # of req
        self.d_VM_num_of_fail = {}  # epoch: # of fail
        # self.d_VM_num_of_error = {}  # epoch: # of fail
        self.d_SLS_num_of_req = {}
        self.d_SLS_num_of_fail = {}
        # self.d_SLS_num_of_error = {}  # epoch: # of fail
        self.d_either_num_of_fail = {}
        self.d_either_num_of_error = {}
        self.d_either_num_of_violation = {}
        self.d_either_num_of_req = {}
        self.d_VM_predict_time = []
        self.d_VM_predict_time_d = {}
        self.d_VM_AVG_predict_time_d = {}
        self.d_SLS_predict_time = []
        self.d_SLS_predict_time_d = {}
        self.d_SLS_AVG_predict_time_d = {}
        self.d_provisioned = {}
        self.d_VM_TAtime = []
        self.d_VM_TAtime_d = {}
        self.d_VM_AVG_TAtime_d = {}
        self.d_SLS_TAtime = []
        self.d_SLS_TAtime_d = {}
        self.d_SLS_AVG_TAtime_d = {}
        self.d_VM_duration = []
        self.d_VM_Launched_Time = []
        self.d_VM_Terminated_Time = []

        self.d_target_sample_timestamp = []
        self.d_inital_count = []
        self.d_healthy_count = []
        self.d_unhealthy = []
        self.d_unused_count = []
        self.d_draining_count = []
        self.d_unavailable_count = []
        self.d_total_count = []



def readLog(logfile):
    # print(logfile)
    ret = logdata()
    # print(ret.d_SLS_predict_time)
    with open(logfile) as f:
        # print(logfile)
        for line in f:
            if "!!" not in line:
                l = line.split(" ")
                # print(l)
                # if l[4] == "epoch" and l[5] == "701\n":
                #     print(line)
                #     break
                continue
            try:
                l = line.split("!!")[1].split(": ")
            except:
                continue
            if "(VM)" == l[0]:
                data = l[2].split(", ")
                if int(data[0]) not in ret.d_VM_num_of_req:
                    ret.d_VM_num_of_req[int(data[0])] = 1
                else:
                    ret.d_VM_num_of_req[int(data[0])] = ret.d_VM_num_of_req[int(data[0])] + 1
                if int(data[0]) not in ret.d_either_num_of_req:
                    ret.d_either_num_of_req[int(data[0])] = 1
                else:
                    ret.d_either_num_of_req[int(data[0])] = ret.d_either_num_of_req[int(data[0])] + 1
                if len(data) < 8:
                    print(line)
                    ret.d_VM_TAtime.append(math.inf)
                    if(int(data[0]) not in ret.d_VM_num_of_fail):
                        ret.d_VM_num_of_fail[int(data[0])] = 1
                    else:
                        ret.d_VM_num_of_fail[int(data[0])] = ret.d_VM_num_of_fail[int(data[0])] + 1
                    if (int(data[0]) not in ret.d_either_num_of_fail):
                        ret.d_either_num_of_fail[int(data[0])] = 1
                    else:
                        ret.d_either_num_of_fail[int(data[0])] = ret.d_either_num_of_fail[int(data[0])] + 1
                    if (int(data[0]) not in ret.d_either_num_of_error):
                        ret.d_either_num_of_error[int(data[0])] = 1
                    else:
                        ret.d_either_num_of_error[int(data[0])] = ret.d_either_num_of_error[int(data[0])] + 1
                    ret.d_VM_predict_time.append(math.inf)
                    continue
                if float(data[4]) > 1: # violate SLA
                    print(line)
                    if (int(data[0]) not in ret.d_VM_num_of_fail):
                        ret.d_VM_num_of_fail[int(data[0])] = 1
                    else:
                        ret.d_VM_num_of_fail[int(data[0])] = ret.d_VM_num_of_fail[int(data[0])] + 1
                    if (int(data[0]) not in ret.d_either_num_of_fail):
                        ret.d_either_num_of_fail[int(data[0])] = 1
                    else:
                        ret.d_either_num_of_fail[int(data[0])] = ret.d_either_num_of_fail[int(data[0])] + 1
                    if (int(data[0]) not in ret.d_either_num_of_violation):
                        ret.d_either_num_of_violation[int(data[0])] = 1
                    else:
                        ret.d_either_num_of_violation[int(data[0])] = ret.d_either_num_of_violation[int(data[0])] + 1
                ret.d_VM_TAtime.append(float(data[4]))
                ret.d_VM_TAtime_d.setdefault(int(data[0]), []).append(float(data[4]))
                ret.d_VM_predict_time.append(float(data[3]))
                ret.d_VM_predict_time_d.setdefault(int(data[0]), []).append(float(data[3]))
            if "(Serverless)" == l[0]:
                data = l[2].split(", ")
                if int(data[0]) not in ret.d_SLS_num_of_req:
                    ret.d_SLS_num_of_req[int(data[0])] = 1
                else:
                    ret.d_SLS_num_of_req[int(data[0])] = ret.d_SLS_num_of_req[int(data[0])] + 1
                if int(data[0]) not in ret.d_either_num_of_req:
                    ret.d_either_num_of_req[int(data[0])] = 1
                else:
                    ret.d_either_num_of_req[int(data[0])] = ret.d_either_num_of_req[int(data[0])] + 1
                if len(data) < 6: # error
                    print(line)
                    ret.d_SLS_TAtime.append(math.inf)
                    if (int(data[0]) not in ret.d_SLS_num_of_fail):
                        ret.d_SLS_num_of_fail[int(data[0])] = 1
                    else:
                        ret.d_SLS_num_of_fail[int(data[0])] = ret.d_SLS_num_of_fail[int(data[0])] + 1
                    if (int(data[0]) not in ret.d_either_num_of_fail):
                        ret.d_either_num_of_fail[int(data[0])] = 1
                    else:
                        ret.d_either_num_of_fail[int(data[0])] = ret.d_either_num_of_fail[int(data[0])] + 1
                    if (int(data[0]) not in ret.d_either_num_of_error):
                        ret.d_either_num_of_error[int(data[0])] = 1
                    else:
                        ret.d_either_num_of_error[int(data[0])] = ret.d_either_num_of_error[int(data[0])] + 1
                    ret.d_SLS_predict_time.append(math.inf)
                    continue
                if float(data[4]) > 1: # violate SLA
                    print(line)
                    if (int(data[0]) not in ret.d_SLS_num_of_fail):
                        ret.d_SLS_num_of_fail[int(data[0])] = 1
                    else:
                        ret.d_SLS_num_of_fail[int(data[0])] = ret.d_SLS_num_of_fail[int(data[0])] + 1
                    if (int(data[0]) not in ret.d_either_num_of_fail):
                        ret.d_either_num_of_fail[int(data[0])] = 1
                    else:
                        ret.d_either_num_of_fail[int(data[0])] = ret.d_either_num_of_fail[int(data[0])] + 1
                    if (int(data[0]) not in ret.d_either_num_of_violation):
                        ret.d_either_num_of_violation[int(data[0])] = 1
                    else:
                        ret.d_either_num_of_violation[int(data[0])] = ret.d_either_num_of_violation[int(data[0])] + 1
                #     continue
                ret.d_SLS_TAtime.append(float(data[4]))
                ret.d_SLS_TAtime_d.setdefault(int(data[0]), []).append(float(data[4]))
                ret.d_SLS_predict_time.append(float(data[3]))
                ret.d_SLS_predict_time_d.setdefault(int(data[0]), []).append(float(data[3]))
            if "(provisioned)" == l[0]:
                data = l[2].split(", ")
                ret.d_provisioned[int(data[0])] = int(data[1])
            if "(duration)" == l[0]:
                data = l[2].split(", ")
                ret.d_VM_duration.append(float(data[1]))
                ret.d_VM_Launched_Time.append(float(data[2]))
                ret.d_VM_Terminated_Time.append(float(data[3]))
            if "(target)" == l[0]:
                data = l[2].split(", ")
                ret.d_target_sample_timestamp.append(float(data[0]))
                ret.d_inital_count.append(float(data[1]))
                ret.d_healthy_count.append(float(data[2]))
                ret.d_unhealthy.append(float(data[3]))
                ret.d_unused_count.append(float(data[4]))
                ret.d_draining_count.append(float(data[5]))
                ret.d_unavailable_count.append(float(data[6]))
                ret.d_total_count.append(float(data[7]))


        for k, v in ret.d_VM_TAtime_d.items():
            ret.d_VM_AVG_TAtime_d[k] = statistics.mean(v)
        for k, v in ret.d_VM_predict_time_d.items():
            ret.d_VM_AVG_predict_time_d[k] = statistics.mean(v)
        for k, v in ret.d_SLS_TAtime_d.items():
            ret.d_SLS_AVG_TAtime_d[k] = statistics.mean(v)
        for k, v in ret.d_SLS_predict_time_d.items():
            ret.d_SLS_AVG_predict_time_d[k] = statistics.mean(v)

        # print(ret.d_SLS_predict_time)
    return ret