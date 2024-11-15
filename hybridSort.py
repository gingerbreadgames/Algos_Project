# Merge Sort helper
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = arr[l:m + 1]
    R = arr[m + 1:r + 1]

    i, j, k = 0, 0, l  # Initial index of merged subarray

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


# Insertion Sort
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Merge Sort
def mergeSort(arr, l, r, k):
    if l < r:
        m = l + (r - l) // 2
        hybridSort(arr, l, m, k)
        hybridSort(arr, m + 1, r, k)
        merge(arr, l, m, r)


# Hybrid Sort
def hybridSort(arr, l, r, k):
    if len(arr) <= k:
        insertionSort(arr)
    elif l < r:
        mergeSort(arr, l, r, k)