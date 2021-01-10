# ========================================================================================================================
# price bars for individual VM and SER
import os

import Hybrid_utils, VM_utils, readLog_utils, plot_bar

hybrid_req_logdata = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/28_20200515_hybrid_4_req_per_vm_pos_std_1800_total_")
hybrid_vm_logdata  = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/28_20200515_hybrid_4_req_per_vm_pos_std_1800_total")

VM_req_logdata     = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/37_20200518_VM_simple_2_240_-100_-140_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total_")
VM_vm_logdata      = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/37_20200518_VM_simple_2_240_-100_-140_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total")

VM_hide_req_logdata     = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/43_20200518_VM_hide_simple_2_240_-100_-140_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total_")
VM_hide_vm_logdata      = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/43_20200518_VM_simple_2_240_-100_-140_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total")


Hybridprice_SLS, Hybridprice_Hybrid, Hybridprice_SUM = Hybrid_utils.price(hybrid_req_logdata, hybrid_vm_logdata)
VMprice = VM_utils.price(VM_vm_logdata)
VMHideprice_SLS, VMHideprice_Hybrid, VMHideprice_SUM = Hybrid_utils.price(VM_hide_req_logdata, VM_hide_vm_logdata)


labels = ['LIBRA', 'AUTO', 'SPOCK']
sls_costs = [Hybridprice_SLS+Hybridprice_Hybrid, 0, VMHideprice_SLS+VMHideprice_Hybrid]
vm_costs = [Hybridprice_Hybrid, VMprice, VMHideprice_Hybrid]
# priceBarplot = plot_bar.plot_price_and_SLA_violation(3, labels, sls_costs,  vm_costs, "SER Cost", "VM Cost", "SER cost", "VM cost", "/", "\")
priceBarplot = plot_bar.plot_a_and_b_stack(3, labels, sls_costs,  vm_costs, "SER Cost", "VM Cost", "//", "++")
os.makedirs("fig", exist_ok=True)
priceBarplot.savefig("fig/real_cost_breakdown.pdf")
# ========================================================================================================================