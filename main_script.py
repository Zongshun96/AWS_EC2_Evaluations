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

hybrid_req_logdata = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/28_20200515_hybrid_4_req_per_vm_pos_std_1800_total_")
hybrid_vm_logdata  = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/28_20200515_hybrid_4_req_per_vm_pos_std_1800_total")
SLS_req_logdata    = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/26_serverless_serverless_update_150_0.8.log_request_1_sec_img_load_1800_total_")
MAXVM_req_logdata  = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/27_20200515_MAXVM_4_per_VM_1800_total_")
MAXVM_vm_logdata   = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/27_20200515_MAXVM_4_per_VM_1800_total")

# testing
# VM_req_logdata     = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/31_20200517_VM_simple_2_240_-40_-80_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total_")
# VM_vm_logdata      = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/31_20200517_VM_simple_2_240_-40_-80_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total")

# VM_req_logdata     = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/32_20200517_VM_simple_2_240_-20_-60_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total_")
# VM_vm_logdata      = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/32_20200517_VM_simple_2_240_-20_-60_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total")

VM_req_logdata     = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/26_20200514_VM_simple_2_240_40_40_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total_")
VM_vm_logdata      = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/26_20200514_VM_simple_2_240_40_40_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total")

# VM_req_logdata     = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/36_20200518_VM_simple_2_240_-60_-100_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total_")
# VM_vm_logdata      = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/36_20200518_VM_simple_2_240_-60_-100_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total")

# VM_req_logdata     = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/37_20200518_VM_simple_2_240_-100_-140_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total_")
# VM_vm_logdata      = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/37_20200518_VM_simple_2_240_-100_-140_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total")


# hide
# VM_hide_req_logdata     = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/40_20200518_VM_simple_2_240_-100_-140_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total_")
# VM_hide_vm_logdata      = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/40_20200518_VM_simple_2_240_-100_-140_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total")

VM_hide_req_logdata     = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/41_20200518_VM_simple_2_240_+40_-40_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total_")
VM_hide_vm_logdata      = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/41_20200518_VM_simple_2_240_40_-40_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total")


# testing
# VM_hide_req_logdata     = readLog_utils.readLog("39_serverless_vm_cloud_hide_update_300_0.8.log_request")
# VM_hide_vm_logdata      = readLog_utils.readLog("39_20200518_VM_simple_2_240_-100_-140_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total")

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
VMHideprice_SLS, VMHideprice_Hybrid, VMHideprice_SUM = Hybrid_utils.price(VM_hide_req_logdata, VM_hide_vm_logdata)
priceBarplot = plot_bar.plot_price([Hybridprice_SUM/Hybridprice_SUM, SLSprice/Hybridprice_SUM, MAXVMprice/Hybridprice_SUM, VMprice/Hybridprice_SUM, VMHideprice_SUM/Hybridprice_SUM], ['hybrid', 'serverless', 'max_provison', "auto_scaling", "auto_scaling_hide"], ['g', 'k', 'r', 'b', 'aqua'], "out_file")
# priceBarplot = plot_bar.plot_price([Hybridprice_SUM, SLSprice, MAXVMprice, VMprice], ['hybrid', 'serverless', 'max_provison', "auto_scaling"], ['g', 'k', 'r', 'b'], "out_file")
priceBarplot.savefig(figfolder+"/cost_bar.pdf")


# CDF comparing all
fig, ax = plt.subplots(1, 1)
temp = []
temp.extend(hybrid_req_logdata.d_SLS_TAtime)
temp.extend(hybrid_req_logdata.d_VM_TAtime)
Hybrid_total_cdf = plot_cdf.plot_con(temp, "g", ax)
plot_cdf.plot_con(SLS_req_logdata.d_SLS_TAtime, "k", ax)
plot_cdf.plot_con(MAXVM_req_logdata.d_VM_TAtime, "r", ax)
plot_cdf.plot_con(VM_req_logdata.d_VM_TAtime, "b", ax)
temp = []
temp.extend(VM_hide_req_logdata.d_SLS_TAtime)
temp.extend(VM_hide_req_logdata.d_VM_TAtime)
Hybrid_total_cdf = plot_cdf.plot_con(temp, "aqua", ax)
plt.legend(("hybrid", "serverless", "max_vm", "vm", "vm_hide"), loc='best')
plt.savefig(figfolder+"/comp_cdf_all.pdf")





# hybrid
plt.rcParams.update({'font.size': 4})
fig, ax = plt.subplots(3, 2)
fig.tight_layout(pad=6.0)


Hybrid_utils.Num_Req_to_Either(hybrid_req_logdata, ax[0][0])
# ax[0][0].axis([0, 600, 0, 30])

Hybrid_utils.Num_Req_to_VM(hybrid_req_logdata, ax[0][1])
# ax[0][1].axis([0, 600, 0, 30])

Hybrid_utils.Num_Req_to_SLS(hybrid_req_logdata, ax[1][0])
# ax[1][0].axis([0, 600, 0, 30])



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
# VM_utils.VM_duration(VM_vm_logdata, ax[2])
VM_utils.VM_healthy(VM_req_logdata, ax[2])
# VM_utils.VM_Req_Fail(VM_req_logdata, ax[3])
plt.savefig(figfolder+'/vm_autoscaling_perf.pdf', dpi=1200, bbox_inches='tight')

# VM_hide_AutoScaling
plt.rcParams.update({'font.size': 4})
fig, ax = plt.subplots(4, 2)
fig.tight_layout(pad=6.0)


Hybrid_utils.Num_Req_to_Either(VM_hide_req_logdata, ax[0][0])
# ax[0][0].axis([0, 600, 0, 30])

Hybrid_utils.Num_Req_to_VM(VM_hide_req_logdata, ax[0][1])
# ax[0][1].axis([0, 600, 0, 30])

Hybrid_utils.Num_Req_to_SLS(VM_hide_req_logdata, ax[1][0])
# ax[1][0].axis([0, 600, 0, 30])

temp = []
temp.extend(VM_hide_req_logdata.d_SLS_TAtime)
temp.extend(VM_hide_req_logdata.d_VM_TAtime)
Hybrid_total_cdf = plot_cdf.plot_con(temp, "b", ax[1][1])
SLS_cdf = plot_cdf.plot_con(VM_hide_req_logdata.d_VM_TAtime, "g", ax[1][1])
VM_cdf = plot_cdf.plot_con(VM_hide_req_logdata.d_SLS_TAtime, "r", ax[1][1])
ax[1][1].legend(("all", "serverless", "vm"), loc='best')

Hybrid_utils.VM_Req_TurnAround_time(VM_hide_req_logdata, ax[2][0])
Hybrid_utils.SLS_Req_TurnAround_time(VM_hide_req_logdata, ax[2][1])
VM_utils.VM_duration(VM_hide_vm_logdata, ax[3][0])
VM_utils.VM_healthy(VM_hide_req_logdata, ax[3][1])
plt.savefig(figfolder+'/vm_hide_progress.pdf', dpi=1200, bbox_inches='tight')