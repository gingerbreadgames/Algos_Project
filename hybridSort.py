# Merge helper function
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = arr[l:m + 1]
    R = arr[m + 1:r + 1]

    i, j, k = 0, 0, l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# Merge Sort
def mergeSort(arr, l, r, k):
    if l < r:
        m = l + (r - l) // 2
        mergeSort(arr, l, m, k)
        mergeSort(arr, m + 1, r, k)
        merge(arr, l, m, r)


# Insertion Sort
def insertionSort(arr, l, r):
    for i in range(l + 1, r + 1):
        key = arr[i]
        j = i - 1
        while j >= l and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# HybridSort implementation
def hybridSort(arr, l, r, k):
    if r - l + 1 <= k:
        insertionSort(arr, l, r)
    else:
        mergeSort(arr, l, r, k)
