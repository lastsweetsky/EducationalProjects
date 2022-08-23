def countingSort(random_list, exp1):
    n = len(random_list)

    output = [0] * (n)
    count = [0] * (10)

    for i in range(0, n):
        index = random_list[i] // exp1
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = random_list[i] // exp1
        output[count[index % 10] - 1] = random_list[i]
        count[index % 10] -= 1
        i -= 1


    i = 0
    for i in range(0, len(random_list)):
        random_list[i] = output[i]


def radixSort(random_list):
    max1 = max(random_list)

    exp = 1
    while max1 / exp >= 1:
        countingSort(random_list, exp)
        exp *= 10


def radixSortPrint(random_list):
    for i in range(len(random_list)):
        print(random_list[i],end=" ")