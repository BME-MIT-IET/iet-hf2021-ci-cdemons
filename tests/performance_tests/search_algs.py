import algorithms.search as search
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

class SearchFail(Exception):
    error_count = 0
    labels = []
    markers = ['v', 'x', 's', 'D', 'o', '^']

    def __init__(self, label, handles, color='k'):
        if label not in SearchFail.labels:
            marker = SearchFail.markers[len(SearchFail.labels)]
            SearchFail.labels.append(label)
            handles.append(Line([0], [0], marker=marker,
                           label=label, color=color))
        self.marker = SearchFail.markers[SearchFail.labels.index(label)]
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

    lengths = [int(10 ** (x+1/2)) for x in range(9)]
    algs = [search.binary_search,
            search.first_occurrence,
            search.interpolation_search,
            search.jump_search,
            search.last_occurrence,
            search.linear_search,
            search.search_insert,
            search.search_rotate
            ]
    labels = [alg.__name__ for alg in algs]
    colors = [cm.get_cmap('gist_rainbow')(i)
              for i in np.linspace(0.0, 1.0, len(labels))]
    handles = [Line([0], [0], color=color, lw=4, label=label)
               for label, color in zip(labels, colors)]
    fig, axs = plt.subplots(1, 5, sharey=True, figsize=(25, 5))
    for plot in range(5):
        step = (plot+1) ** 5
        for alg, color in zip(algs, colors):
            rand_gen = np.random.default_rng(0)
            durations = []
            error_flag = False
            measurement_count = 3
            measurements = np.empty(measurement_count)
            for idx, length in enumerate(lengths):
                arr = np.arange(0, step*length, step)
                try:
                    for measurement in range(measurement_count):
                        index = rand_gen.choice(length)
                        val = arr[index]
                        starttime = timer()
                        try:
                            with time_limit(3):
                                sorted = alg(arr, val)
                        except TimeoutException:
                            raise SearchFail('Time out', handles)
                        except RuntimeWarning as r:
                            raise SearchFail('Overflow', handles)
                        measurements[measurement] = timer() - starttime
                except SearchFail as e:
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
            f'Value distance: {step}')
    fig.legend(handles=handles, loc='lower left')
    fig.suptitle("Search Algortihms", fontsize=20)
    fig.supxlabel("Array length")
    fig.supylabel("Seconds")
    fig.tight_layout()
    fig.savefig('tests/performance_tests/searches.png')
    plt.show()