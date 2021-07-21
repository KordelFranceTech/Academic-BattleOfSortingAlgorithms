# graph_data.py
# Kordel France
########################################################################################################################
# This file provides functions to categorize, filter, graph, and save analyzed sorting data.
# The data is first categorized by data type and algorithm, then graphed and saved, and finally summarized.
########################################################################################################################

# used as an interface to build a graph and plot with data
import matplotlib.pyplot as plt
# used to write performance data to .csv files
import csv
from Lab4.Metric import Metric as m
from Lab4.constants import file_sizes, file_types, sort_algos

final_metrics = []

def stratify_data_sorts(metrics):
	"""
	Categorizes (stratifies) the data according to the data's initial distribution: sorted, reverse-sorted, random.
	;param metrics: An array of metrics evaluated from the sorting data that will be categorized here.
	"""
	sorted_metrics = []
	rev_sorted_metrics = []
	random_metrics = []
	for i in range(0, len(metrics)):
		met = metrics[i]
		m0 = m(met.n, met.sort, met.algo, met.comps, met.exs, met.predata, met.postdata, '', '', met.time)
		if m0.sort == 'sorted':
			sorted_metrics.append(m0)
		elif m0.sort == 'reverse_sorted':
			rev_sorted_metrics.append(m0)
		elif m0.sort == 'random':
			random_metrics.append(m0)
	stratify_data_algos(sorted_metrics, rev_sorted_metrics, random_metrics)


def stratify_data_algos(sorted_metrics, rev_sorted_metrics, random_metrics):
	"""
	Categorizes (stratifies) the data according to the data's sorting algorithm.
	After this categorization procedure, all Metric objects will be grouped primarily by sort type and secondarily
		by sorting algorithm. This helps with outputting data to the screen in a clean, logical manner.
	After categorization, the data is sent to be graphed.
	;param sorted_metrics: An array of metrics evaluated from initially sorted data that will be categorized here.
	;param rev_sorted_metrics: An array of metrics evaluated from initially reverse-sorted data that will be categorized here.
	;param random_metrics: An array of metrics evaluated from initially randomized data that will be categorized here.
	"""
	# initialize arrays for population
	m1x_data = []
	m2x_data = []
	m3x_data = []
	heap_data = []

	# traverse through sorted metrics and classify by algorithm
	for i in range(0, len(sorted_metrics)):
		met = sorted_metrics[i]
		s = m(met.n, met.sort, met.algo, met.comps, met.exs, met.predata, met.postdata, '', '', met.time)
		if s.algo == 'm1x':
			m1x_data.append(s)
		elif s.algo == 'm2x':
			m2x_data.append(s)
		elif s.algo == 'm3x':
			m3x_data.append(s)
		elif s.algo == 'heap':
			heap_data.append(s)

	# sorted metrics categorized - prepare them for graphing
	graph_exchanges('Sorted', m1x_data, m2x_data, m3x_data, heap_data)
	# re-init the data for next sorting category
	m1x_data.clear()
	m2x_data.clear()
	m3x_data.clear()
	heap_data.clear()

	# traverse through reverse-sorted metrics and classify by algorithm
	for i in range(0, len(rev_sorted_metrics)):
		met = rev_sorted_metrics[i]
		s = m(met.n, met.sort, met.algo, met.comps, met.exs, met.predata, met.postdata, '', '', met.time)
		if s.algo == 'm1x':
			m1x_data.append(s)
		elif s.algo == 'm2x':
			m2x_data.append(s)
		elif s.algo == 'm3x':
			m3x_data.append(s)
		elif s.algo == 'heap':
			heap_data.append(s)

	# reverse-sorted metrics categorized - prepare them for graphing
	graph_exchanges('Reverse Sorted', m1x_data, m2x_data, m3x_data, heap_data)
	# re-init the data for next sorting category
	m1x_data.clear()
	m2x_data.clear()
	m3x_data.clear()
	heap_data.clear()

	# traverse through randomized metrics and classify by algorithm
	for i in range(0, len(random_metrics)):
		met = random_metrics[i]
		s = m(met.n, met.sort, met.algo, met.comps, met.exs, met.predata, met.postdata, '', '', met.time)
		if s.algo == 'm1x':
			m1x_data.append(s)
		elif s.algo == 'm2x':
			m2x_data.append(s)
		elif s.algo == 'm3x':
			m3x_data.append(s)
		elif s.algo == 'heap':
			heap_data.append(s)

	# randomized metrics categorized - prepare them for graphing
	graph_exchanges('Randomized', m1x_data, m2x_data, m3x_data, heap_data)


def graph_exchanges(title, m1x_data, m2x_data, m3x_data, heap_data):
	"""
	Graphs the cleanly sorted data in accordance to each sort category - sorted, reverse-sorted, or randomized.
	All runs of similar categories and algorithms are graphed together, as long as they belong to the same sort category.
	This function is called 3 times - (1 sorted data, 2) reverse-sorted data, 3) randomized data
	;param title: a string of one of the three data categories being graphed and the title of our graph.
	;param m1x_data: an array of Metric objects representing the natural merge sort algorithm.
	;param m2x_data: an array of Metric objects representing the 2-way merge sort algorithm.
	;param m3x_data: an array of Metric objects representing the 3-way merge sort algorithm.
	;param heap_data: an array of Metric objects representing the heap sort algorithm.
	"""
	global final_metrics
	m1x_x_vals = []
	m1x_comp_vals = []
	m1x_ex_vals = []
	m2x_x_vals = []
	m2x_comp_vals = []
	m2x_ex_vals = []
	m3x_x_vals = []
	m3x_comp_vals = []
	m3x_ex_vals = []
	heap_x_vals = []
	heap_comp_vals = []
	heap_ex_vals = []

	# iterate through all natural merge sort objects to extract # comparisons and # exchanges for graphing
	for metric in m1x_data:
		met = metric
		m0 = m(met.n, met.sort, met.algo, met.comps, met.exs, met.predata, met.postdata, '', '', met.time)
		m1x_x_vals.append(m0.n)
		m1x_ex_vals.append(m0.exs)
		m1x_comp_vals.append(m0.comps)

	# iterate through all 2-way merge sort objects to extract # comparisons and # exchanges for graphing
	for metric in m2x_data:
		met = metric
		m0 = m(met.n, met.sort, met.algo, met.comps, met.exs, met.predata, met.postdata, '', '', met.time)
		m2x_x_vals.append(m0.n)
		m2x_ex_vals.append(m0.exs)
		m2x_comp_vals.append(m0.comps)

	# iterate through all 3-way merge sort objects to extract # comparisons and # exchanges for graphing
	for metric in m3x_data:
		met = metric
		m0 = m(met.n, met.sort, met.algo, met.comps, met.exs, met.predata, met.postdata, '', '', met.time)
		m3x_x_vals.append(m0.n)
		m3x_ex_vals.append(m0.exs)
		m3x_comp_vals.append(m0.comps)

	# iterate through all heap sort objects to extract # comparisons and # exchanges for graphing
	for metric in heap_data:
		met = metric
		m0 = m(met.n, met.sort, met.algo, met.comps, met.exs, met.predata, met.postdata, '', '', met.time)
		heap_x_vals.append(m0.n)
		heap_ex_vals.append(m0.exs)
		heap_comp_vals.append(m0.comps)

	# iterate through all natural merge sort objects to compute the fitted exponential regression curves for trajectory
	#		of # comparisons and # exchanges as n scales larger.
	# also write to file
	for m1 in m1x_data:
		m1.comp_eq = m1.fitPowerRegressionCurveComparisons(m1x_x_vals, m1x_comp_vals)
		m1.ex_eq = m1.fitPowerRegressionCurveExchanges(m1x_x_vals, m1x_ex_vals)
		write_data_to_file(m1)
		final_metrics.append(m1)

	# iterate through all 2-way merge sort objects to compute the fitted exponential regression curves for trajectory
	#		of # comparisons and # exchanges as n scales larger.
	# also write to file
	for m2 in m2x_data:
		m2.comp_eq = m2.fitPowerRegressionCurveComparisons(m2x_x_vals, m2x_comp_vals)
		m2.ex_eq = m2.fitPowerRegressionCurveExchanges(m2x_x_vals, m2x_ex_vals)
		write_data_to_file(m2)
		final_metrics.append(m2)

	# iterate through all 3-way merge sort objects to compute the fitted exponential regression curves for trajectory
	#		of # comparisons and # exchanges as n scales larger.
	# also write to file
	for m3 in m3x_data:
		m3.comp_eq = m3.fitPowerRegressionCurveComparisons(m3x_x_vals, m3x_comp_vals)
		m3.ex_eq = m3.fitPowerRegressionCurveExchanges(m3x_x_vals, m3x_ex_vals)
		write_data_to_file(m3)
		final_metrics.append(m3)

	# iterate through all heap sort objects to compute the fitted exponential regression curves for trajectory
	#		of # comparisons and # exchanges as n scales larger.
	# also write to file
	for h in heap_data:
		h.comp_eq = h.fitPowerRegressionCurveComparisons(heap_x_vals, heap_comp_vals)
		h.ex_eq = h.fitPowerRegressionCurveExchanges(heap_x_vals, heap_ex_vals)
		write_data_to_file(h)
		final_metrics.append(h)

	# create scatter plots of all the data
	plt.scatter(m1x_x_vals, m1x_ex_vals)
	plt.scatter(m2x_x_vals, m2x_ex_vals)
	plt.scatter(m3x_x_vals, m3x_ex_vals)
	plt.scatter(heap_x_vals, heap_ex_vals)
	plt.scatter(m1x_x_vals, m1x_comp_vals)
	plt.scatter(m2x_x_vals, m2x_comp_vals)
	plt.scatter(m3x_x_vals, m3x_comp_vals)
	plt.scatter(heap_x_vals, heap_comp_vals)

	# overlay line graphs of # comparisons per algorithm
	plt.plot(m1x_x_vals, m1x_comp_vals, label='(comparisons)  natural merge sort', color='orange')
	plt.plot(m2x_x_vals, m2x_comp_vals, label='(comparisons)  2-way merge sort', color='green')
	plt.plot(m3x_x_vals, m3x_comp_vals, label='(comparisons)  3-way merge sort', color='blue')
	plt.plot(heap_x_vals, heap_comp_vals, label='(comparisons)  heap sort', color='red')

	# overlay dashed line graphs of # exchanges per algorithm
	plt.plot(m1x_x_vals, m1x_ex_vals, label='(exchanges)     natural merge sort', linestyle='--', color='orange')
	plt.plot(m2x_x_vals, m2x_ex_vals, label='(exchanges)     2-way merge sort', linestyle='--', color='green')
	plt.plot(m3x_x_vals, m3x_ex_vals, label='(exchanges)     3-way merge sort', linestyle='--', color='blue')
	plt.plot(heap_x_vals, heap_ex_vals, label='(exchanges)     heap sort', linestyle='--', color='red')

	# format the graph and show it to the user
	plt.title(f'Algorithm Performance Over {title} Data')
	plt.xlabel('number of files (n)')
	plt.ylabel('number of exchanges')
	plt.xlim(0, max(file_sizes) * 1.05)
	plt.ylim(0, max(heap_comp_vals) * 1.05)
	plt.legend()
	plt.show(block=False)
	print('\n\n\n\n\n')
	print('_________________________________________________________________________________________')
	print('_________________________________________________________________________________________')
	print(f'Now displaying algorithmic performance over {title} data.')
	print('\nType any key to dismiss current plot and view next plot...')
	# the user simply taps a key in order to dismiss the plot and move to the next one
	if input() != None:
		# reset plot for redraw on new data
		plt.clf()
		plt.cla()
	print('_________________________________________________________________________________________')
	print('_________________________________________________________________________________________')


def write_data_to_file(data):
	"""
	This function writes data to a .csv file for interpretation by user after program termination.
	Each possible scenario gets its own .csv file.
	Files are named {algorithm_name}-{date_type}-{n} count.csv such as '3-way_merge_random_1000count.csv'.
	All files are output to the 'output_Files' folder.
	The 'csv' library is used to write the data to each respective report.
	;param data: an array of Metric objects used to build .csv file
	"""
	metric = m(data.n, data.sort, data.algo, data.comps, data.exs, data.predata, data.postdata, data.comp_eq, data.ex_eq, data.time)
	if metric.algo == 'm1x':
		metric.algo = 'natural_merge'
	elif metric.algo == 'm2x':
		metric.algo = '2-way_merge'
	elif metric.algo == 'm3x':
		metric.algo = '3-way_merge'
	elif metric.algo == 'm4x':
		metric.algo = '4-way_merge'
	else:
		metric.algo = 'heap_sort'

	with open(f'output_files/{metric.algo}-{metric.sort}-{metric.n}count.csv', 'w', newline='') as csv_file:
			title_names = ['title']
			comp_names = ['comparisons', 'equation', 'time']
			ex_names = ['exchanges', 'equation']
			col_names = ['count', 'presorted values', 'postsorted values']
			title_writer = csv.DictWriter(csv_file, fieldnames=title_names)
			title_writer.writerow({'title': f'Analysis data for {metric.algo} algorithm on {metric.sort} data for n = {metric.n}'})
			comp_writer = csv.DictWriter(csv_file, fieldnames=comp_names)
			comp_writer.writerow({'comparisons': f'# of comparisons: {str(metric.comps)}',
								  'equation': f' regression equation: {str(metric.comp_eq)}',
								  'time': f'execution time: {str(metric.time)} s'})
			ex_writer = csv.DictWriter(csv_file, fieldnames=ex_names)
			ex_writer.writerow({'exchanges': f'# of exchanges: {str(metric.exs)}',
								'equation': f' regression equation: {str(metric.ex_eq)}'})
			csv_writer = csv.DictWriter(csv_file, fieldnames=col_names)
			csv_writer.writeheader()
			count = 0
			for i in range(0, min(len(metric.predata), len(metric.postdata))):
				csv_writer.writerow({'count': str(count),
									 'presorted values': data.predata[i],
									 'postsorted values': data.postdata[i]})
				count += 1


def present_and_save_summary():
	"""
	This function presents a final summary of performance statistics for each sorting run analyzed.
	A summary table is printed to the console and a copy of that summary table is written to a .csv file.
	The summary .csv file is named FINAL_ANALYSIS.csv and may be found in the 'output_files' folder of this module.
	"""
	global final_metrics
	metrics = final_metrics

	with open(f'output_files/FINAL_ANALYSIS.csv', 'w', newline='') as csv_file:
			title_names = ['title']
			col_names = ['#',
						  'data_type',
						  'n',
						  'algorithm',
						  'comparisons',
						  'exchanges',
						  'comparison trajectory equation',
						  'exchange trajectory equation',
						  'time']
			title_writer = csv.DictWriter(csv_file, fieldnames=title_names)
			title_writer.writerow({'title': f'Summary of all {len(file_types) * len(file_sizes) * len(sort_algos)} analyzed sorting runs'})
			csv_writer = csv.DictWriter(csv_file, fieldnames=col_names)
			csv_writer.writeheader()

			print('#\t|data type\t|n\t|algorithm\t|comparisons\t|exchanges\t|time\t\t|comparison trajectory eqn\t\t\t\t\t|exchange trajectory eqn')
			print('____________________________________________________________________________________________'
				  '____________________________________________________________________________________________')

			count = 0
			for i in range(0, len(metrics)):
				count += 1
				metric = metrics[i]
				if metric.algo == 'm1x':
					metric.algo = 'natural_merge'
				elif metric.algo == 'm2x':
					metric.algo = '2-way_merge'
				elif metric.algo == 'm3x':
					metric.algo = '3-way_merge'
				elif metric.algo == 'm4x':
					metric.algo = '4-way_merge'
				else:
					metric.algo = 'heap_sort'
				if metric.sort == 'reverse_sorted':
					metric.sort = 'reverse'
				else:
					metric.sort = f'{metric.sort}\t'

				print(f'{count}\t|{metric.sort}\t|{metric.n}\t|{metric.algo}\t|\t{metric.comps}\t|\t{metric.exs}\t|{metric.time} s\t|  {metric.comp_eq}  |  {metric.ex_eq}')
				csv_writer.writerow({'#':f'{count}',
									 'data_type':f'{metric.sort}',
									 'n':f'{metric.n}',
									 'algorithm':f'{metric.algo}',
									 'comparisons':f'{metric.comps}',
									 'exchanges':f'{metric.exs}',
									 'comparison trajectory equation':f'{metric.comp_eq}',
									 'exchange trajectory equation':f'{metric.ex_eq}',
									 'time':f'execution time: {metric.time} s'})









