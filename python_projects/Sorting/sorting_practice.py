import pandas as pd

from time import perf_counter
import numpy as np


from python_projects.Sorting.gnomeSort import *
from python_projects.Sorting.mergeSort import *
from python_projects.Sorting.quickSort import *
from python_projects.Sorting.radixSort import *
from python_projects.Sorting.coctailSort import *

NUMBER_OF_ELEMENTS = [10, 100, 1000, 10000, 100000]


def randomList(len_of_list):
    random_list = np.arange(len_of_list)
    np.random.shuffle(random_list)
    return random_list


def tableOutput(sort_names, time_spend, list_len):

    df = pd.DataFrame()
    df['algo_name'] = sort_names
    df['time of sorting'] = time_spend
    df['len of list'] = list_len

    print(df)



def main():
    time_spend = []
    sort_names = ['quicksort', 'mergesort', 'radixsort', 'gnomesort', 'coctailsort']*len(NUMBER_OF_ELEMENTS)

    for number_of_element in NUMBER_OF_ELEMENTS:
        random_list = randomList(number_of_element)

        start_time = perf_counter()
        quickSort(random_list)
        end_time_1 = perf_counter()
        time_spend.append(end_time_1 - start_time)

        mergeSort(random_list)
        end_time_2 = perf_counter()
        time_spend.append(end_time_2 - end_time_1)

        radixSort(random_list)
        end_time_3 = perf_counter()
        time_spend.append(end_time_3 - end_time_2)

        gnomeSort(random_list, len(random_list))
        end_time_4 = perf_counter()
        time_spend.append(end_time_4- end_time_3)

        cocktailSort(random_list)
        end_time_5 = perf_counter()
        time_spend.append(end_time_5 - end_time_4)
    names = [el for el in NUMBER_OF_ELEMENTS for _ in range(len(NUMBER_OF_ELEMENTS))]
    tableOutput(sort_names, time_spend, names)


if __name__ == "__main__":
    main()