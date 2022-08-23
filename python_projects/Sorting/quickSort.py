def quickSort(random_list):
    if len(random_list) <= 1:
        return random_list

    elem = random_list[0]
    left = list(filter(lambda x: x < elem, random_list))
    center = [i for i in random_list if i == elem]
    right = list(filter(lambda x: x > elem, random_list))

    return quickSort(left) + center + quickSort(right)
