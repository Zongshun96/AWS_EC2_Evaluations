import Hybrid_utils
import SLS_utils
import VM_utils
import plot_bar
import readLog_utils
import plot_cdf
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt


hybrid_req_logdata = readLog_utils.readLog("t3_medium_1_sec_img_load/serverless_hybrid_update_150_0.8.log_request_t3_medium_1_sec_img_load")
hybrid_vm_logdata = readLog_utils.readLog("t3_medium_1_sec_img_load/20200428_Hybrid")
SLS_req_logdata = logdata = readLog_utils.readLog("t3_medium_1_sec_img_load/serverless_serverless_update_150_0.8.log_request_1_sec_img_load")
MAXVM_req_logdata = logdata = readLog_utils.readLog("t3_medium_1_sec_img_load/serverless_vm_cloud_max_update_150_0.8.log_request_7_t3_medium_1_sec_img_load")
MAXVM_vm_logdata = logdata = readLog_utils.readLog("t3_medium_1_sec_img_load/20200428_MAX_VM")

# price
# Hybrid
Hybridprice_SLS, Hybridprice_Hybrid, Hybridprice_SUM = Hybrid_utils.price(hybrid_req_logdata, hybrid_vm_logdata)
# SLS
SLSprice = SLS_utils.price(SLS_req_logdata)
# VM
VMprice = VM_utils.price(MAXVM_vm_logdata)
# Barplot
priceBarplot = plot_bar.plot_price([Hybridprice_SUM/Hybridprice_SUM, SLSprice/Hybridprice_SUM, VMprice/Hybridprice_SUM], ['hybrid', 'serverless', 'max_provison'], ['g', 'k', 'r'], "out_file")
priceBarplot.savefig("Price_BarPlot.pdf")
priceBarplot.show()


# CDF
fig = plt.figure()
# Hybrid
temp = []
temp.extend(hybrid_req_logdata.d_SLS_TAtime)
temp.extend(hybrid_req_logdata.d_VM_TAtime)
Hybrid_total_cdf = plot_cdf.plot_con(temp, "r")
# SLS
SLS_cdf = plot_cdf.plot_con(SLS_req_logdata.d_SLS_TAtime, "g")
# MAX VM
MAXVM_cdf = plot_cdf.plot_con(MAXVM_req_logdata.d_VM_TAtime, "b")
plt.legend(("Hybrid", "serverless", "MAXVM"))
plt.savefig('Comparing_CDF.pdf', dpi=600, bbox_inches='tight')

# progress
# hybrid
plt.rcParams.update({'font.size': 4})
fig, ax = plt.subplots(3, 2)
f1, f2, f3, f4, f5, f6 = Hybrid_utils.plot_progress(hybrid_req_logdata, hybrid_vm_logdata, ax)
plt.savefig('hybrid_progress.pdf', dpi=1200, bbox_inches='tight')
# SLS
fig, ax = plt.subplots(2, 1)
f1, f2 = SLS_utils.plot_progress(SLS_req_logdata, ax)
plt.savefig('SLS_progress.pdf', dpi=1200, bbox_inches='tight')
# MAX_VM
fig, ax = plt.subplots(3, 1)
f1, f2, f3 = VM_utils.plot_progress(MAXVM_req_logdata, MAXVM_vm_logdata, ax)
plt.savefig('VMMAX_progress.pdf', dpi=1200, bbox_inches='tight')


