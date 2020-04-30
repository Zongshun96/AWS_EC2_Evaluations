import matplotlib.pyplot as plt

def price(hybrid_req_logdata, hybrid_vm_logdata):
    # logdata = readLog_utils.readLog("t3_medium_1_sec_img_load/serverless_hybrid_update_150_0.8.log_request_t3_medium_1_sec_img_load")
    # print("SLS duration: "+str(sum(logdata.d_SLS_predict_time)))
    SLS_price = sum(hybrid_req_logdata.d_SLS_predict_time)*0.0000166667*512/1024
    # print("SLS_price: "+str(SLS_price))
    # logdata = readLog_utils.readLog(
    #     "t3_medium_1_sec_img_load/20200428_Hybrid")
    VM_price = sum(hybrid_vm_logdata.d_VM_duration) / 1000 / 3600 * 0.0416
    # print("VM_price:  "+str(VM_price))
    # print("sum_price: "+str(SLS_price+VM_price))
    return SLS_price, VM_price, SLS_price+VM_price


def Num_Req_to_VM(hybrid_req_logdata, ax):
    lists = sorted(hybrid_req_logdata.d_VM_num_of_req.items())
    x, y = zip(*lists)
    # ax = plt.figure(0)
    ax.set_title('number of requests (VM)', fontdict={'fontsize': 4, 'fontweight': 'medium'})
    ax.set_xlabel('epoch', fontdict={'fontsize': 4, 'fontweight': 'medium'})
    ax.set_ylabel('number of requests', fontdict={'fontsize': 4, 'fontweight': 'medium'})
    ax.scatter(x, y, s=2)
    # plt.legend(hybrid_req_logdata.d_VM_num_of_req.keys())
    # ax.plot()
    # plt.savefig('plot0.pdf', dpi=600, bbox_inches='tight')
    # return fig

def Num_Req_to_SLS(hybrid_req_logdata, ax):
    lists = sorted(hybrid_req_logdata.d_SLS_num_of_req.items())
    x, y = zip(*lists)
    # ax = plt.figure()
    ax.set_title('number of requests (SLS)', fontdict={'fontsize': 4, 'fontweight': 'medium'})
    ax.set_xlabel('epoch', fontdict={'fontsize': 4, 'fontweight': 'medium'})
    ax.set_ylabel('number of requests', fontdict={'fontsize': 4, 'fontweight': 'medium'})
    ax.scatter(x, y, s=2)
    # plt.legend(hybrid_req_logdata.d_SLS_num_of_req.keys())
    # ax.plot()
    # plt.savefig('plot1.pdf', dpi=600, bbox_inches='tight')
    # return fig

def Num_VM_Provisioned(hybrid_req_logdata, ax):
    # fig = plt.figure()
    ax.set_title('number of VM provisioned', fontdict={'fontsize': 4, 'fontweight': 'medium'})
    lists = sorted(hybrid_req_logdata.d_provisioned.items())
    x, y = zip(*lists)
    ax.set_xlabel('epoch povisioning', fontdict={'fontsize': 4, 'fontweight': 'medium'})
    ax.set_ylabel('number of requests', fontdict={'fontsize': 4, 'fontweight': 'medium'})
    ax.plot(x, y)
    # plt.savefig('plot2.pdf', dpi=600, bbox_inches='tight')
    # ax.plot()
    # plt.show()
    # print("Figure 2 done!")
    # return fig

def VM_Req_TurnAround_time(hybrid_req_logdata, ax):
    # fig = plt.figure()
    ax.set_title('VM req turn around time', fontdict={'fontsize': 4, 'fontweight': 'medium'})
    ax.scatter(list(range(0, len(hybrid_req_logdata.d_VM_TAtime))), hybrid_req_logdata.d_VM_TAtime, s=2)
    ax.set_xlabel('request', fontdict={'fontsize': 4, 'fontweight': 'medium'})
    ax.set_ylabel('turn around time', fontdict={'fontsize': 4, 'fontweight': 'medium'})
    # ax.plot()
    # return fig

def SLS_Req_TurnAround_time(hybrid_req_logdata, ax):
    # fig = plt.figure()
    ax.set_title('SLS req turn around time', fontdict={'fontsize': 4, 'fontweight': 'medium'})
    ax.set_xlabel('request', fontdict={'fontsize': 4, 'fontweight': 'medium'})
    ax.set_ylabel('turn around time', fontdict={'fontsize': 4, 'fontweight': 'medium'})
    ax.scatter(list(range(0, len(hybrid_req_logdata.d_SLS_TAtime))), hybrid_req_logdata.d_SLS_TAtime, s=2)
    # ax.plot()
    # return fig

def VM_duration(hybrid_vm_logdata, ax):
    # d_duration = {}
    # print(d_duration)
    # fig = plt.figure()
    ax.set_title('VM duration', fontdict={'fontsize': 4, 'fontweight': 'medium'})
    ax.set_xlabel('time', fontdict={'fontsize': 4, 'fontweight': 'medium'})
    ax.set_ylabel('VM index', fontdict={'fontsize': 4, 'fontweight': 'medium'})
    for i in range(len(hybrid_vm_logdata.d_VM_duration)):
        # print(key)
        # print(value)
        ax.plot((hybrid_vm_logdata.d_VM_Launched_Time[i], hybrid_vm_logdata.d_VM_Terminated_Time[i]), (i, i))
    # ax.plot()
    # return fig

def plot_progress(hybrid_req_logdata, hybrid_vm_logdata, ax):
    f1 = Num_Req_to_VM(hybrid_req_logdata, ax[0][0])
    f2 = Num_Req_to_SLS(hybrid_req_logdata, ax[0][1])
    f3 = Num_VM_Provisioned(hybrid_req_logdata, ax[1][0])
    f6 = VM_duration(hybrid_vm_logdata, ax[1][1])
    f4 = VM_Req_TurnAround_time(hybrid_req_logdata, ax[2][0])
    f5 = SLS_Req_TurnAround_time(hybrid_req_logdata, ax[2][1])

    return f1, f2, f3, f4, f5, f6