import random
import timeit
import matplotlib.pyplot as plt
import numpy as np

K_VALUES = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]
N_VALUES = [1_000, 10_000, 100_000, 500_000, 1_000_000]
times_per_n = {n: [] for n in N_VALUES}

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

# Hybrid Sort
def hybridSort(arr, l, r, k):
    if len(arr) <= k:
        insertionSort(arr)
    elif l < r:
        m = l + (r - l) // 2
        hybridSort(arr, l, m, k)
        hybridSort(arr, m + 1, r, k)
        merge(arr, l, m, r)

def __main__():
    # Test code
    for n in N_VALUES:
        avg_times_for_n = []
        for k in K_VALUES:
            times = []
            for _ in range(3):
                arr = [random.randint(0, 500_000) for _ in range(n)]
                time_to_sort = timeit.timeit(lambda: hybridSort(arr, 0, len(arr) - 1, k), number=1)
                times.append(time_to_sort)
            avg_times_for_n.append(np.mean(times))
        times_per_n[n] = avg_times_for_n

    # Plotting the performance of the hybrid sort
    plt.figure(figsize=(10, 6))
    for n in N_VALUES:
        plt.plot(K_VALUES, times_per_n[n], label=f"n={n}")

    plt.title("Hybrid Sort Performance with Different K Thresholds")
    plt.xlabel("K values")
    plt.ylabel("Average time (s)")
    plt.xticks(K_VALUES)
    plt.legend(title="Array Size")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    __main__()
