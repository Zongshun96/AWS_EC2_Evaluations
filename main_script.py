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
VM_req_logdata     = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/37_20200518_VM_simple_2_240_-100_-140_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total_")
VM_vm_logdata      = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/37_20200518_VM_simple_2_240_-100_-140_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total")

# VM_req_logdata     = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/26_20200514_VM_simple_2_240_40_40_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total_")
# VM_vm_logdata      = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/26_20200514_VM_simple_2_240_40_40_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total")

# VM_req_logdata     = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/31_20200517_VM_simple_2_240_-40_-80_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total_")
# VM_vm_logdata      = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/31_20200517_VM_simple_2_240_-40_-80_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total")

# VM_req_logdata     = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/32_20200517_VM_simple_2_240_-20_-60_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total_")
# VM_vm_logdata      = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/32_20200517_VM_simple_2_240_-20_-60_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total")

# VM_req_logdata     = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/36_20200518_VM_simple_2_240_-60_-100_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total_")
# VM_vm_logdata      = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/36_20200518_VM_simple_2_240_-60_-100_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total")

# testing
# VM_req_logdata     = readLog_utils.readLog("51_serverless_vm_cloud_update_300_0.8.log_request")
# VM_vm_logdata      = readLog_utils.readLog("51_20200519_VM_simple_2_240_-140_-180_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total")


# hide
VM_hide_req_logdata     = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/43_20200518_VM_hide_simple_2_240_-100_-140_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total_")
VM_hide_vm_logdata      = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/43_20200518_VM_simple_2_240_-100_-140_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total")

# VM_hide_req_logdata     = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/44_20200519_VM_hide_simple_2_240_40_-40_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total_")
# VM_hide_vm_logdata      = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/44_20200519_VM_simple_2_240_40_-40_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total")

# VM_hide_req_logdata     = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/46_20200519_VM_hide_simple_2_240_-40_-80_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total_")
# VM_hide_vm_logdata      = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/46_20200519_VM_hide_simple_2_240_-40_-80_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total")

# VM_hide_req_logdata     = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/47_20200519_VM_hide_simple_2_240_-20_-60_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total_")
# VM_hide_vm_logdata      = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/47_20200519_VM_hide_simple_2_240_-20_-60_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total")

# VM_hide_req_logdata     = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/45_20200519_VM_hide_simple_2_240_-60_-100_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total_")
# VM_hide_vm_logdata      = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/45_20200519_VM_hide_simple_2_240_-60_-100_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total")

# VM_hide_req_logdata     = readLog_utils.readLog("52_20200519_VM_hide_simple_2_240_-140_-180_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total_")
# VM_hide_vm_logdata      = readLog_utils.readLog("52_20200519_VM_hide_simple_2_240_-140_-180_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total")


# hide late
# the good one
# VM_hide_req_logdata     = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/40_20200518_VM_hide_simple_2_240_-100_-140_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total_")
# VM_hide_vm_logdata      = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/40_20200518_VM_simple_2_240_-100_-140_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total")
# reproduce
# VM_hide_req_logdata     = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/48_20200519_VM_hide_late_simple_2_240_-100_-140_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total_")
# VM_hide_vm_logdata      = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/48_20200519_VM_hide_late_simple_2_240_-100_-140_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total")

# VM_hide_req_logdata     = readLog_utils.readLog("50_20200519_VM_hide_simple_2_240_-100_-140_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total_")
# VM_hide_vm_logdata      = readLog_utils.readLog("50_20200519_VM_hide_simple_2_240_-100_-140_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total")




# price bar
Hybridprice_SLS, Hybridprice_Hybrid, Hybridprice_SUM = Hybrid_utils.price(hybrid_req_logdata, hybrid_vm_logdata)
SLSprice = SLS_utils.price(SLS_req_logdata)
MAXVMprice = VM_utils.price(MAXVM_vm_logdata)
VMprice = VM_utils.price(VM_vm_logdata)
VMHideprice_SLS, VMHideprice_Hybrid, VMHideprice_SUM = Hybrid_utils.price(VM_hide_req_logdata, VM_hide_vm_logdata)
# priceBarplot = plot_bar.plot_price([Hybridprice_SUM/Hybridprice_SUM, SLSprice/Hybridprice_SUM, MAXVMprice/Hybridprice_SUM, VMprice/Hybridprice_SUM, VMHideprice_SUM/Hybridprice_SUM], ['hybrid', 'serverless', 'max_provison', "auto_scaling", "auto_scaling_hide"], ['g', 'k', 'r', 'b', 'aqua'], "out_file")
# labels = ['hybrid', 'serverless', 'max_provison', "auto_scaling", "auto_scaling_hide"]
labels = ['LIBRA', 'SER', 'MAX', 'SPOCK', 'AUTO']
costs = [(Hybridprice_SUM + 300/60/60*0.0225)/Hybridprice_SUM, (SLSprice)/Hybridprice_SUM, (MAXVMprice + 300/60/60*0.0225)/Hybridprice_SUM, (VMHideprice_SUM + 300/60/60*0.0225)/Hybridprice_SUM, (VMprice + 300/60/60*0.0225)/Hybridprice_SUM]
sla_violations_percent = [
                  100*sum(list(hybrid_req_logdata.d_either_num_of_fail.values())) /sum(list(hybrid_req_logdata.d_either_num_of_req.values())),
                  100*sum(list(SLS_req_logdata.d_either_num_of_fail.values()))    /sum(list(SLS_req_logdata.d_either_num_of_req.values())),
                  100*sum(list(MAXVM_req_logdata.d_either_num_of_fail.values()))  /sum(list(MAXVM_req_logdata.d_either_num_of_req.values())),
                  100*sum(list(VM_hide_req_logdata.d_either_num_of_fail.values()))/sum(list(VM_hide_req_logdata.d_either_num_of_req.values())),
                  100*sum(list(VM_req_logdata.d_either_num_of_fail.values()))     /sum(list(VM_req_logdata.d_either_num_of_req.values()))
                  ]
priceBarplot = plot_bar.plot_price_and_SLA_violation(5, labels, costs, sla_violations_percent, 'Normalized Cost', 'SLA Violations', 'cost', '%', "++", "//")

priceBarplot.savefig(figfolder+"/cost_bar.pdf")


# duration bar for VM
labels = ['LIBRA', 'AUTO', 'SPOCK']
durations = [sum(hybrid_vm_logdata.d_VM_duration)/1000, sum(VM_vm_logdata.d_VM_duration)/1000, sum(VM_hide_vm_logdata.d_VM_duration)/1000]
durationBarplot = plot_bar.plot_a(3, labels, durations, "//")
durationBarplot.savefig(figfolder+"/vm_duration_bar.pdf")


# price bars for individual VM and SER
labels = ['LIBRA', 'AUTO', 'SPOCK']
sls_costs = [Hybridprice_SLS+Hybridprice_Hybrid, 0, VMHideprice_SLS+VMHideprice_Hybrid]
vm_costs = [Hybridprice_Hybrid, VMprice, VMHideprice_Hybrid]
# priceBarplot = plot_bar.plot_price_and_SLA_violation(3, labels, sls_costs,  vm_costs, "SER Cost", "VM Cost", "SER cost", "VM cost", "/", "\")
priceBarplot = plot_bar.plot_a_and_b_stack(3, labels, sls_costs,  vm_costs, "SER Cost", "VM Cost", "//", "++")
priceBarplot.savefig(figfolder+"/individual_cost_bar.pdf")


# CDF comparing all
fig, ax = plt.subplots(1, 1)
temp = []
temp.extend(hybrid_req_logdata.d_SLS_TAtime)
temp.extend(hybrid_req_logdata.d_VM_TAtime)
Hybrid_total_cdf = plot_cdf.plot_con(temp, "g", ax, "^")
plot_cdf.plot_con(SLS_req_logdata.d_SLS_TAtime, "k", ax, "v")
plot_cdf.plot_con(MAXVM_req_logdata.d_VM_TAtime, "r", ax, "o")
temp = []
temp.extend(VM_hide_req_logdata.d_SLS_TAtime)
temp.extend(VM_hide_req_logdata.d_VM_TAtime)
SPOCK_total_cdf = plot_cdf.plot_con(temp, "aqua", ax, "s")
plot_cdf.plot_con(VM_req_logdata.d_VM_TAtime, "b", ax, "p")

plt.legend(("LIBRA", "SER", "MAX", "SPOCK", "AUTO"), loc='best')
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
Hybrid_total_cdf = plot_cdf.plot_con(temp, "b", ax[1][1], "*")
SLS_cdf = plot_cdf.plot_con(hybrid_req_logdata.d_VM_TAtime, "g", ax[1][1], "+")
VM_cdf = plot_cdf.plot_con(hybrid_req_logdata.d_SLS_TAtime, "r", ax[1][1], "x")
ax[1][1].legend(("all", "serverless", "vm"), loc='best')

Hybrid_utils.VM_Req_TurnAround_time(hybrid_req_logdata, ax[2][0])
Hybrid_utils.SLS_Req_TurnAround_time(hybrid_req_logdata, ax[2][1])
# Hybrid_utils.VM_Req_Fail(hybrid_req_logdata, ax[3][0])
# Hybrid_utils.SLS_Req_Fail(hybrid_req_logdata, ax[3][1])
plt.savefig(figfolder+'/hybrid_progress.pdf', dpi=1200, bbox_inches='tight')


fig, ax = plt.subplots(1, 1)
Hybrid_utils.Num_Req_to_Either(hybrid_req_logdata, ax)
plt.savefig(figfolder+'/hybrid_progress_2.pdf', dpi=1200, bbox_inches='tight')


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
Hybrid_total_cdf = plot_cdf.plot_con(temp, "b", ax[1][1], "*")
SLS_cdf = plot_cdf.plot_con(VM_hide_req_logdata.d_VM_TAtime, "g", ax[1][1], "+")
VM_cdf = plot_cdf.plot_con(VM_hide_req_logdata.d_SLS_TAtime, "r", ax[1][1], "x")
ax[1][1].legend(("all", "serverless", "vm"), loc='best')

Hybrid_utils.VM_Req_TurnAround_time(VM_hide_req_logdata, ax[2][0])
Hybrid_utils.SLS_Req_TurnAround_time(VM_hide_req_logdata, ax[2][1])
VM_utils.VM_duration(VM_hide_vm_logdata, ax[3][0])
VM_utils.VM_healthy(VM_hide_req_logdata, ax[3][1])
plt.savefig(figfolder+'/vm_hide_progress.pdf', dpi=1200, bbox_inches='tight')