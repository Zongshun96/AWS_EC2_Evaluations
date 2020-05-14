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




# plot_price([1, 2, 3], ['hybrid', 'serverless', 'max_provison'], ['g', 'k', 'r'], 'figs/cost.pdf')
