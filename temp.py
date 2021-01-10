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

# SLS_req_logdata    = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/26_serverless_serverless_update_150_0.8.log_request_1_sec_img_load_1800_total_")
hybrid_req_logdata = readLog_utils.readLog("data/t3_medium_1_sec_img_load_4_req_per_VM/28_20200515_hybrid_4_req_per_vm_pos_std_1800_total_")
