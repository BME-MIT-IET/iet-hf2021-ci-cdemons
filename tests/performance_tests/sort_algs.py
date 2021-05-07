import algorithms.sort as sort
import matplotlib as mpl
from matplotlib import pyplot as plt, cm
from matplotlib.lines import Line2D as Line
from timeit import default_timer as timer
import numpy as np
from contextlib import contextmanager
import threading
import _thread
import warnings
warnings.filterwarnings("error", '.*overflow.*')

class TimeoutException(Exception):
    def __init__(self, msg=''):
        self.msg = msg

def _get_limit(limit):
    if limit == 0:
        return '0'
    superscript = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    return '10' + f'{limit}'.translate(superscript)

class SortFail(Exception):
    error_count = 0
    labels = []
    markers = ['v', 'x', 's', 'D', 'o', '^']

    def __init__(self, label, handles, color='k'):
        if label not in SortFail.labels:
            marker = SortFail.markers[len(SortFail.labels)]
            SortFail.labels.append(label)
            handles.append(Line([0], [0], marker=marker,
                           label=label, color=color))
        self.marker = SortFail.markers[SortFail.labels.index(label)]
        self.color = color

@contextmanager
def time_limit(seconds):
    timer = threading.Timer(seconds, lambda: _thread.interrupt_main())
    timer.start()
    try:
        yield
    except KeyboardInterrupt:
        raise TimeoutException()
    finally:
        # if the action ends in specified time, timer is canceled
        timer.cancel()

if __name__ == "__main__":
    mpl.rcParams['toolbar'] = 'None'

    lengths = [int(10 ** (x/2)) for x in range(16)]
    algs = [sort.quick_sort,
            sort.radix_sort,
            sort.counting_sort,
            sort.selection_sort,
            sort.bucket_sort,
            # for the brave hearted
            sort.gnome_sort,
            sort.bogo_sort
            ]
    labels = [alg.__name__ for alg in algs]
    colors = [cm.get_cmap('gist_rainbow')(i)
              for i in np.linspace(0.0, 1.0, len(labels))]
    handles = [Line([0], [0], color=color, lw=4, label=label)
               for label, color in zip(labels, colors)]
    fig, axs = plt.subplots(1, 5, sharey=True, figsize=(25, 5))
    for plot in range(5):
        limit = plot*2
        for alg, color in zip(algs, colors):
            durations = []
            error_flag = False
            measurement_count = 3
            measurements = np.empty(measurement_count)
            for idx, length in enumerate(lengths):
                arr = np.random.randint(
                    pow(10, limit), pow(10, limit+1), length)
                try:
                    for measurement in range(measurement_count):
                        starttime = timer()
                        try:
                            with time_limit(20):
                                sorted = alg(arr)
                        except RecursionError:
                            raise SortFail('Recursion limit', handles)
                        except TimeoutException:
                            raise SortFail('Time out', handles)
                        except AttributeError:
                            raise SortFail('Array Structure not supported', handles)
                        except RuntimeWarning as r:
                            raise SortFail('Overflow', handles)
                        measurements[measurement] = timer() - starttime
                except SortFail as e:
                    if len(durations) > 0:
                        axs[plot].plot(lengths[idx-1],
                                       durations[-1],
                                       marker=e.marker,
                                       color=e.color,
                                       zorder=10)
                    else:
                        axs[plot].plot(1,
                                       0,
                                       marker=e.marker,
                                       color=e.color,
                                       zorder=10)
                    break
                durations.append(measurements.mean())
            axs[plot].plot(lengths[:len(durations)], durations, color=color)
        axs[plot].set_xscale('log')
        axs[plot].set_yscale('log')
        axs[plot].grid()
        axs[plot].title.set_text(
            f'{"Value range: " if limit == 0 else ""}{_get_limit(limit)}-{_get_limit(limit+1)}')
    fig.legend(handles=handles, loc='upper left')
    fig.suptitle("Sorting Algortihms", fontsize=20)
    fig.supxlabel("Array length")
    fig.supylabel("Seconds")
    fig.savefig('tests/performance_tests/sorts.png')
    plt.show()