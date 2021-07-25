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





# ========================================================================================================================
# ========================================================================================================================
# price and SLA bar
s = 25.155386165004835+0.27+0.4512
cost = [s/s, 54.898033244999645/s, (60.0+0.27)/s, (29.512843283896807+0.27)/s, (29.273888888896806+0.27)/s]
sla_violations = [0.0*100, 0.0*100, 0.00*100, 0.019423151694771015*100, 0.031150601194911715*100]

labels = ['LIBRA', 'FaaS', 'MAX', 'SPOCK', 'AUTO']
priceBarplot = plot_bar.plot_price_and_SLA_violation(5, labels, cost, sla_violations, 'Normalized Cost', 'SLA Violations', 'Normalized Cost', '%', "++", "//", "b", "r")
priceBarplot.savefig(figfolder+"/sla_cost_IC2E.eps", format='eps')

# ========================================================================================================================
# ========================================================================================================================
# duration bar for VM
uptime = [547200/547200, 1053860/547200, 1053860/547200]
labels = ['LIBRA', 'AUTO', 'SPOCK']
durationBarplot = plot_bar.plot_a(3, labels, uptime, "//")
durationBarplot.savefig(figfolder+"/vm_uptime_IC2E.eps", format='eps')

# ========================================================================================================================
# ========================================================================================================================
lib_ser_cost, lib_vm_cost = 9.955386165000183, 15.200000000004653
s = lib_ser_cost + lib_vm_cost + 0.27 + 0.4512
auto_ser_cost, auto_vm_cost = 0, 29.273888888896806
spock_ser_cost, spock_vm_cost = 0.23895439499999985, 29.273888888896806

# price bars for individual VM and SER
priceBarplot = plt.figure()
ax1 = plt.subplot(1, 1, 1)
ax1.set_ylim(0, 0.3 + max([s/s, (auto_vm_cost+ 0.5*(0.0225+0.008))/s, (spock_ser_cost+spock_vm_cost+ 0.5*(0.0225+0.008))/s]) + 0.2)
labels = ['LIBRA', 'AUTO', 'SPOCK']
libra_costs = [0.4512/s, 0, 0]
ser_costs = [(lib_ser_cost)/s, 0, (spock_ser_cost)/s]
alb_costs = [(0.27)/s, (0.27)/s, (0.27)/s]
vm_costs = [(lib_vm_cost)/s, (auto_vm_cost)/s, (spock_vm_cost)/s]

empty_costs = [0,0,0]

plot_bar.plot_a_stack(3, labels, ser_costs, "FaaS Cost", "Normalized Cost", "++", "none", "g", ax1, [sum(x) for x in zip(libra_costs, alb_costs, vm_costs)])
plot_bar.plot_a_stack(3, labels, libra_costs, "LG Cost", "Normalized Cost", "", "black", "black", ax1, [sum(x) for x in zip(alb_costs, vm_costs)])
plot_bar.plot_a_stack(3, labels, [sum(x) for x in zip(alb_costs, vm_costs)], "IaaS Cost", "Normalized Cost", "//", "none", "b", ax1, empty_costs)

ax1.legend(prop={'size': 20}, loc="upper center", ncol = 2)
ax1.grid(True)
# plt.tight_layout()
priceBarplot.savefig(figfolder+"/cost_break_down_norm_IC2E.eps", format='eps')