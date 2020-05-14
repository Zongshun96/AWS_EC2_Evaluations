
import matplotlib.pyplot as plt

def price(SLS_req_logdata):
    # logdata = readLog_utils.readLog("t3_medium_1_sec_img_load/serverless_serverless_update_150_0.8.log_request_1_sec_img_load")
    # readLog("t3_medium_1_sec_img_load/serverless_serverless_update_150_0.8.log_request_1_sec_img_load")
    # print(logdata.d_SLS_predict_time)
    # print(d_SLS_predict_time)
    # print(logdata)
    # print("SLS duration: "+str(sum(logdata.d_SLS_predict_time)))
    SLS_price = sum(SLS_req_logdata.d_SLS_predict_time)*0.0000166667*512/1024
    # print("SLS_price: "+str(SLS_price))
    return SLS_price


def Num_Req_to_SLS(SLS_req_logdata, ax):
    lists = sorted(SLS_req_logdata.d_SLS_num_of_req.items())
    x, y = zip(*lists)
    ax.set_title('Total Requests',fontdict={'fontsize': 8, 'fontweight': 'medium'})
    ax.set_xlabel('epoch')
    ax.set_ylabel('# of requests')
    ax.plot(x, y)
    # ax.scatter(x, y)
    SLS_Req_Fail(SLS_req_logdata, ax)
    VM_Req_Fail(SLS_req_logdata, ax)

def SLS_Req_TurnAround_time(SLS_req_logdata, ax):
    # fig = plt.figure()
    ax.set_title('Performance',fontdict={'fontsize': 8, 'fontweight': 'medium'})
    ax.set_xlabel('request')
    ax.set_ylabel('turn-around time (s)')
    # ax.scatter(list(range(0, len(SLS_req_logdata.d_SLS_TAtime))), SLS_req_logdata.d_SLS_TAtime, s=2)
    ax.scatter(list(SLS_req_logdata.d_SLS_AVG_TAtime_d.keys()), list(SLS_req_logdata.d_SLS_AVG_TAtime_d.values()), s=2)
    # return fig

def SLS_Req_Fail(SLS_req_logdata, ax):
    lists = sorted(SLS_req_logdata.d_SLS_num_of_fail.items())
    if lists:
        x, y = zip(*lists)
        ax.set_title('VM req failure', fontdict={'fontsize': 8, 'fontweight': 'medium'})
        ax.set_xlabel('epoch (s)', fontdict={'fontsize': 4, 'fontweight': 'medium'})
        ax.set_ylabel('failure count', fontdict={'fontsize': 4, 'fontweight': 'medium'})
        ax.plot(x, y)
        # ax.scatter(x, y)
        # ax.scatter(list(range(0, len(hybrid_req_logdata.d_SLS_TAtime))), hybrid_req_logdata.d_SLS_TAtime, s=2)
        # ax.scatter(list(SLS_req_logdata.d_SLS_num_of_fail.keys()), list(SLS_req_logdata.d_SLS_num_of_fail.values()), s=2)

def VM_Req_Fail(SLS_req_logdata, ax):
    lists = sorted(SLS_req_logdata.d_VM_num_of_fail.items())
    if lists:
        x, y = zip(*lists)
        ax.set_title('VM req failure', fontdict={'fontsize': 8, 'fontweight': 'medium'})
        ax.set_xlabel('epoch (s)', fontdict={'fontsize': 4, 'fontweight': 'medium'})
        ax.set_ylabel('failure count', fontdict={'fontsize': 4, 'fontweight': 'medium'})
        ax.plot(x, y)
        # ax.scatter(x, y)
        # ax.scatter(list(range(0, len(hybrid_req_logdata.d_SLS_TAtime))), hybrid_req_logdata.d_SLS_TAtime, s=2)
        # ax.scatter(list(SLS_req_logdata.d_SLS_num_of_fail.keys()), list(SLS_req_logdata.d_SLS_num_of_fail.values()), s=2)

def plot_progress(SLS_req_logdata, ax):
    f1 = Num_Req_to_SLS(SLS_req_logdata, ax[0])
    f2 = SLS_Req_TurnAround_time(SLS_req_logdata, ax[1])
    return f1, f2