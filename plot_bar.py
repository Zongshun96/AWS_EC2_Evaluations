import numpy as np
import matplotlib.pyplot as plt

def plot_price(data, labels, colors, out_file):
	index = np.arange(len(data))
	bar_width = 0.35
	opacity = 0.8
	fig = plt.figure()
	for i in range(0, len(data)): 
		rects1 = plt.bar(i+(bar_width/20), data[i], bar_width,
		alpha=opacity, label=labels[i], color=colors[i])
	plt.ylabel('normalized cost')
	plt.xticks(index+0.2, labels)
	plt.ticklabel_format(axis='y', scilimits=(0,0))
	plt.tight_layout()
	plt.plot()
	# fig.savefig(out_file, dpi=600, bbox_inches='tight')
	#plt.show()
	return fig

def plot_a(length, labels, a, hatch=""):
	x = np.arange(length)
	fig = plt.figure()
	ax1 = plt.subplot(1,1,1)
	w = 0.3
	plt.xticks(x, labels)
	plt.ylabel('cost')
	plt.ylim(0, max(a) + 1)
	cost_bar =ax1.bar(x, a, width=w, facecolor="none", edgecolor="b", align='center', hatch=hatch)
	#The trick is to use two different axes that share the same x axis, we have used ax1.twinx() method.
	# ax2 = ax1.twinx()
	# sla_vio_bar =ax2.bar(x + w, sla_violations, width=w,color='r',align='center')
	plt.ylabel('Normalized Time', fontsize=20)
	# plt.legend([cost_bar, sla_vio_bar],['Normalized Cost', 'SLA Violations'])
	plt.axis([-0.3, 2.3, 0, 2.5])
	plt.grid()
	plt.tight_layout()
	#plt.savefig('uptime.pdf')
	# plt.show()
	return fig

def plot_price_and_SLA_violation(length, labels, cost, sla_violations, left, right, left_label, right_label, left_hatch, right_hatch, left_color, right_color):
	x = np.arange(length)
	fig = plt.figure(figsize=(7,4.7))
	ax1 = plt.subplot(1, 1, 1)
	w = 0.3
	plt.xlabel(" ", fontsize=20)
	plt.xticks(x + w / 2, labels, fontsize=15)
	plt.ylabel(left_label, fontsize=20)
	plt.ylim(0, max(cost)+0.7)
	cost_bar = ax1.bar(x, cost, width=w, facecolor="none", edgecolor=left_color, align='center', hatch=left_hatch)
	ax1.tick_params(axis='both', which='major', labelsize=15)
	# The trick is to use two different axes that share the same x axis, we have used ax1.twinx() method.
	ax2 = ax1.twinx()
	sla_vio_bar = ax2.bar(x + w, sla_violations, width=w, facecolor="none", edgecolor=right_color, align='center', hatch=right_hatch)
	plt.ylabel(right_label, fontsize=20)
	plt.ylim(0, max(sla_violations)+10)
	plt.legend([cost_bar, sla_vio_bar], [left, right], prop={'size': 20}, loc="upper left", bbox_to_anchor=(0,1.03))
	# plt.legend([cost_bar, sla_vio_bar], ['Normalized Cost', 'SLA Violations'])
	ax2.tick_params(axis='both', which='major', labelsize=15)

	plt.grid()
	plt.tight_layout()
	return fig

# def plot_price_and_SLA_violation(length, labels, cost, sla_violations, left, right, left_label, right_label, left_hatch, right_hatch, left_color, right_color):
# 	x = np.arange(length)
# 	fig = plt.figure(figsize=(7,4.7))
# 	ax1 = plt.subplot(1, 1, 1)
# 	w = 0.3
# 	plt.xlabel(" ", fontsize=20)
# 	plt.xticks(x + w / 2, labels, fontsize=15)
# 	plt.ylabel(left_label, fontsize=20)
# 	plt.ylim(0, 3)
# 	cost_bar = ax1.bar(x, cost, width=w, facecolor="none", edgecolor=left_color, align='center', hatch=left_hatch)
# 	ax1.tick_params(axis='both', which='major', labelsize=15)
# 	# The trick is to use two different axes that share the same x axis, we have used ax1.twinx() method.
# 	ax2 = ax1.twinx()
# 	sla_vio_bar = ax2.bar(x + w, sla_violations, width=w, facecolor="none", edgecolor=right_color, align='center', hatch=right_hatch)
# 	plt.ylabel(right_label, fontsize=20)
# 	plt.ylim(0, max(sla_violations)+10)
# 	# plt.ylim(0, 10)
# 	plt.legend([cost_bar, sla_vio_bar], [left, right], prop={'size': 16}, loc="upper left", facecolor="none", edgecolor="none")
# 	# legend.get_frame().set_alpha(None)
# 	# legend.get_frame().set_facecolor((0, 0, 1, 0.1))
# 	# plt.legend([cost_bar, sla_vio_bar], ['Normalized Cost', 'SLA Violations'])
# 	ax2.tick_params(axis='both', which='major', labelsize=15)

# 	plt.grid()
# 	plt.tight_layout()
# 	return fig

def plot_a_and_b_violation_side(length, labels, a, b, left, right, y_label, left_hatch, right_hatch, left_color, right_color):
	x = np.arange(length)
	fig = plt.figure()
	ax1 = plt.subplot(1, 1, 1)
	w = 0.3
	plt.xticks(x + w / 2, labels)
	cost_bar = ax1.bar(x, a, width=w, facecolor="none", edgecolor=left_color, align='center', hatch=left_hatch)
	sla_vio_bar = ax1.bar(x + w, b, width=w, facecolor="none", edgecolor=right_color, align='center',hatch=right_hatch)
	ax1.tick_params(axis='both', which='major', labelsize=15)
	plt.ylabel(y_label, fontsize=20)
	plt.ylim(0, max(b+a) + 0.01)
	plt.legend([cost_bar, sla_vio_bar], [left, right], prop={'size': 20})
	plt.grid()
	plt.tight_layout()
	return fig

def plot_a_stack(length, labels, a, legend, y_label, hatch, face_color, edge_color, ax1, bottom_dataset):
	x = np.arange(length)
	# fig = plt.figure()
	# ax1 = plt.subplot(1, 1, 1)
	w = 0.3
	plt.xticks(x, labels)
	a_bar = ax1.bar(x, a, width=w, facecolor=face_color, edgecolor=edge_color, align='center', hatch=hatch, label=legend, bottom=bottom_dataset)
	ax1.tick_params(axis='both', which='major', labelsize=15)
	plt.ylabel(y_label, fontsize=20)

	# plt.legend([a_bar], [left, right], prop={'size': 20})
	# plt.grid()
	plt.tight_layout()
	# return fig


def plot_a_and_b_stack(length, labels, a, b, left, right, left_hatch='', right_hatch=''):
	x = np.arange(length)
	fig = plt.figure()
	ax1 = plt.subplot(1, 1, 1)
	w = 0.3
	plt.xticks(x, labels, rotation=60)
	plt.ylabel('cost ($)')
	a_bar = ax1.bar(x, a, width=w, color='r', align='center', hatch=left_hatch)
	b_bar = ax1.bar(x, b, width=w, color='b', align='center', hatch=right_hatch)
	# plt.ylim(min(b)-0.01, max(a) + 0.01)
	plt.legend([a_bar, b_bar], [left, right])
	# plt.legend([cost_bar, sla_vio_bar], ['Normalized Cost', 'SLA Violations'])
	plt.grid()
	plt.tight_layout()
	return fig


# w = 0.3
# plt.xticks(x, labels, rotation=60)
# plt.ylabel('cost')
# cost_bar =ax1.bar(x, ser_cost, width=w, color='r', align='center', label='Serverless cost')
# cost_bar =ax1.bar(x, vm_cost, width=w, color='b', align='center', label='VM cost')
# plot_price([1, 2, 3], ['hybrid', 'serverless', 'max_provison'], ['g', 'k', 'r'], 'figs/cost.pdf')
