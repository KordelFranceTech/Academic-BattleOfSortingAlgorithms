#__main__.py
# Kordel France
########################################################################################################################
# This file contains the driver code for the sorting complexity analysis program.
# All other files may be viewed as helpers that are pooled together here for use.
########################################################################################################################

from Lab4.heap_sort import heap_sort, reset_counts_heap_sort
from Lab4.merge_sort_natural import merge_sort_natural, reset_counts_merge_sort_natural
from Lab4.merge_sort_2way import merge_sort_two_way, reset_counts_merge_sort_two_way
from Lab4.merge_sort_3way import merge_sort_three_way, reset_counts_merge_sort_three_way
from Lab4.constants import file_sizes, file_types, sort_algos
from Lab4.file_manager import generate_sorted_file, generate_reverse_sorted_file, generate_random_sorted_file
from Lab4 import graph_data as graph
from Lab4.Metric import Metric as m
import time


data_metrics = []
status = len(file_sizes) * len(file_types)
status_count = 0
# print a header for UI aesthetics
print('_________________________________________________________________________________________')
print('_________________________________________________________________________________________')
print('_________________________________________________________________________________________')
print('\t\t\t\t\tWelcome')
print('*****************************************************************************************')
print('*****************************************************************************************')


# briefly pause processing so the user can read the feedback given to them in the command prompt
time.sleep(2.0)
print('*****************************************************************************************')
print('\t\t\tStarting Complexity Analysis Program\n')
print('_________________________________________________________________________________________')
time.sleep(2.0)

# inform the user of what will be accomplished by and presented in this program
print(f'A total of {len(file_types) * len(file_sizes) * len(sort_algos)} different analyses will be performed on '
      f'different sorting scenarios.')
print(f'\t{len(sort_algos)} different sorts will be compared: {[algo for algo in sort_algos]}.')
print(f'\t{len(file_sizes)} different file sizes will be compared for each sort: {[size for size in file_sizes]}.')
print(f'\t{len(file_types)} different data distributions will be evaluated for each sort at each quantity: '
      f'{[type for type in file_types]}.')

# briefly pause processing so the user can read the feedback given to them in the command prompt
time.sleep(7.0)
print(f'\n\nBeginning sorting procedures now.')
time.sleep(2.0)
print('_________________________________________________________________________________________')

# begin automatically generating and distributing the data to its respective algorithm
for size in file_sizes:                                                             # iterate through file sizes (n)
    for file_type in file_types:                                                    # iterate through file types
        if file_type == 'sorted':                                                   # check for sorted file type
            predata = generate_sorted_file(size)

            algo = 'm1x'                                                            # perform natural merge sort
            predata_m1x = [int] * len(predata)
            for i in range(0, len(predata)):
                predata_m1x[i] = predata[i]
            postdata_m1x, comps, exs, dt = merge_sort_natural(predata_m1x)
            metric_m1x = m(n=int(size),                                             # a Metric object is created for every run
                              sort=str(file_type),
                              algo=str(algo),
                              comps=comps,
                              exs=exs,
                              predata=predata,
                              postdata=postdata_m1x,
                              comp_eq='',
                              ex_eq='',
                              time=str(dt))
            data_metrics.append(metric_m1x)
            reset_counts_merge_sort_natural()

            algo = 'm2x'                                                            # perform 2-way merge sort
            predata_m2x = [int] * len(predata)
            for i in range(0, len(predata)):
                predata_m2x[i] = predata[i]
            postdata_m2x, comps, exs, dt = merge_sort_two_way(predata_m2x)
            metric_m2x = m(n=int(size),
                              sort=str(file_type),
                              algo=str(algo),
                              comps=comps,
                              exs=exs,
                              predata=predata,
                              postdata=postdata_m2x,
                              comp_eq='',
                              ex_eq='',
                              time=str(dt))
            data_metrics.append(metric_m2x)
            reset_counts_merge_sort_two_way()

            algo = 'm3x'                                                            # perform 3-way merge sort
            predata_m3x = [int] * len(predata)
            for i in range(0, len(predata)):
                predata_m3x[i] = predata[i]
            postdata_m3x, comps, exs, dt = merge_sort_three_way(predata_m3x)
            metric_m3x = m(n=int(size),
                              sort=str(file_type),
                              algo=str(algo),
                              comps=comps,
                              exs=exs,
                              predata=predata,
                              postdata=postdata_m3x,
                              comp_eq='',
                              ex_eq='',
                              time=str(dt))
            data_metrics.append(metric_m3x)
            reset_counts_merge_sort_three_way()

            algo = 'heap'                                                           # perform heap sort
            predata_h = [int] * len(predata)
            for i in range(0, len(predata)):
                predata_h[i] = predata[i]
            postdata_h, comps, exs, dt = heap_sort(predata_h)
            metric_heap = m(n=int(size),
                              sort=str(file_type),
                              algo=str(algo),
                              comps=comps,
                              exs=exs,
                              predata=predata,
                              postdata=postdata_h,
                              comp_eq='',
                              ex_eq='',
                              time=str(dt))
            data_metrics.append(metric_heap)
            reset_counts_heap_sort()

        elif file_type == 'reverse_sorted':                                         # check for reverse-sorted file type
            predata = generate_reverse_sorted_file(size)

            algo = 'm1x'                                                            # perform natural merge sort
            predata_m1x = [int] * len(predata)
            for i in range(0, len(predata)):
                predata_m1x[i] = predata[i]
            postdata_m1x, comps, exs, dt = merge_sort_natural(predata_m1x)
            metric_m1x = m(n=int(size),
                              sort=str(file_type),
                              algo=str(algo),
                              comps=comps,
                              exs=exs,
                              predata=predata,
                              postdata=postdata_m1x,
                              comp_eq='',
                              ex_eq='',
                              time=str(dt))
            data_metrics.append(metric_m1x)
            reset_counts_merge_sort_natural()

            algo = 'm2x'                                                                # perform 2-way merge sort
            predata_m2x = [int] * len(predata)
            for i in range(0, len(predata)):
                predata_m2x[i] = predata[i]
            postdata_m2x, comps, exs, dt = merge_sort_two_way(predata_m2x)
            metric_m2x = m(n=int(size),
                              sort=str(file_type),
                              algo=str(algo),
                              comps=comps,
                              exs=exs,
                              predata=predata,
                              postdata=postdata_m2x,
                              comp_eq='',
                              ex_eq='',
                              time=str(dt))
            data_metrics.append(metric_m2x)
            reset_counts_merge_sort_two_way()

            algo = 'm3x'                                                                # perform 3-way merge sort
            predata_m3x = [int] * len(predata)
            for i in range(0, len(predata)):
                predata_m3x[i] = predata[i]
            postdata_m3x, comps, exs, dt = merge_sort_three_way(predata_m3x)
            metric_m3x = m(n=int(size),
                              sort=str(file_type),
                              algo=str(algo),
                              comps=comps,
                              exs=exs,
                              predata=predata,
                              postdata=postdata_m3x,
                              comp_eq='',
                              ex_eq='',
                              time=str(dt))
            data_metrics.append(metric_m3x)
            reset_counts_merge_sort_three_way()

            algo = 'heap'                                                            # perform heap sort
            predata_h = [int] * len(predata)
            for i in range(0, len(predata)):
                predata_h[i] = predata[i]
            postdata_h, comps, exs, dt = heap_sort(predata_h)
            metric_heap = m(n=int(size),
                              sort=str(file_type),
                              algo=str(algo),
                              comps=comps,
                              exs=exs,
                              predata=predata,
                              postdata=postdata_h,
                              comp_eq='',
                              ex_eq='',
                              time=str(dt))
            data_metrics.append(metric_heap)
            reset_counts_heap_sort()

        elif file_type == 'random':                                                 # check for random sorted file type
            predata = generate_random_sorted_file(size)

            algo = 'm1x'                                                            # perform natural merge sort
            predata_m1x = [int] * len(predata)
            for i in range(0, len(predata)):
                predata_m1x[i] = predata[i]
            postdata_m1x, comps, exs, dt = merge_sort_natural(predata_m1x)
            metric_m1x = m(n=int(size),
                              sort=str(file_type),
                              algo=str(algo),
                              comps=comps,
                              exs=exs,
                              predata=predata,
                              postdata=postdata_m1x,
                              comp_eq='',
                              ex_eq='',
                              time=str(dt))
            data_metrics.append(metric_m1x)
            reset_counts_merge_sort_natural()

            algo = 'm2x'                                                             # perform 2-way merge sort
            predata_m2x = [int] * len(predata)
            for i in range(0, len(predata)):
                predata_m2x[i] = predata[i]
            postdata_m2x, comps, exs, dt = merge_sort_two_way(predata_m2x)
            metric_m2x = m(n=int(size),
                              sort=str(file_type),
                              algo=str(algo),
                              comps=comps,
                              exs=exs,
                              predata=predata,
                              postdata=postdata_m2x,
                              comp_eq='',
                              ex_eq='',
                              time=str(dt))
            data_metrics.append(metric_m2x)
            reset_counts_merge_sort_two_way()

            algo = 'm3x'                                                             # perform 3-way merge sort
            predata_m3x = [int] * len(predata)
            for i in range(0, len(predata)):
                predata_m3x[i] = predata[i]
            postdata_m3x, comps, exs, dt = merge_sort_three_way(predata_m3x)
            metric_m3x = m(n=int(size),
                              sort=str(file_type),
                              algo=str(algo),
                              comps=comps,
                              exs=exs,
                              predata=predata,
                              postdata=postdata_m3x,
                              comp_eq='',
                              ex_eq='',
                              time=str(dt))
            data_metrics.append(metric_m3x)
            reset_counts_merge_sort_three_way()

            algo = 'heap'                                                             # perform heap sort
            predata_h = [int] * len(predata)
            for i in range(0, len(predata)):
                predata_h[i] = predata[i]
            postdata_h, comps, exs, dt = heap_sort(predata_h)
            metric_heap = m(n=int(size),
                              sort=str(file_type),
                              algo=str(algo),
                              comps=comps,
                              exs=exs,
                              predata=predata,
                              postdata=postdata_h,
                              comp_eq='',
                              ex_eq='',
                              time=str(dt))
            data_metrics.append(metric_heap)
            reset_counts_heap_sort()
        status_count += 1                                                             # print status as % completion
        print(f'{str(round(100.00 * float(status_count / status), 2))} % complete.\t\t\t'
              f'Finished analysis of {file_type} data for size {size}.')
        time.sleep(0.1)                                                               # briefly pause for visual effect
print('_________________________________________________________________________________________')

# all sorting runs are complete
# now present the results and performance metrics to the user
# inform them of what is to come
print(f'\n\nPresenting results of analysis now.\nA final summary will follow a series of performance graphs.')
time.sleep(5.0)

# process data for graphing, saving, and printing
graph.stratify_data_sorts(data_metrics)
print('*****************************************************************************************')
print('*****************************************************************************************')

# graphing complete, now build and write the performance summary
print(f'\nSummary of all {len(file_types) * len(file_sizes) * len(sort_algos)} analyzed sorting runs:')
print('_________________________________________________________________________________________')
graph.present_and_save_summary()

# inform user to check 'output_files' folder for a thorough archive of the analysis
print(f'\nA copy of the graph above along with individual .csv files for each of the '
      f'{len(file_types) * len(file_sizes) * len(sort_algos)} sorting runs may be found in the `output_files` folder.')
print('____________________________________________________________________________________________'
      '____________________________________________________________________________________________\n\n')




