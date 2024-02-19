import timeit
import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_pointer, right_pointer = 0, 0

    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1

    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])
    return result

def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        position = i

        while position > 0 and arr[position - 1] > current:
            arr[position] = arr[position - 1]
            position -= 1

        arr[position] = current

def main():
    random.seed(42)  # Задаємо однакове початкове значення для генератора випадкових чисел

    # Генеруємо список розміром 10000 з випадковими числами
    data = [random.randint(0, 100000) for _ in range(10000)]

    # Сортування злиттям
    merge_sort_time = timeit.timeit(lambda: merge_sort(data.copy()), number=1)
    print(f"Час сортування злиттям: {merge_sort_time} сек")

    # Сортування вставками
    insertion_sort_time = timeit.timeit(lambda: insertion_sort(data.copy()), number=1)
    print(f"Час сортування вставками: {insertion_sort_time} сек")

    # Сортування Timsort (вбудований у Python)
    timsort_time = timeit.timeit(lambda: sorted(data.copy()), number=1)
    print(f"Час сортування Timsort: {timsort_time} сек")

if __name__ == "__main__":
    main()
