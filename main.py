# (Порівняйте три алгоритми сортування: злиттям, вставками та Timsort за часом виконання.)

import timeit
import random


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def timsort(arr):
    arr.sort()


def benchmark_sorting_algorithms():
    sizes = [100, 1000, 10000]
    results = {}

    for size in sizes:
        data = random.sample(range(size * 10), size)
        results[size] = {}

        # Benchmark insertion sort
        insertion_time = timeit.timeit(lambda: insertion_sort(data.copy()), number=1)
        results[size]['сортування злиттям'] = insertion_time

        # Benchmark merge sort
        merge_time = timeit.timeit(lambda: merge_sort(data.copy()), number=1)
        results[size]['сотрування вставками'] = merge_time

        # Benchmark timsort (built-in sort)
        timsort_time = timeit.timeit(lambda: timsort(data.copy()), number=1)
        results[size]['timsort'] = timsort_time

    return results


def main():
    results = benchmark_sorting_algorithms()
    for size in results:
        print(f"Розмір масиву: {size}")
        for alg in results[size]:
            print(f"   {alg}: {results[size][alg]:.6f} секунд")


if __name__ == "__main__":
    main()
