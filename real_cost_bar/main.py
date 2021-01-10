# ========================================================================================================================
# price and SLA bar
# import os
import readLog_utils
# import VM_utils, Hybrid_utils, SLS_utils, readLog_utils
# import plot_bar

hybrid_req_logdata = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/28_20200515_hybrid_4_req_per_vm_pos_std_1800_total_")
hybrid_vm_logdata  = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/28_20200515_hybrid_4_req_per_vm_pos_std_1800_total")

# SLS_req_logdata    = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/26_serverless_serverless_update_150_0.8.log_request_1_sec_img_load_1800_total_")

# MAXVM_req_logdata  = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/27_20200515_MAXVM_4_per_VM_1800_total_")
# MAXVM_vm_logdata   = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/27_20200515_MAXVM_4_per_VM_1800_total")

# VM_req_logdata     = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/37_20200518_VM_simple_2_240_-100_-140_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total_")
# VM_vm_logdata      = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/37_20200518_VM_simple_2_240_-100_-140_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total")

# VM_hide_req_logdata     = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/43_20200518_VM_hide_simple_2_240_-100_-140_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total_")
# VM_hide_vm_logdata      = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/43_20200518_VM_simple_2_240_-100_-140_req_per_vm_3_to_1_to_9_pos_std_wait_for_server_new_alarm_1_pts_in_1_1_min_pts_scaling_per_300_sec_1800_total")



# Hybridprice_SLS, Hybridprice_Hybrid, Hybridprice_SUM = Hybrid_utils.price(hybrid_req_logdata, hybrid_vm_logdata)
# SLSprice = SLS_utils.price(SLS_req_logdata)
# MAXVMprice = VM_utils.price(MAXVM_vm_logdata)
# VMprice = VM_utils.price(VM_vm_logdata)
# VMHideprice_SLS, VMHideprice_Hybrid, VMHideprice_SUM = Hybrid_utils.price(VM_hide_req_logdata, VM_hide_vm_logdata)
# # priceBarplot = plot_bar.plot_price([Hybridprice_SUM/Hybridprice_SUM, SLSprice/Hybridprice_SUM, MAXVMprice/Hybridprice_SUM, VMprice/Hybridprice_SUM, VMHideprice_SUM/Hybridprice_SUM], ['hybrid', 'serverless', 'max_provison', "auto_scaling", "auto_scaling_hide"], ['g', 'k', 'r', 'b', 'aqua'], "out_file")
# # labels = ['hybrid', 'serverless', 'max_provison', "auto_scaling", "auto_scaling_hide"]
# labels = ['LIBRA', 'SER', 'MAX', 'SPOCK', 'AUTO']
# costs = [(Hybridprice_SUM + 300/60/60*0.0225)/Hybridprice_SUM, (SLSprice)/Hybridprice_SUM, (MAXVMprice + 300/60/60*0.0225)/Hybridprice_SUM, (VMHideprice_SUM + 300/60/60*0.0225)/Hybridprice_SUM, (VMprice + 300/60/60*0.0225)/Hybridprice_SUM]
# sla_violations_percent = [
#                   100*sum(list(hybrid_req_logdata.d_either_num_of_fail.values())) /sum(list(hybrid_req_logdata.d_either_num_of_req.values())),
#                   100*sum(list(SLS_req_logdata.d_either_num_of_fail.values()))    /sum(list(SLS_req_logdata.d_either_num_of_req.values())),
#                   100*sum(list(MAXVM_req_logdata.d_either_num_of_fail.values()))  /sum(list(MAXVM_req_logdata.d_either_num_of_req.values())),
#                   100*sum(list(VM_hide_req_logdata.d_either_num_of_fail.values()))/sum(list(VM_hide_req_logdata.d_either_num_of_req.values())),
#                   100*sum(list(VM_req_logdata.d_either_num_of_fail.values()))     /sum(list(VM_req_logdata.d_either_num_of_req.values()))
#                   ]
# priceBarplot = plot_bar.plot_price_and_SLA_violation(5, labels, costs, sla_violations_percent, 'Normalized Cost', 'SLA Violations', 'cost', '%', "++", "//", "b", "r")
# os.makedirs("fig", exist_ok=True)
# priceBarplot.savefig("fig/real_cost_bar.pdf")
# ========================================================================================================================