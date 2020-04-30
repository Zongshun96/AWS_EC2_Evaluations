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
        self.d_SLS_num_of_req = {}
        self.d_VM_predict_time = []  # epoch: # of req
        self.d_SLS_predict_time = []
        self.d_provisioned = {}
        self.d_VM_TAtime = []
        self.d_SLS_TAtime = []
        self.d_VM_duration = []
        self.d_VM_Launched_Time = []
        self.d_VM_Terminated_Time = []


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
                if int(data[0]) not in ret.d_VM_num_of_req:
                    ret.d_VM_num_of_req[int(data[0])] = 1
                else:
                    ret.d_VM_num_of_req[int(data[0])] = ret.d_VM_num_of_req[int(data[0])] + 1
                if len(data) < 8:
                    ret.d_VM_TAtime.append(0.0)
                    continue
                ret.d_VM_TAtime.append(float(data[4]))
                ret.d_VM_predict_time.append(float(data[3]))
            if "(Serverless)" == l[0]:
                data = l[2].split(", ")
                if int(data[0]) not in ret.d_SLS_num_of_req:
                    ret.d_SLS_num_of_req[int(data[0])] = 1
                else:
                    ret.d_SLS_num_of_req[int(data[0])] = ret.d_SLS_num_of_req[int(data[0])] + 1
                if len(data) < 6:
                    ret.d_SLS_TAtime.append(0.0)
                    continue
                ret.d_SLS_TAtime.append(float(data[4]))
                ret.d_SLS_predict_time.append(float(data[3]))
            if "(provisioned)" == l[0]:
                data = l[2].split(", ")
                ret.d_provisioned[int(data[0])] = int(data[1])
            if "(duration)" == l[0]:
                data = l[2].split(", ")
                ret.d_VM_duration.append(float(data[1]))
                ret.d_VM_Launched_Time.append(float(data[2]))
                ret.d_VM_Terminated_Time.append(float(data[3]))
    # print(ret.d_SLS_predict_time)
    return ret