def mergeSort(random_list):
    if len(random_list) > 1:

        r = len(random_list) // 2
        L = random_list[:r]
        M = random_list[r:]

        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                random_list[k] = L[i]
                i += 1
            else:
                random_list[k] = M[j]
                j += 1
            k += 1

        while i < len(L):
            random_list[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            random_list[k] = M[j]
            j += 1
            k += 1

def printMergeList(random_list):
    for i in range(len(random_list)):
        print(random_list[i], end=" ")