import matplotlib.pyplot as plt

def price(hybrid_req_logdata, hybrid_vm_logdata):
    SLS_price = sum(hybrid_req_logdata.d_SLS_predict_time)*0.0000166667*512/1024
    VM_price = sum(hybrid_vm_logdata.d_VM_duration) / 1000 / 3600 * 0.0416
    return SLS_price, VM_price, SLS_price+VM_price


def Num_Req_to_VM(hybrid_req_logdata, ax):
    lists = sorted(hybrid_req_logdata.d_VM_num_of_req.items())
    x, y = zip(*lists)
    ax.set_title('number of requests (VM)', fontdict={'fontsize': 8, 'fontweight': 'medium'})
    ax.set_xlabel('epoch', fontdict={'fontsize': 4, 'fontweight': 'medium'})
    ax.set_ylabel('# of requests', fontdict={'fontsize': 4, 'fontweight': 'medium'})
    # ax.plot(x, y, color='g')
    ax.scatter(x, y, color='g')

def Num_Req_to_SLS(hybrid_req_logdata, ax):
    lists = sorted(hybrid_req_logdata.d_SLS_num_of_req.items())
    x, y = zip(*lists)
    ax.set_title('number of requests (SLS)', fontdict={'fontsize': 8, 'fontweight': 'medium'})
    ax.set_xlabel('epoch', fontdict={'fontsize': 4, 'fontweight': 'medium'})
    ax.set_ylabel('# of requests', fontdict={'fontsize': 4, 'fontweight': 'medium'})
    # ax.plot(x, y, color='r')
    ax.scatter(x, y, color='r')

def Num_VM_Provisioned(hybrid_req_logdata, ax):
    ax.set_title('number of VM provisioned', fontdict={'fontsize': 4, 'fontweight': 'medium'})
    lists = sorted(hybrid_req_logdata.d_provisioned.items())
    x, y = zip(*lists)
    ax.set_xlabel('epoch povisioning', fontdict={'fontsize': 4, 'fontweight': 'medium'})
    ax.set_ylabel('number of requests', fontdict={'fontsize': 4, 'fontweight': 'medium'})
    ax.plot(x, y)


def VM_Req_TurnAround_time(hybrid_req_logdata, ax):
    ax.set_title('VM req turn around time', fontdict={'fontsize': 8, 'fontweight': 'medium'})
    # ax.scatter(list(range(0, len(hybrid_req_logdata.d_VM_TAtime))), hybrid_req_logdata.d_VM_TAtime, s=2)
    ax.scatter(list(hybrid_req_logdata.d_VM_AVG_TAtime_d.keys()), list(hybrid_req_logdata.d_VM_AVG_TAtime_d.values()), s=2)
    ax.set_xlabel('epoch (s)', fontdict={'fontsize': 4, 'fontweight': 'medium'})
    ax.set_ylabel('turn-around time (s)', fontdict={'fontsize': 4, 'fontweight': 'medium'})

    VM_Req_Fail(hybrid_req_logdata, ax)


def SLS_Req_TurnAround_time(hybrid_req_logdata, ax):
    ax.set_title('SLS req turn around time', fontdict={'fontsize': 8, 'fontweight': 'medium'})
    ax.set_xlabel('epoch (s)', fontdict={'fontsize': 4, 'fontweight': 'medium'})
    ax.set_ylabel('turn-around time (s)', fontdict={'fontsize': 4, 'fontweight': 'medium'})
    # ax.scatter(list(range(0, len(hybrid_req_logdata.d_SLS_TAtime))), hybrid_req_logdata.d_SLS_TAtime, s=2)
    ax.scatter(list(hybrid_req_logdata.d_SLS_AVG_TAtime_d.keys()), list(hybrid_req_logdata.d_SLS_AVG_TAtime_d.values()), s=2)

def VM_duration(hybrid_vm_logdata, ax):
    ax.set_title('VM duration', fontdict={'fontsize': 4, 'fontweight': 'medium'})
    ax.set_xlabel('time', fontdict={'fontsize': 4, 'fontweight': 'medium'})
    ax.set_ylabel('VM index', fontdict={'fontsize': 4, 'fontweight': 'medium'})
    for i in range(len(hybrid_vm_logdata.d_VM_duration)):
        ax.plot((hybrid_vm_logdata.d_VM_Launched_Time[i], hybrid_vm_logdata.d_VM_Terminated_Time[i]), (i, i))

def VM_Req_Fail(hybrid_req_logdata, ax):
    lists = sorted(hybrid_req_logdata.d_VM_num_of_fail.items())
    if lists:
        x, y = zip(*lists)
        ax.set_title('VM req failure', fontdict={'fontsize': 8, 'fontweight': 'medium'})
        ax.set_xlabel('epoch (s)', fontdict={'fontsize': 4, 'fontweight': 'medium'})
        ax.set_ylabel('failure count', fontdict={'fontsize': 4, 'fontweight': 'medium'})
        # ax.scatter(list(range(0, len(hybrid_req_logdata.d_SLS_TAtime))), hybrid_req_logdata.d_SLS_TAtime, s=2)
        # ax.scatter(list(hybrid_req_logdata.d_VM_num_of_fail.keys()), list(hybrid_req_logdata.d_VM_num_of_fail.values()), s=2)
        ax.plot(x, y)
        # ax.scatter(x, y)

def SLS_Req_Fail(hybrid_req_logdata, ax):
    lists = sorted(hybrid_req_logdata.d_SLS_num_of_fail.items())
    if lists:
        x, y = zip(*lists)
        ax.set_title('VM req failure', fontdict={'fontsize': 8, 'fontweight': 'medium'})
        ax.set_xlabel('epoch (s)', fontdict={'fontsize': 4, 'fontweight': 'medium'})
        ax.set_ylabel('failure count', fontdict={'fontsize': 4, 'fontweight': 'medium'})
        # ax.scatter(list(range(0, len(hybrid_req_logdata.d_SLS_TAtime))), hybrid_req_logdata.d_SLS_TAtime, s=2)
        # ax.scatter(list(hybrid_req_logdata.d_SLS_num_of_fail.keys()), list(hybrid_req_logdata.d_SLS_num_of_fail.values()), s=2)
        ax.plot(x, y)
        # ax.scatter(x, y)