import sys
import time
import random

# Set a higher recursion limit
sys.setrecursionlimit(2000)

# Randomized partition (pivot chosen randomly)
def partition_randomized(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Randomized quicksort function
def randomized_quicksort(arr, low, high):
    if low < high:
        pi = partition_randomized(arr, low, high)
        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)

# Helper function for randomized quicksort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    randomized_quicksort(arr, 0, len(arr) - 1)
    return arr


# Deterministic partition (first element as pivot)
def partition_deterministic(arr, low, high):
    pivot = arr[low]  # Pivot is the first element
    i = low + 1
    
    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    
    arr[low], arr[i - 1] = arr[i - 1], arr[low]  # Place the pivot in correct position
    return i - 1

# Deterministic quicksort function
def deterministic_quicksort(arr, low, high):
    if low < high:
        pi = partition_deterministic(arr, low, high)
        deterministic_quicksort(arr, low, pi - 1)
        deterministic_quicksort(arr, pi + 1, high)

# Helper function for deterministic quicksort
def quicksort_deterministic(arr):
    if len(arr) <= 1:
        return arr
    deterministic_quicksort(arr, 0, len(arr) - 1)
    return arr


# Timing function
def time_algorithm(func, arr):
    start_time = time.time()
    func(arr)
    end_time = time.time()
    return end_time - start_time

# Run experiments
def run_experiments():
    input_sizes = [1000, 5000, 10000, 20000]  # Different array sizes

    for n in input_sizes:
        # Generate test cases
        random_array = [random.randint(0, 10000) for _ in range(n)]
        sorted_array = list(range(n))
        reverse_sorted_array = list(range(n, 0, -1))
        repeated_array = [42] * n  # All elements are the same

        test_cases = {
            "Random": random_array,
            "Sorted": sorted_array,
            "Reverse Sorted": reverse_sorted_array,
            "Repeated": repeated_array,
        }

        print(f"\nArray Size: {n}")
        for case_name, case_array in test_cases.items():
            print(f"\nTest Case: {case_name}")

            # Time Randomized Quicksort
            randomized_time = time_algorithm(lambda x: quicksort(x), case_array[:])
            print(f"Randomized Quicksort Time: {randomized_time:.6f} seconds")

            # Time Deterministic Quicksort
            deterministic_time = time_algorithm(lambda x: quicksort_deterministic(x), case_array[:])
            print(f"Deterministic Quicksort Time: {deterministic_time:.6f} seconds")

# Run the experiments
run_experiments()
