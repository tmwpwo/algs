import random
import time
import matplotlib.pyplot as plt


class SelectionSort:
    @staticmethod
    def sorting(data):
        n = len(data)
        comparisons = 0
        swaps = 0

        for i in range(n - 1):
            min_index = i
            for j in range(i + 1, n):
                comparisons += 1
                if data[j] < data[min_index]:
                    min_index = j

            # if min_index != i:
            swaps += 1
            data[i], data[min_index] = data[min_index], data[i]

        return data, comparisons, swaps


class InsertionSort:
    @staticmethod
    def sorting(data):
        n = len(data)
        comparisons = 0
        swaps = 0

        for i in range(1, n):
            key = data[i]
            j = i - 1

            while j >= 0 and key < data[j]:
                comparisons += 1
                swaps += 1
                data[j + 1] = data[j]
                j -= 1
            swaps += 1
            data[j + 1] = key

        return data, comparisons, swaps


class BubbleSort:
    @staticmethod
    def sorting(data):
        n = len(data)
        comparisons = 0
        swaps = 0

        for i in range(n):
            for j in range(0, n - i - 1):
                comparisons += 1
                if data[j] > data[j + 1]:
                    swaps += 1
                    data[j], data[j + 1] = data[j + 1], data[j]

        return data, comparisons, swaps


class MergeSort:
    @staticmethod
    def sorting(data):
        comparisons = 0
        swaps = 0
        if len(data) > 1:
            mid = len(data) // 2
            left_half = data[:mid]
            right_half = data[mid:]

            left_part = MergeSort.sorting(left_half)
            right_part = MergeSort.sorting(right_half)

            comparisons += left_part[1] + right_part[1]
            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                comparisons += 1
                if left_half[i] < right_half[j]:
                    data[k] = left_half[i]
                    i += 1
                else:
                    data[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                comparisons += 1
                data[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                comparisons += 1
                data[k] = right_half[j]
                j += 1
                k += 1

        return data, comparisons, swaps


class QuickSort:
    def __str__():
        return "QuickSort"

    @staticmethod
    def sorting(data):
        comparisons = 0
        swaps = 0

        def partition(arr, low, high):
            nonlocal comparisons, swaps
            i = low - 1
            pivot = arr[high]

            for j in range(low, high):
                comparisons += 1
                if arr[j] < pivot:
                    i += 1
                    swaps += 1
                    arr[i], arr[j] = arr[j], arr[i]

            swaps += 1
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1

        def quick_sort(arr, low, high):
            nonlocal comparisons, swaps
            if low < high:
                pi = partition(arr, low, high)
                quick_sort(arr, low, pi - 1)
                quick_sort(arr, pi + 1, high)

        n = len(data)
        quick_sort(data, 0, n - 1)
        return data, comparisons, swaps


def binary_search(array, x, low, high):
    if high >= low:
        mid = low + (high - low) // 2
        if array[mid] == x:
            return mid

        elif array[mid] > x:
            return binary_search(array, x, low, mid - 1)
        else:
            return binary_search(array, x, mid + 1, high)
    else:
        return -1


def bench(data_set) -> list[dict]:
    res = {}

    for alg in sortingAlgs:
        algs_res = []
        for dataset_name, data in data_set:
            start_time = time.time()
            sorted_data, comparisons, swaps = alg.sorting(data.copy())
            end_time = time.time()
            time_taken_for_algs = end_time - start_time

            x = random.randint(1, 100)
            start = time.time()
            result = binary_search(sorted_data, x, 0, len(sorted_data) - 1)
            end = time.time()
            time_taken_for_binary = end - start
            if result != -1:
                print(
                    x,
                    "in",
                    dataset_name,
                    "Element is present at index " + str(result),
                    "and time taken to find was: ",
                    time_taken_for_binary,
                )
            else:
                print(x, "in", dataset_name, "Not found")

            algs_res.append(
                {
                    "data_set_name": dataset_name,
                    "elems": len(data),
                    "time": time_taken_for_algs,
                    "comparisons": comparisons,
                    "swaps": swaps,
                }
            )
        res[alg] = algs_res
    return res


if __name__ == "__main__":
    # Generate random data
    data_sets = [
        ("Set1", [random.randint(1, 100) for _ in range(100)]),
        ("Set2", [random.randint(1, 1000) for _ in range(1000)]),
        ("Set3", [random.randint(1, 5000) for _ in range(5000)]),
    ]

    data_sets_for_binary = [
        ("x1", random.randint(1, 100)),
        ("x2", random.randint(1, 1000)),
        ("x3", random.randint(1, 5000)),
    ]

    sortingAlgs = [BubbleSort, InsertionSort, SelectionSort, MergeSort, QuickSort]

    res = bench(data_sets)
    for alg, results in res.items():
        print(alg.__name__ + "\n" + "\n".join([str(result) for result in results]))

    z = []
    y = []
    y2 = []
    y3 = []
    for i in sortingAlgs:
        x = res[i][0]
        y.append(x["time"])
        z.append(i.__name__)

    for i in sortingAlgs:
        x = res[i][1]
        y2.append(x["time"])

    for i in sortingAlgs:
        x = res[i][2]
        y3.append(x["time"])

    fig = plt.figure(figsize=(20, 20))

    plt.subplot(221)
    plt.bar(z, y, color="maroon", width=0.3)
    plt.ylabel("time in seconds")
    plt.title("execution time for each algorithm, 100 el array")

    plt.subplot(222)
    plt.bar(z, y2, color="maroon", width=0.3)
    plt.ylabel("time in seconds")
    plt.title("execution time for each algorithm, 1000 el array")

    plt.subplot(223)
    plt.bar(z, y3, color="maroon", width=0.3)
    plt.ylabel("time in seconds")
    plt.title("execution time for each algorithm, 5000 el array")

    plt.plot()
    plt.show()
