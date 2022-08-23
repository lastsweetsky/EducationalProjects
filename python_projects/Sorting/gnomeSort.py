def gnomeSort(random_list, n):
    index = 0

    while index < len(random_list):
        if index == 0:
            index = index + 1
        if random_list[index] >= random_list[index - 1]:
            index = index + 1
        else:
            random_list[index], random_list[index - 1] = random_list[index - 1], random_list[index]
            index = index - 1

    return random_list