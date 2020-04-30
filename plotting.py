import matplotlib.pyplot as plt
import numpy as np

# plotting_req
def plotting_req():
    # d_VM = {} # epoch: # of req
    # d_SLS = {}
    # d_provisioned = {}
    # d_VM_TAtime = []
    # d_SLS_TAtime = []
    # with open('/Users/muyun/Research/evaluation/t3_medium_1_sec_img_load/serverless_hybrid_update_150_0.8.log_request_t3_medium_1_sec_img_load') as f:
    #     for line in f:
    #         # if "!!" not in line:
    #         #     continue
    #         try:
    #             l = line.split("!!")[1].split(": ")
    #         except:
    #             continue
    #         if "(VM)" == l[0]:
    #             data = l[2].split(", ")
    #             if int(data[0]) not in d_VM:
    #                 d_VM[int(data[0])] = 1
    #             else:
    #                 d_VM[int(data[0])] = d_VM[int(data[0])] + 1
    #             if len(data) < 8:
    #                 d_VM_TAtime.append(0.0)
    #                 continue
    #             d_VM_TAtime.append(float(data[4]))
    #         if "(Serverless)" == l[0]:
    #             data = l[2].split(", ")
    #             if int(data[0]) not in d_SLS:
    #                 d_SLS[int(data[0])] = 1
    #             else:
    #                 d_SLS[int(data[0])] = d_SLS[int(data[0])] + 1
    #             if len(data) < 6:
    #                 d_SLS_TAtime.append(0.0)
    #                 continue
    #             d_SLS_TAtime.append(float(data[4]))
    #         if "(provisioned)" == l[0]:
    #             data = l[2].split(", ")
    #             d_provisioned[int(data[0])] = int(data[1])


    # colors = list("rgbcmyk")
    if(len(d_VM) > 0):
        # lists = sorted(d_VM.items())
        # x, y = zip(*lists)
        # fig = plt.figure(0)
        # fig.suptitle('number of requests (VM)', fontsize=20)
        # plt.xlabel('epoch')
        # plt.ylabel('number of requests')
        # plt.scatter(x,y, s=2)
        # plt.legend(d_VM.keys())
        # # plt.savefig('plot0.pdf', dpi=600, bbox_inches='tight')
        plt.show()
        print("Figure 0 done!")
    if(len(d_SLS) > 0):
        # lists = sorted(d_SLS.items())
        # x, y = zip(*lists)
        # fig = plt.figure(1)
        # fig.suptitle('number of requests (SLS)', fontsize=20)
        # plt.xlabel('epoch')
        # plt.ylabel('number of requests')
        # plt.scatter(x,y, s=2)
        # plt.legend(d_SLS.keys())
        # plt.savefig('plot1.pdf', dpi=600, bbox_inches='tight')
        # plt.show()
        print("Figure 1 done!")

    if (len(d_provisioned) > 0):
        # fig = plt.figure(2)
        # fig.suptitle('number of VM to provisioned', fontsize=20)
        # lists = sorted(d_provisioned.items())
        # x, y = zip(*lists)
        # plt.xlabel('epoch povisioning')
        # plt.ylabel('number of requests')
        # plt.plot(x, y)
        # plt.savefig('plot2.pdf', dpi=600, bbox_inches='tight')
        # plt.show()
        print("Figure 2 done!")

    # fig = plt.figure(3)
    # fig.suptitle('VM req turn around time', fontsize=20)
    # plt.scatter(list(range(0,len(d_VM_TAtime))), d_VM_TAtime, s=2)
    # plt.xlabel('request')
    # plt.ylabel('turn around time')
    # plt.savefig('plot3.pdf', dpi=600, bbox_inches='tight')
    # plt.show()
    print("Figure 3 done!")

    # print(str(d_SLS_TAtime))
    # fig = plt.figure(4)
    # fig.suptitle('SLS req turn around time', fontsize=20)
    # plt.xlabel('request')
    # plt.ylabel('turn around time')
    # plt.scatter(list(range(0, len(d_SLS_TAtime))), d_SLS_TAtime, s=2)
    # plt.savefig('plot4.pdf', dpi=600, bbox_inches='tight')
    # plt.show()
    print("Figure 4 done!")

def plotting_VM():
    d_duration = {}

    with open('20200428_Hybrid') as f:
        index = 0
        for line in f:
            print(line)
            data = line.split("!!")[1].split(": ")

            if data[0] == "(duration)":
                data = data[2].split(", ")
                print(data)
                d_duration[index] = [float(data[2]), float(data[3])]
                index += 1
                print(d_duration)

    # print(d_duration)
    fig = plt.figure(5)
    fig.suptitle('VM duration', fontsize=20)
    plt.xlabel('time')
    plt.ylabel('VM index')
    for key, value in d_duration.items():
        print(key)
        print(value)
        plt.plot((value[0], value[1]), (key, key))
    plt.savefig('plot5.pdf', dpi=600, bbox_inches='tight')
    # plt.legend(d_duration.keys())
    # plt.show()
    print("Figure 5 done!")


plotting_req()
plotting_VM()
