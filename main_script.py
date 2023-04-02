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
# LIBRA_price = (float(hybrid_req_logdata.d_timestamp_of_decision[-1])-float(hybrid_req_logdata.d_timestamp_of_decision[0])) / 1800 * 0.0116 # note that here no need to divide 1000. That is s bug I made earlier when logging duration of VM, specificly the dict d in VM_utils
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

# .eps', format='eps'


# ========================================================================================================================
# plot trace
fig, ax = plt.subplots(1, 1)
Hybrid_utils.Num_Req_to_Either(hybrid_req_logdata, ax)
plt.savefig(figfolder+'/real_eval_trace.pdf', format='pdf', dpi=1200, bbox_inches='tight')
# ========================================================================================================================
# ========================================================================================================================
# price and SLA bar
Hybridprice_SLS, Hybridprice_Hybrid, Hybridprice_SUM = Hybrid_utils.price(hybrid_req_logdata, hybrid_vm_logdata)
# Hybridprice_Hybrid = Hybridprice_Hybrid +LIBRA_price
# Hybridprice_SUM = Hybridprice_SUM +LIBRA_price
SLSprice = SLS_utils.price(SLS_req_logdata)
MAXVMprice = VM_utils.price(MAXVM_vm_logdata)
VMprice = VM_utils.price(VM_vm_logdata)
VMHideprice_SLS, VMHideprice_Hybrid, VMHideprice_SUM = Hybrid_utils.price(VM_hide_req_logdata, VM_hide_vm_logdata)
# priceBarplot = plot_bar.plot_price([Hybridprice_SUM/Hybridprice_SUM, SLSprice/Hybridprice_SUM, MAXVMprice/Hybridprice_SUM, VMprice/Hybridprice_SUM, VMHideprice_SUM/Hybridprice_SUM], ['hybrid', 'serverless', 'max_provison', "auto_scaling", "auto_scaling_hide"], ['g', 'k', 'r', 'b', 'aqua'], "out_file")
# labels = ['hybrid', 'serverless', 'max_provison', "auto_scaling", "auto_scaling_hide"]
labels = ['LIBRA', 'FaaS', 'MAX', 'SPOCK', 'AUTO']
Libra_cost = Hybridprice_SUM + 0.5*0.0116 + 0.5*(0.0225+0.008)  # 0.5 hour * ( SLS + t2.micro for LIBRA gateway + t3.medium for request + ALB )
SLS_cost = SLSprice
MAX_cost = MAXVMprice + 0.5*(0.0225+0.008)
SPOCK_cost =VMHideprice_SUM + 0.5*(0.0225+0.008)
AUTO_cost = VMprice + 0.5*(0.0225+0.008)
# costs = [(Hybridprice_SUM + LIBRA_price + 300/60/60*(0.0225+0.008))/(Hybridprice_SUM + LIBRA_price + 300/60/60*(0.0225+0.008)), (SLSprice)/(Hybridprice_SUM + LIBRA_price + 300/60/60*(0.0225+0.008)), (MAXVMprice + 300/60/60*(0.0225+0.008))/(Hybridprice_SUM + LIBRA_price + 300/60/60*(0.0225+0.008)), (VMHideprice_SUM + 300/60/60*(0.0225+0.008))/(Hybridprice_SUM + LIBRA_price + 300/60/60*(0.0225+0.008)), (VMprice + 300/60/60*(0.0225+0.008))/(Hybridprice_SUM + LIBRA_price + 300/60/60*(0.0225+0.008))]
costs = [Libra_cost/Libra_cost, SLS_cost/Libra_cost, MAX_cost/Libra_cost, SPOCK_cost/Libra_cost, AUTO_cost/Libra_cost]
sla_violations_percent = [
                  100*sum(list(hybrid_req_logdata.d_either_num_of_fail.values())) /sum(list(hybrid_req_logdata.d_either_num_of_req.values())),
                  100*sum(list(SLS_req_logdata.d_either_num_of_fail.values()))    /sum(list(SLS_req_logdata.d_either_num_of_req.values())),
                  100*sum(list(MAXVM_req_logdata.d_either_num_of_fail.values()))  /sum(list(MAXVM_req_logdata.d_either_num_of_req.values())),
                  100*sum(list(VM_hide_req_logdata.d_either_num_of_fail.values()))/sum(list(VM_hide_req_logdata.d_either_num_of_req.values())),
                  100*sum(list(VM_req_logdata.d_either_num_of_fail.values()))     /sum(list(VM_req_logdata.d_either_num_of_req.values()))
                  ]
# print("===================================")
# print(costs)
# print(sla_violations_percent)
priceBarplot = plot_bar.plot_price_and_SLA_violation(5, labels, costs, sla_violations_percent, 'Normalized Cost', 'SLO Violations', 'Normalized Cost', '%', "++", "//", "b", "r")
priceBarplot.savefig(figfolder+"/real_cost_bar.pdf", format='pdf')
# ========================================================================================================================
# ========================================================================================================================
# duration bar for VM
labels = ['LIBRA', 'AUTO', 'SPOCK']
# LIBRA_price = float(hybrid_vm_logdata.d_timestamp_of_decision[-1])-float(hybrid_vm_logdata.d_timestamp_of_decision[0]) / 1000 / 1800 * 0.0416
durations = [(sum(hybrid_vm_logdata.d_VM_duration)/1000) / (sum(hybrid_vm_logdata.d_VM_duration)/1000), (sum(VM_vm_logdata.d_VM_duration)/1000) / (sum(hybrid_vm_logdata.d_VM_duration)/1000), (sum(VM_hide_vm_logdata.d_VM_duration)/1000) / (sum(hybrid_vm_logdata.d_VM_duration)/1000)]
durationBarplot = plot_bar.plot_a(3, labels, durations, "//")
durationBarplot.savefig(figfolder+"/real_vm_uptime.pdf", format='pdf')
# ========================================================================================================================
# ========================================================================================================================
# price bars for individual VM and SER
priceBarplot = plt.figure()
ax1 = plt.subplot(1, 1, 1)
ax1.set_ylim(0, 0.3 + max([Libra_cost/Libra_cost, (VMprice+ 0.5*(0.0225+0.008))/Libra_cost, (VMHideprice_SLS+VMHideprice_Hybrid+ 0.5*(0.0225+0.008))/Libra_cost]) + 0.2)
labels = ['LIBRA', 'AUTO', 'SPOCK']
ser_costs = [(Hybridprice_SLS)/Libra_cost, 0, (VMHideprice_SLS)/Libra_cost]
libra_costs = [(0.5*0.0116)/Libra_cost, 0, 0]
alb_costs = [(0.5*(0.0225+0.008))/Libra_cost, (0.5*(0.0225+0.008))/Libra_cost, (0.5*(0.0225+0.008))/Libra_cost]
vm_costs = [(Hybridprice_Hybrid)/Libra_cost, (VMprice)/Libra_cost, (VMHideprice_Hybrid)/Libra_cost]
# print(ser_costs)
# print(libra_costs)
# print(alb_costs)
# print(vm_costs)
# print(Hybridprice_SLS)
# print(Hybridprice_Hybrid)
# print(Hybridprice_SUM)
empty_costs = [0,0,0]

plot_bar.plot_a_stack(3, labels, ser_costs, "FaaS Cost", "Normalized Cost", "++", "none", "g", ax1, [sum(x) for x in zip(libra_costs, alb_costs, vm_costs)])
plot_bar.plot_a_stack(3, labels, libra_costs, "LG Cost", "Normalized Cost", "", "black", "black", ax1, [sum(x) for x in zip(alb_costs, vm_costs)])
plot_bar.plot_a_stack(3, labels, [sum(x) for x in zip(alb_costs, vm_costs)], "IaaS Cost", "Normalized Cost", "//", "none", "b", ax1, empty_costs)
# plot_bar.plot_a_stack(3, labels, alb_costs, "ALB Cost", "Normalized Cost", "xx", "r", ax1, vm_costs)
# plot_bar.plot_a_stack(3, labels, vm_costs, "VM Cost", "Normalized Cost", "//", "b", ax1, empty_costs)

# sls_costs = [Hybridprice_SLS, 0, VMHideprice_SLS]
# vm_costs = [Hybridprice_Hybrid + LIBRA_price, VMprice, VMHideprice_Hybrid]
# plot_bar.plot_a_and_b_violation_side(3, labels, sls_costs,  vm_costs, "SER Cost", "VM Cost", "Cost", "//", "++", "g", "g", ax1)
# priceBarplot = plot_bar.plot_a_and_b_violation_side(3, labels, sls_costs,  vm_costs, "SER Cost", "VM Cost", "Cost", "//", "++", "r", "b")

# print("========================================================================================================================")
# print("libra SER cost     : " + str(Hybridprice_SLS))
# print("libra VM cost      : " + str(Hybridprice_Hybrid))
# print("libra instance cost: " + str(LIBRA_price))
# print("libra ALB cost     : " + str(300/60/60*(0.0225+0.008)))
# print("libra total cost   : " + str(Hybridprice_SLS+ Hybridprice_Hybrid + LIBRA_price + 300/60/60*(0.0225+0.008)))
# print("(libra instance cost)/(libra total cost)                 : " + str((LIBRA_price)/(Hybridprice_SLS+ Hybridprice_Hybrid + LIBRA_price + 300/60/60*(0.0225+0.008))))
# print("(libra instance cost)/(libra total cost without ALB cost): " + str((LIBRA_price)/(Hybridprice_SLS+ Hybridprice_Hybrid + LIBRA_price)))
# print("========================================================================================================================")
# print("AUTO VM cost       : " + str(VMprice))
# print("AUTO ALB cost      : " + str(300/60/60*(0.0225+0.008)))
# print("AUTO total cost    : " + str(VMprice + 300/60/60*(0.0225+0.008)))
# print("========================================================================================================================")
# print("SPOCK SER cost     : " + str(VMHideprice_SLS))
# print("SPOCK VM cost      : " + str(VMHideprice_Hybrid))
# print("SPOCK ALB cost     : " + str(300/60/60*(0.0225+0.008)))
# print("SPOCK total cost   : " + str(VMHideprice_Hybrid + VMHideprice_SLS + 300/60/60*(0.0225+0.008)))
# print("========================================================================================================================")

ax1.legend(prop={'size': 20}, loc="upper center", ncol = 2)
ax1.grid(True)
# plt.tight_layout()
priceBarplot.savefig(figfolder+"/real_cost_break_down_norm.pdf", format='pdf')
# ========================================================================================================================
# ========================================================================================================================
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

plt.legend(("LIBRA", "FaaS", "MAX", "SPOCK", "AUTO"), loc='best')
plt.savefig(figfolder+"/real_cdf_all.pdf", format='pdf')
# ========================================================================================================================




# hybrid
plt.rcParams.update({'font.size': 4})
fig, ax = plt.subplots(4, 2)
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
VM_utils.VM_duration(hybrid_vm_logdata, ax[3][0])
VM_utils.VM_healthy(hybrid_req_logdata, ax[3][1])
plt.savefig(figfolder+'/hybrid_progress.pdf', format='pdf', dpi=1200, bbox_inches='tight')




# SLS
fig, ax = plt.subplots(2, 1)
SLS_utils.plot_progress(SLS_req_logdata, ax)
# SLS_utils.SLS_Req_Fail(SLS_req_logdata, ax[2])
plt.savefig(figfolder+'/serv_perf.pdf', format='pdf', dpi=1200, bbox_inches='tight')

# MAX_VM
fig, ax = plt.subplots(2, 1)
VM_utils.plot_progress(MAXVM_req_logdata, MAXVM_vm_logdata, ax)
# VM_utils.VM_Req_Fail(MAXVM_req_logdata, ax[2])
plt.savefig(figfolder+'/all_vm_perf.pdf', format='pdf', dpi=1200, bbox_inches='tight')

# VM_AutoScaling
fig, ax = plt.subplots(3, 1)
VM_utils.plot_progress(VM_req_logdata, VM_vm_logdata, ax)
# VM_utils.VM_duration(VM_vm_logdata, ax[2])
VM_utils.VM_healthy(VM_req_logdata, ax[2])
# VM_utils.VM_Req_Fail(VM_req_logdata, ax[3])
plt.savefig(figfolder+'/vm_autoscaling_perf.pdf', format='pdf', dpi=1200, bbox_inches='tight')

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
plt.savefig(figfolder+'/vm_hide_progress.pdf', format='pdf', dpi=1200, bbox_inches='tight')