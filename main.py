import random
import timeit
import matplotlib.pyplot as plt
import numpy as np
from hybridSort import hybridSort

K_VALUES = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
# N_VALUES = [500, 1_000, 5_000, 10_000, 50_000, 100_000, 500_000]
N_VALUES = [500, 1_000, 5_000, 10_000, 50_000, 100_000]
times_per_n = {n: [] for n in N_VALUES}


def avg_runtime():
    # Test code
    for n in N_VALUES:
        avg_times_for_n = []
        for k in K_VALUES:
            times = []
            for _ in range(3):
                arr = [random.randint(0, n) for _ in range(n)]
                time_to_sort = timeit.timeit(lambda: hybridSort(arr, 0, len(arr) - 1, k), number=1)
                times.append(time_to_sort)
            avg_times_for_n.append(np.mean(times))
        times_per_n[n] = avg_times_for_n

    # Plotting the performance of the hybrid sort
    plt.figure(figsize=(10, 6))
    for n in N_VALUES:
        plt.plot(K_VALUES, times_per_n[n], label=f"n={n}")

    plt.title("Hybrid Sort Performance with Different K Thresholds")
    plt.xlabel("K Values")
    plt.ylabel("Average Time (s)")
    plt.xticks(K_VALUES)
    plt.legend(title="Array Size")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    avg_runtime()
