def cocktailSort(random_list):
    n = len(random_list)
    swapped = True
    start = 0
    end = n - 1
    while (swapped == True):

        swapped = False

        for i in range(start, end):
            if (random_list[i] > random_list[i + 1]):
                random_list[i], random_list[i + 1] = random_list[i + 1], random_list[i]
                swapped = True

        if (swapped == False):
            break

        swapped = False

        end = end - 1

        for i in range(end - 1, start - 1, -1):
            if (random_list[i] > random_list[i + 1]):
                random_list[i], random_list[i + 1] = random_list[i + 1],random_list[i]
                swapped = True

        start = start + 1

def cocktailSortPrint(random_list):
    for i in range(len(random_list)):
        print(random_list[i], end=' ')