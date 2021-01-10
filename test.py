import numpy as np
import matplotlib.pyplot as plt

cost = [25.155386165004835/25.155386165004835, 54.898033244999645/25.155386165004835, 60.0/25.155386165004835, 29.512843283896807/25.155386165004835, 29.273888888896806/25.155386165004835]
sla_violations = [0.0*100, 0.0*100, 0.004526044109651783*100, 0.019423151694771015*100, 0.031150601194911715*100]
labels = ['LIBRA', 'SER', 'MAX', 'SPOCK', 'AUTO']




x = np.arange(5)
ax1 = plt.subplot(1,1,1)
w = 0.3
plt.xticks(x + w /2, labels, rotation='vertical')
plt.ylabel('cost')
cost_bar =ax1.bar(x, cost, width=w, color='b', align='center')
#The trick is to use two different axes that share the same x axis, we have used ax1.twinx() method.
ax2 = ax1.twinx()
sla_vio_bar =ax2.bar(x + w, sla_violations, width=w,color='r',align='center')
plt.ylabel('%')
plt.legend([cost_bar, sla_vio_bar],['Normalized Cost', 'SLA Violations'])
plt.grid()
plt.tight_layout()
plt.savefig('sla_cost.pdf')
plt.show()