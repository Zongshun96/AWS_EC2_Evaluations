# ========================================================================================================================
# duration bar for VM
import os

import readLog_utils, plot_bar

hybrid_req_logdata = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/28_20200515_hybrid_4_req_per_vm_pos_std_1800_total_")
hybrid_vm_logdata  = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/28_20200515_hybrid_4_req_per_vm_pos_std_1800_total")

VM_req_logdata     = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/37_20200518_VM_simple_2_240_-100_-140_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total_")
VM_vm_logdata      = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/37_20200518_VM_simple_2_240_-100_-140_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total")

VM_hide_req_logdata     = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/43_20200518_VM_hide_simple_2_240_-100_-140_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total_")
VM_hide_vm_logdata      = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/43_20200518_VM_simple_2_240_-100_-140_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total")

labels = ['LIBRA', 'AUTO', 'SPOCK']
durations = [sum(hybrid_vm_logdata.d_VM_duration)/1000, sum(VM_vm_logdata.d_VM_duration)/1000, sum(VM_hide_vm_logdata.d_VM_duration)/1000]
durationBarplot = plot_bar.plot_a(3, labels, durations, "//")
os.makedirs("fig", exist_ok=True)
durationBarplot.savefig("fig/main.py.pdf")
# ========================================================================================================================