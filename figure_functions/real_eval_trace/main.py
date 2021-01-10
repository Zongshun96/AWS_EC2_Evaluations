# ========================================================================================================================
# plot trace
import os

import matplotlib.pyplot as plt
import Hybrid_utils,readLog_utils

hybrid_req_logdata = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/28_20200515_hybrid_4_req_per_vm_pos_std_1800_total_")
hybrid_vm_logdata  = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/28_20200515_hybrid_4_req_per_vm_pos_std_1800_total")

fig, ax = plt.subplots(1, 1)
Hybrid_utils.Num_Req_to_Either(hybrid_req_logdata, ax)
os.makedirs("fig", exist_ok=True)
plt.savefig('fig/real_eval_trace.pdf', dpi=1200, bbox_inches='tight')
# ========================================================================================================================