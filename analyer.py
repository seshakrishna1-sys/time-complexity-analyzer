import time
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def run_experiment():
    input_sizes = [100, 500, 1000, 2000]

    print("Input Size | Bubble Sort Time | Binary Search Time")
    print("-" * 50)

    for size in input_sizes:
        arr = [random.randint(1, size) for _ in range(size)]
        sorted_arr = sorted(arr)

        start = time.time()
        bubble_sort(arr.copy())
        bubble_time = time.time() - start

        start = time.time()
        binary_search(sorted_arr, sorted_arr[-1])
        binary_time = time.time() - start

        print(f"{size:<10} | {bubble_time:.6f}s       | {binary_time:.6f}s")

if __name__ == "__main__":
    run_experiment()
