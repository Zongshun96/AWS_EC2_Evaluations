import os
import sys

import Hybrid_utils
import SLS_utils
import VM_utils
import plot_bar
import readLog_utils
import plot_cdf
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

figfolder = "figs"
if len(sys.argv) >= 2:
    figfolder = sys.argv[1]
os.makedirs(figfolder, exist_ok=True)

hybrid_req_logdata = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/9_serverless_hybrid_update_150_0.8.log_request_t3_medium_1_sec_img_load")
hybrid_vm_logdata  = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/9_20200508_hybrid_4_req_per_vm_pos_std")
SLS_req_logdata    = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/8_serverless_serverless_update_150_0.8.log_request_1_sec_img_load")
MAXVM_req_logdata  = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/2_serverless_vm_cloud_max_update_150_0.8.log_request_7_t3_medium_1_sec_img_load")
MAXVM_vm_logdata   = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/2_20200428_MAX_VM")

# testing
VM_req_logdata     = readLog_utils.readLog("serverless_vm_cloud_update_150_0.8.log_request")
VM_vm_logdata      = readLog_utils.readLog("25_testing")


# testing
# VM_req_logdata     = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/14_serverless_vm_cloud_update_150_0.8.log_request_VM_step_2_240_40_40_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_and_monitoring_new_alarm_2_pts_in_2_mins_pre-load_with_4_req_per_VM")
# VM_vm_logdata      = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/14_20200510_VM_step_2_240_40_40_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_and_monitoring_new_alarm_2_pts_in_2_mins_pre-load_with_4_req_per_VM")

# 4reqs_step_wait_server_init_3_vm
# VM_req_logdata     = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/10_serverless_vm_cloud_update_150_0.8.log_request_target_step_2_240_20_20_per_vm_3_to_1_to_9_t3_medium_1_sec_img_load_wait_for_server")
# VM_vm_logdata      = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/10_20200508_VM_step_2_240_20_20_req_per_vm_3_to_1_to_9_pos_std_wait_for_server")

# 4reqs_step
# VM_req_logdata     = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/5_serverless_vm_cloud_update_150_0.8.log_request_step_2_240_20_20_per_vm_1_to_1_to_9_t3_medium_1_sec_img_load")
# VM_vm_logdata      = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/5_20200507_VM_step_2_240_20_20_per_vm_1_to_1_to_9_pos_std")

# 4reqs_target
# VM_req_logdata     = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/4_serverless_vm_cloud_update_150_0.8.log_request_1_to_9_t3_medium_1_sec_img_load")
# VM_vm_logdata      = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/4_20200507_VM_Target_240_req_per_vm_1_to_1_to_9_pos_std")

# 4reqs_target_wait_server
# VM_req_logdata     = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/6_serverless_vm_cloud_update_150_0.8.log_request_target_240_per_vm_1_to_1_to_9_t3_medium_1_sec_img_load_wait_for_server")
# VM_vm_logdata      = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/6_20200507_VM_240_req_per_vm_1_to_1_to_9_pos_std_wait_for_server")

# 4reqs_step_wait_server
# VM_req_logdata     = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/7_serverless_vm_cloud_update_150_0.8.log_request_target_step_2_240_20_20_per_vm_1_to_1_to_9_t3_medium_1_sec_img_load_wait_for_server")
# VM_vm_logdata      = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/7_20200507_VM_step_2_240_20_20_req_per_vm_1_to_1_to_9_pos_std_wait_for_server")

Hybridprice_SLS, Hybridprice_Hybrid, Hybridprice_SUM = Hybrid_utils.price(hybrid_req_logdata, hybrid_vm_logdata)

SLSprice = SLS_utils.price(SLS_req_logdata)
MAXVMprice = VM_utils.price(MAXVM_vm_logdata)
VMprice = VM_utils.price(VM_vm_logdata)
priceBarplot = plot_bar.plot_price([Hybridprice_SUM/Hybridprice_SUM, SLSprice/Hybridprice_SUM, MAXVMprice/Hybridprice_SUM, VMprice/Hybridprice_SUM], ['hybrid', 'serverless', 'max_provison', "auto_scaling"], ['g', 'k', 'r', 'b'], "out_file")
priceBarplot.savefig(figfolder+"/cost_bar.pdf")


# CDF comparing all
fig, ax = plt.subplots(1, 1)
temp = []
temp.extend(hybrid_req_logdata.d_SLS_TAtime)
temp.extend(hybrid_req_logdata.d_VM_TAtime)
Hybrid_total_cdf = plot_cdf.plot_con(temp, "g", ax)
plot_cdf.plot_con(SLS_req_logdata.d_SLS_TAtime, "k", ax)
plot_cdf.plot_con(MAXVM_req_logdata.d_VM_TAtime, "m", ax)
plot_cdf.plot_con(VM_req_logdata.d_VM_TAtime, "b", ax)
plt.legend(("hybrid", "serverless", "max_vm", "vm"), loc='best')
plt.savefig(figfolder+"/comp_cdf_all.pdf")





# hybrid
plt.rcParams.update({'font.size': 4})
fig, ax = plt.subplots(3, 2)
fig.tight_layout(pad=6.0)


SLS_utils.Num_Req_to_SLS(SLS_req_logdata, ax[0][0])
ax[0][0].axis([0, 600, 0, 30])

Hybrid_utils.Num_Req_to_VM(hybrid_req_logdata, ax[0][1])
ax[0][1].axis([0, 600, 0, 30])

Hybrid_utils.Num_Req_to_SLS(hybrid_req_logdata, ax[1][0])
ax[1][0].axis([0, 600, 0, 30])



temp = []
temp.extend(hybrid_req_logdata.d_SLS_TAtime)
temp.extend(hybrid_req_logdata.d_VM_TAtime)
Hybrid_total_cdf = plot_cdf.plot_con(temp, "b", ax[1][1])
SLS_cdf = plot_cdf.plot_con(hybrid_req_logdata.d_VM_TAtime, "g", ax[1][1])
VM_cdf = plot_cdf.plot_con(hybrid_req_logdata.d_SLS_TAtime, "r", ax[1][1])
ax[1][1].legend(("all", "serverless", "vm"), loc='best')

Hybrid_utils.VM_Req_TurnAround_time(hybrid_req_logdata, ax[2][0])
Hybrid_utils.SLS_Req_TurnAround_time(hybrid_req_logdata, ax[2][1])
# Hybrid_utils.VM_Req_Fail(hybrid_req_logdata, ax[3][0])
# Hybrid_utils.SLS_Req_Fail(hybrid_req_logdata, ax[3][1])
plt.savefig(figfolder+'/hybrid_progress.pdf', dpi=1200, bbox_inches='tight')


# SLS
fig, ax = plt.subplots(2, 1)
SLS_utils.plot_progress(SLS_req_logdata, ax)
# SLS_utils.SLS_Req_Fail(SLS_req_logdata, ax[2])
plt.savefig(figfolder+'/serv_perf.pdf', dpi=1200, bbox_inches='tight')

# MAX_VM
fig, ax = plt.subplots(2, 1)
VM_utils.plot_progress(MAXVM_req_logdata, MAXVM_vm_logdata, ax)
# VM_utils.VM_Req_Fail(MAXVM_req_logdata, ax[2])
plt.savefig(figfolder+'/all_vm_perf.pdf', dpi=1200, bbox_inches='tight')

# VM_AutoScaling
fig, ax = plt.subplots(3, 1)
VM_utils.plot_progress(VM_req_logdata, VM_vm_logdata, ax)
VM_utils.VM_healthy(VM_req_logdata, ax[2])
# VM_utils.VM_Req_Fail(VM_req_logdata, ax[3])
plt.savefig(figfolder+'/vm_autoscaling_perf.pdf', dpi=1200, bbox_inches='tight')