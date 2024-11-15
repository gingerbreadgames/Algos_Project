import random
import timeit
import matplotlib.pyplot as plt
import numpy as np
from hybridSort import hybridSort

K_VALUES = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
N_VALUES = [1_000, 5_000, 10_000, 50_000, 100_000]
times_per_n = {n: [] for n in N_VALUES}
optimal_k_values = {n: 0 for n in N_VALUES}


# Deliverable 1.2
# ---------------------------------------------------------------------------------------------------------
def avg_runtime(isSorted=False):
    # Test code
    for n in N_VALUES:
        avg_times_for_n = []
        for k in K_VALUES:
            times = []
            for _ in range(5):
                arr = list(range(n)) if isSorted else [random.randint(0, n) for _ in range(n)]
                time_to_sort = timeit.timeit(lambda: hybridSort(arr.copy(), 0, len(arr) - 1, k), number=1)
                times.append(time_to_sort)
            avg_times_for_n.append(np.mean(times))
        times_per_n[n] = avg_times_for_n

    # Plotting the performance of the hybrid sort
    plt.figure(figsize=(10, 6))
    for n in N_VALUES:
        plt.plot(K_VALUES, times_per_n[n], label=f"n={n}")

    title = "Hybrid Sort Performance with Different K Thresholds (Sorted Data)" if isSorted else "Hybrid Sort Performance with Different K Thresholds (Random Data)"
    plt.title(title)
    plt.xlabel("K Values")
    plt.ylabel("Average Time (s)")
    plt.xticks(K_VALUES)
    plt.legend(title="Array Size")
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.show()
# ---------------------------------------------------------------------------------------------------------


# Deliverable 1.3
# ---------------------------------------------------------------------------------------------------------
def optimal_k_value():
    for n in N_VALUES:
        runtimes = times_per_n[n]
        optimal_k_values[n] = K_VALUES[np.argmin(runtimes)]

    # Plotting the optimal k values
    plt.figure(figsize=(10, 6))
    plt.plot(N_VALUES, list(optimal_k_values.values()), marker="o")
    plt.title("Optimal K Value for Hybrid Sort")
    plt.xlabel("Array Size")
    plt.ylabel("Optimal K Value")
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.show()
# ---------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    avg_runtime()
    optimal_k_value()

    # Deliverable 1.4
    # ------------------------------
    avg_runtime(True)
    optimal_k_value()
    # ------------------------------
 